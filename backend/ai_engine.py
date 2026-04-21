from google import genai
import time
import random
import os
from dotenv import load_dotenv

load_dotenv()

# Load API keys from .env — add GEMINI_KEY_4, GEMINI_KEY_5 as needed
API_KEYS = [v for k, v in sorted(os.environ.items())
            if k.startswith("GEMINI_KEY_") and v.strip()]

if not API_KEYS:
    raise RuntimeError("No GEMINI_KEY_* found in .env — add at least GEMINI_KEY_1")

def _make_client(api_key: str):
    return genai.Client(api_key=api_key)

# Only proven-working models (404s removed)
MODELS = [
    "gemini-2.0-flash",
    "gemini-2.5-flash",
    "gemini-flash-latest",
    "gemini-2.0-flash-lite",
]

# ─────────────────────────────────────────────────────────
# Generic fallback animation — plays when ALL models fail
# ─────────────────────────────────────────────────────────
FALLBACK_SCRIPT = '''from manim import *

class MainScene(Scene):
    def construct(self):
        self.camera.background_color = BLACK

        title = Text("EduMotion AI", font_size=56, color=TEAL_A)
        sub   = Text("Your ideas, animated.", font_size=28, color=WHITE)
        sub.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(title, shift=UP*0.3), run_time=0.8)
        self.play(FadeIn(sub), run_time=0.6)
        self.wait(2.5)
        self.play(FadeOut(title), FadeOut(sub), run_time=0.5)

        # Animated concept: idea → video pipeline
        idea_box  = Rectangle(width=3, height=1.2, color=TEAL_A, fill_color=TEAL_E, fill_opacity=0.3)
        idea_lbl  = Text("Your Idea", font_size=26, color=WHITE)
        idea_lbl.move_to(idea_box)
        idea_grp  = VGroup(idea_box, idea_lbl).shift(LEFT * 3.5)

        ai_box   = Rectangle(width=3, height=1.2, color=PINK, fill_color=MAROON, fill_opacity=0.3)
        ai_lbl   = Text("EduMotion AI", font_size=22, color=WHITE)
        ai_lbl.move_to(ai_box)
        ai_grp   = VGroup(ai_box, ai_lbl)

        vid_box  = Rectangle(width=3, height=1.2, color=GREEN, fill_color=GREEN_E, fill_opacity=0.3)
        vid_lbl  = Text("Animated Video", font_size=22, color=WHITE)
        vid_lbl.move_to(vid_box)
        vid_grp  = VGroup(vid_box, vid_lbl).shift(RIGHT * 3.5)

        arr1 = Arrow(idea_grp.get_right(), ai_grp.get_left(), buff=0.1, color=TEAL_A)
        arr2 = Arrow(ai_grp.get_right(), vid_grp.get_left(), buff=0.1, color=GREEN)

        self.play(FadeIn(idea_grp), run_time=0.6)
        self.wait(0.5)
        self.play(GrowArrow(arr1), run_time=0.6)
        self.play(FadeIn(ai_grp), run_time=0.6)
        self.wait(0.5)
        self.play(GrowArrow(arr2), run_time=0.6)
        self.play(FadeIn(vid_grp), run_time=0.6)
        self.wait(2.5)
        self.play(*[FadeOut(m) for m in [idea_grp, arr1, ai_grp, arr2, vid_grp]], run_time=0.5)

        done = Text("Try again in a moment!", font_size=36, color=YELLOW)
        hint = Text("AI servers are busy right now.", font_size=24, color=LIGHT_GRAY)
        hint.next_to(done, DOWN, buff=0.4)
        self.play(FadeIn(done), FadeIn(hint), run_time=0.7)
        self.wait(3.0)
'''

FALLBACK_VOICE_TEXT = "EduMotion AI turns your ideas into educational animated videos. The AI servers are currently busy. Please try again in a moment."

# ─────────────────────────────────────────────────────────
# Single-stage prompt: plan + code + voice narration at once
# ─────────────────────────────────────────────────────────
UNIFIED_PROMPT = """\
You are an expert educational animated video creator using Manim Python.
Your output has TWO parts separated by exactly this marker: ===VOICE===

PART 1 — Complete Manim Python code (before the marker)
PART 2 — Voiceover narration text (after the marker)

═══ INPUT ═══
TOPIC: {topic}
LANGUAGE: {language} ({lang_instruction})
DURATION: {duration} seconds (MUST fill this entire time)
STYLE: {style}
ASPECT RATIO: {aspect_ratio}

═══ TIMING RULES ═══
The video must last EXACTLY {duration} seconds.
- You have 7 scenes. Each scene must end with:  self.wait({scene_wait:.1f})
- Final scene ends with:  self.wait({final_wait:.1f})
- Animation run_times: 0.5–0.8 per play() call
- Total self.wait() across all scenes ≥ {total_wait:.1f} seconds
- NEVER skip self.wait() calls — they define video length

═══ VIDEO STRUCTURE (7 scenes) ═══
Scene 1 (Hook): Bold title + question — {hook_dur}s
Scene 2 (Setup): Real-world context — {mid_dur}s  
Scene 3 (Problem): Show the challenge visually — {mid_dur}s
Scene 4 (Explanation): Core concept animated in detail — {mid_dur}s
Scene 5 (Solution): Step-by-step animated answer — {mid_dur}s
Scene 6 (Impact): Why it matters — {mid_dur}s
Scene 7 (Summary): 3 bullet points animated — {hook_dur}s

═══ VISUAL SYSTEM ═══
- self.camera.background_color = BLACK  (in construct() — REQUIRED)
- Primary:   TEAL_A (neon cyan glow)
- Accent:    PINK (hot pink highlights)
- Success:   GREEN (correct answers, final state)
- Text:      WHITE
- Problem:   RED_B
- Use VGroup to group related elements

═══ MANIM STRICT RULES (violations CRASH the program) ═══
1. from manim import *  (first line)
2. Exactly ONE class: MainScene(Scene)
3. FORBIDDEN: MathTex, Tex, SVGMobject, ImageMobject  → CRASH
4. ALLOWED: Text, Circle, Square, Rectangle, Arrow, Line, NumberLine,
            Dot, VGroup, Polygon, Brace, DoubleArrow, Triangle, AnnularSector
5. VALID COLORS ONLY:
   BLACK WHITE GRAY LIGHT_GRAY DARK_GRAY
   BLUE BLUE_A BLUE_B BLUE_C BLUE_D BLUE_E
   RED  RED_A  RED_B  RED_C  RED_D  RED_E
   GREEN GREEN_A GREEN_B GREEN_C GREEN_D GREEN_E
   YELLOW YELLOW_A YELLOW_B YELLOW_C YELLOW_D YELLOW_E
   TEAL TEAL_A TEAL_B TEAL_C TEAL_D TEAL_E
   ORANGE PINK GOLD MAROON
   ✗ NEVER: CYAN PURPLE VIOLET INDIGO BROWN MAGENTA
6. Math → plain Text strings: Text("E = m * c^2")
7. No imports except: from manim import *
8. ZERO syntax errors

═══ VOICE NARRATION RULES ═══
- Natural, conversational, educational tone
- Match the video scenes (7 paragraphs, one per scene)
- Max 15 words per sentence
- Language: {lang_instruction}
- Output ONLY the spoken text (no stage directions, no brackets)

═══ OUTPUT FORMAT ═══
[complete Manim Python code here — start with: from manim import *]
===VOICE===
[voiceover narration text here — one paragraph per scene]
"""


def _call_gemini(prompt: str) -> str:
    """
    Try every (API key × model) combination with exponential backoff.
    This gives us 3 keys × 6 models = 18 total attempts before giving up.
    """
    last_error = None
    attempt = 0
    for api_key in API_KEYS:
        client = _make_client(api_key)
        for model_name in MODELS:
            attempt += 1
            try:
                response = client.models.generate_content(model=model_name, contents=prompt)
                text = response.text.strip()
                print(f"[ai_engine] ✓ key#{API_KEYS.index(api_key)+1} + {model_name}")
                return text
            except Exception as e:
                err_str = str(e)
                last_error = e
                is_quota = any(k in err_str for k in ("503", "UNAVAILABLE", "high demand", "overloaded", "429", "quota"))
                wait_sec = min(attempt * 0.8 + random.uniform(0, 0.5), 3)  # max 3s wait
                if is_quota:
                    print(f"[ai_engine] key#{API_KEYS.index(api_key)+1}/{model_name} → quota/503, next in {wait_sec:.1f}s")
                    time.sleep(wait_sec)
                else:
                    print(f"[ai_engine] key#{API_KEYS.index(api_key)+1}/{model_name} failed: {err_str[:80]}")
                continue
    raise Exception(f"503_ALL_MODELS: {last_error}")


def generate_manim_script(request):
    """
    Returns a tuple: (manim_code: str, voice_text: str)
    voice_text is a natural narration script for TTS — NOT just the topic title.
    """
    lang_instruction = (
        "output ALL text in Arabic using proper Arabic Unicode."
        if request.language == "ar"
        else "output ALL text in English."
    )

    # Timing calculations
    duration    = int(request.duration)
    num_scenes  = 7
    total_wait  = duration * 0.60
    scene_wait  = round(total_wait / num_scenes, 1)
    final_wait  = round(scene_wait, 1)
    hook_dur    = max(3, round(duration * 0.12))
    mid_dur     = max(3, round((duration - hook_dur * 2) / 5))

    prompt = UNIFIED_PROMPT.format(
        topic=request.topic,
        language=request.language,
        lang_instruction=lang_instruction,
        duration=duration,
        style=request.style,
        aspect_ratio=request.aspect_ratio,
        scene_wait=scene_wait,
        final_wait=final_wait,
        total_wait=total_wait,
        hook_dur=hook_dur,
        mid_dur=mid_dur,
        num_scenes=num_scenes,
    )

    print(f"[ai_engine] Generating video plan + Manim code + narration (single call)...")
    try:
        raw = _call_gemini(prompt)

        # Split on the voice marker
        if "===VOICE===" in raw:
            code_part, voice_part = raw.split("===VOICE===", 1)
        else:
            code_part  = raw
            voice_part = f"This video explains {request.topic}."

        # Strip markdown fences from code
        code = code_part.strip()
        if "```python" in code:
            code = code.split("```python")[1].split("```")[0].strip()
        elif "```" in code:
            code = code.split("```")[1].split("```")[0].strip()

        voice_text = voice_part.strip()
        print(f"[ai_engine] Code: {len(code)} chars | Voice: {len(voice_text)} chars")
        return code, voice_text

    except Exception as e:
        err_str = str(e)
        if "503_ALL_MODELS" in err_str or "503" in err_str or "UNAVAILABLE" in err_str:
            print("[ai_engine] All models returned 503 — using fallback animation.")
            return FALLBACK_SCRIPT.strip(), FALLBACK_VOICE_TEXT
        raise

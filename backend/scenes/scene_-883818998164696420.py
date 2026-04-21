from manim import *

config.pixel_width = 480
config.pixel_height = 854
config.frame_width = 8.0
config.frame_height = 14.22
config.background_color = "#1E1E2E"


class MainScene(Scene):
    def construct(self):
        # Configuration for vertical video
        self.camera.background_color = BLACK
        
        # --- SCENE 1: HOOK ---
        title = Text("NEWTON'S 2ND LAW", color=TEAL_A, font_size=70).shift(UP * 2)
        question = Text("WHY SO HEAVY?", color=PINK, font_size=50).shift(DOWN * 1)
        hook_group = VGroup(title, question)
        
        self.play(Write(title), run_time=0.8)
        self.play(FadeIn(question, shift=UP), run_time=0.8)
        self.wait(2.6)
        self.play(FadeOut(hook_group), run_time=0.5)

        # --- SCENE 2: SETUP ---
        small_box = Square(side_length=1, color=TEAL_A).shift(LEFT * 2 + UP * 2)
        large_box = Square(side_length=2.5, color=PINK).shift(LEFT * 1.5 + DOWN * 2)
        label_small = Text("1 kg", font_size=30).next_to(small_box, UP)
        label_large = Text("10 kg", font_size=30).next_to(large_box, UP)
        
        self.play(Create(small_box), Write(label_small), run_time=0.8)
        self.play(Create(large_box), Write(label_large), run_time=0.8)
        self.wait(2.6)

        # --- SCENE 3: PROBLEM ---
        arrow1 = Arrow(start=LEFT * 4 + UP * 2, end=LEFT * 2.5 + UP * 2, color=RED_B)
        arrow2 = Arrow(start=LEFT * 4 + DOWN * 2, end=LEFT * 3 + DOWN * 2, color=RED_B)
        push_text = Text("SAME FORCE", color=RED_B, font_size=40).shift(RIGHT * 2)
        
        self.play(GrowArrow(arrow1), GrowArrow(arrow2), run_time=0.8)
        self.play(Write(push_text), run_time=0.8)
        self.wait(2.6)
        self.play(FadeOut(small_box, large_box, label_small, label_large, arrow1, arrow2, push_text), run_time=0.5)

        # --- SCENE 4: EXPLANATION ---
        formula = Text("F = m * a", color=WHITE, font_size=90)
        box_f = Rectangle(height=1.5, width=1.5, color=RED_B).move_to(formula[0])
        box_m = Rectangle(height=1.5, width=1.5, color=PINK).move_to(formula[2])
        
        self.play(Write(formula), run_time=0.8)
        self.play(Create(box_f), Create(box_m), run_time=0.8)
        self.wait(2.6)
        self.play(FadeOut(box_f, box_m), run_time=0.5)

        # --- SCENE 5: SOLUTION ---
        formula.generate_target()
        formula.target.shift(UP * 3)
        
        m_up = Text("MASS UP", color=PINK, font_size=50).shift(LEFT * 2)
        a_down = Text("ACCEL DOWN", color=TEAL_A, font_size=50).shift(RIGHT * 2)
        arrow_up = Arrow(start=DOWN * 0.5, end=UP * 0.5, color=PINK).next_to(m_up, UP)
        arrow_down = Arrow(start=UP * 0.5, end=DOWN * 0.5, color=TEAL_A).next_to(a_down, DOWN)
        
        self.play(MoveToTarget(formula), run_time=0.8)
        self.play(Write(m_up), Write(a_down), GrowArrow(arrow_up), GrowArrow(arrow_down), run_time=0.8)
        self.wait(2.6)
        self.play(FadeOut(formula, m_up, a_down, arrow_up, arrow_down), run_time=0.5)

        # --- SCENE 6: IMPACT ---
        impact_bg = Circle(radius=3, color=DARK_GRAY).set_fill(DARK_GRAY, opacity=0.2)
        impact_text = Text("MORE MASS\nNEEDS\nMORE FORCE", color=GREEN, font_size=60, line_spacing=1)
        
        self.play(FadeIn(impact_bg), run_time=0.8)
        self.play(Write(impact_text), run_time=0.8)
        self.wait(2.6)
        self.play(FadeOut(impact_bg, impact_text), run_time=0.5)

        # --- SCENE 7: SUMMARY ---
        summary_title = Text("SUMMARY", color=TEAL_A, font_size=60).shift(UP * 4)
        b1 = Text("1. Force Pushes", font_size=40).shift(UP * 1.5)
        b2 = Text("2. Mass Resists", font_size=40).shift(ORIGIN)
        b3 = Text("3. Accel Results", font_size=40).shift(DOWN * 1.5)
        
        self.play(Write(summary_title), run_time=0.8)
        self.play(FadeIn(VGroup(b1, b2, b3), shift=RIGHT), run_time=0.8)
        self.wait(2.6)
        # Extra wait to reach exactly 30 seconds
        self.wait(0.6)
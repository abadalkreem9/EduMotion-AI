from manim import *

config.pixel_width = 480
config.pixel_height = 854
config.frame_width = 8.0
config.frame_height = 14.22
config.background_color = "#000000"


class MainScene(Scene):
    def construct(self):
        self.camera.background_color = BLACK

        # Scene 1 — Title
        title = Text("Bubble Sort", font_size=64, color=TEAL_A)
        subtitle = Text("A visual explanation", font_size=28, color=WHITE)
        subtitle.next_to(title, DOWN, buff=0.4)
        self.play(FadeIn(title), run_time=0.8)
        self.play(FadeIn(subtitle), run_time=0.5)
        self.wait(2.8)
        self.play(FadeOut(title), FadeOut(subtitle), run_time=0.4)

        # Scene 2 — Build bars
        values  = [5, 3, 8, 1, 9, 2, 7, 4, 6]
        colors  = [TEAL_A, BLUE_B, TEAL_C, BLUE_D, TEAL_B, BLUE_C, TEAL_D, BLUE_A, TEAL_E]
        bar_w   = 0.55
        gap     = 0.65
        start_x = -(len(values) - 1) * gap / 2

        def make_bars(vals):
            grp = VGroup()
            for i, v in enumerate(vals):
                bar = Rectangle(width=bar_w, height=v * 0.38,
                                fill_color=colors[i % len(colors)],
                                fill_opacity=0.9, stroke_color=WHITE, stroke_width=1)
                bar.move_to([start_x + i * gap, (v * 0.38) / 2 - 2.0, 0])
                lbl = Text(str(v), font_size=20, color=WHITE)
                lbl.next_to(bar, UP, buff=0.08)
                grp.add(bar, lbl)
            return grp

        bars = make_bars(values)
        hdr  = Text("Unsorted Array", font_size=30, color=LIGHT_GRAY).to_edge(UP, buff=0.5)
        self.play(FadeIn(hdr), run_time=0.4)
        self.play(*[FadeIn(b) for b in bars], run_time=0.8)
        self.wait(2.8)

        # Scene 3 — Sorting pass
        self.play(FadeOut(hdr), run_time=0.3)
        sort_lbl = Text("Comparing and swapping...", font_size=28, color=PINK).to_edge(UP, buff=0.5)
        self.play(FadeIn(sort_lbl), run_time=0.4)
        arr = list(values)
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                new_bars = make_bars(arr)
                self.play(Transform(bars, new_bars), run_time=0.5)
                self.wait(0.2)
        self.wait(2.8)
        self.play(FadeOut(sort_lbl), run_time=0.3)

        # Scene 4 — Done
        done = Text("Sorted!", font_size=54, color=GREEN)
        sub  = Text("Bubble Sort complete", font_size=26, color=WHITE)
        sub.next_to(done, DOWN, buff=0.4)
        self.play(FadeOut(bars), run_time=0.5)
        self.play(FadeIn(done), FadeIn(sub), run_time=0.8)
        self.wait(3.5)
        self.play(FadeOut(done), FadeOut(sub), run_time=0.5)
        self.wait(1.0)
from manim import *

config.pixel_width = 854
config.pixel_height = 480
config.frame_width = 14.22
config.frame_height = 8.0
config.background_color = "#1E1E2E"


class MainScene(Scene):
    def construct(self):
        # Initial Setup
        self.camera.background_color = BLACK
        self.wait(0.3)

        # Scene 1: Hook
        title = Text("The Geometry Secret", color=TEAL_A).scale(1.2)
        subtitle = Text("How to find the missing side?", color=WHITE).scale(0.8).next_to(title, DOWN)
        scene1 = VGroup(title, subtitle)
        self.play(FadeIn(scene1), run_time=0.8)
        self.wait(1.3)
        self.play(FadeOut(scene1), run_time=0.8)

        # Scene 2: Setup
        # Create a right triangle
        p1 = [ -1.5, -1, 0 ]
        p2 = [ 1.5, -1, 0 ]
        p3 = [ -1.5, 2, 0 ]
        tri = Polygon(p1, p2, p3, color=TEAL_A, stroke_width=6)
        label_a = Text("a", color=WHITE).next_to(Line(p1, p2), DOWN)
        label_b = Text("b", color=WHITE).next_to(Line(p1, p3), LEFT)
        scene2 = VGroup(tri, label_a, label_b)
        self.play(Create(tri), Write(label_a), Write(label_b), run_time=0.8)
        self.wait(1.3)

        # Scene 3: Problem
        label_c = Text("c = ?", color=RED_B).move_to([0.5, 0.8, 0])
        self.play(Write(label_c), tri.animate.set_stroke(color=RED_B), run_time=0.8)
        self.wait(1.3)

        # Scene 4: Explanation
        formula = Text("a^2 + b^2 = c^2", color=PINK).to_edge(UP)
        self.play(Write(formula), run_time=0.8)
        self.wait(1.3)

        # Scene 5: Solution (Squares)
        sq_a = Square(side_length=3, fill_opacity=0.3, color=PINK).next_to(Line(p1, p2), DOWN, buff=0)
        sq_b = Square(side_length=3, fill_opacity=0.3, color=PINK).next_to(Line(p1, p3), LEFT, buff=0)
        self.play(FadeIn(sq_a), FadeIn(sq_b), label_c.animate.set_color(GREEN), run_time=0.8)
        self.wait(1.3)

        # Scene 6: Impact
        self.play(FadeOut(sq_a), FadeOut(sq_b), FadeOut(tri), FadeOut(label_a), FadeOut(label_b), run_time=0.5)
        impact_text = Text("Used in Architecture", color=GREEN).scale(1.1)
        self.play(Write(impact_text), run_time=0.8)
        self.wait(1.3)

        # Scene 7: Summary
        self.play(FadeOut(impact_text), FadeOut(label_c), FadeOut(formula), run_time=0.5)
        b1 = Text("1. Right Triangles Only", color=WHITE).scale(0.7).shift(UP*1)
        b2 = Text("2. Square the sides", color=WHITE).scale(0.7)
        b3 = Text("3. Sum equals c^2", color=WHITE).scale(0.7).shift(DOWN*1)
        summary = VGroup(b1, b2, b3)
        self.play(Write(summary), run_time=0.8)
        self.wait(1.3)
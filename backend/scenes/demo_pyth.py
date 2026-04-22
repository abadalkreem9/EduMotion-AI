from manim import *

class MainScene(Scene):
    def construct(self):
        self.camera.background_color = "#0f0f1a"

        title = Text("Pythagorean Theorem", font_size=42, color=BLUE_B, weight=BOLD)
        title.to_edge(UP, buff=0.4)
        self.play(Write(title), run_time=1)

        # Triangle points
        A = np.array([-2.5, -1.2, 0])
        B = np.array([ 1.5, -1.2, 0])
        C = np.array([ 1.5,  1.8, 0])

        tri = Polygon(A, B, C, color=WHITE, stroke_width=3)
        right_mark = RightAngle(Line(B, A), Line(B, C), length=0.28, color=YELLOW)

        a_lbl = Text("a", color=RED_B,   font_size=40).next_to(Line(A, B).get_center(), DOWN,  buff=0.25)
        b_lbl = Text("b", color=GREEN_B, font_size=40).next_to(Line(B, C).get_center(), RIGHT, buff=0.25)
        c_lbl = Text("c", color=YELLOW,  font_size=40).next_to(Line(A, C).get_center(), LEFT,  buff=0.25)

        self.play(Create(tri), Create(right_mark), run_time=1.2)
        self.play(Write(a_lbl), Write(b_lbl), Write(c_lbl), run_time=0.8)
        self.wait(0.3)

        # Colored squares
        sq_a = Square(side_length=1.5, color=RED_B,   fill_color=RED_B,   fill_opacity=0.25).move_to(A + np.array([0, -0.75, 0]))
        sq_b = Square(side_length=1.5, color=GREEN_B, fill_color=GREEN_B, fill_opacity=0.25).move_to(B + np.array([0.75, 0.3, 0]))

        self.play(FadeIn(sq_a, shift=DOWN*0.3), FadeIn(sq_b, shift=RIGHT*0.3), run_time=0.9)

        # Formula using Text only (no LaTeX)
        formula = Text("a² + b² = c²", font_size=52, color=WHITE)
        formula.to_edge(DOWN, buff=0.55)
        box = SurroundingRectangle(formula, color=BLUE_B, buff=0.18, corner_radius=0.1)

        self.play(Write(formula), Create(box), run_time=1.1)
        self.wait(1.2)

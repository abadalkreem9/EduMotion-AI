from manim import *

config.pixel_width = 854
config.pixel_height = 480
config.frame_width = 14.22
config.frame_height = 8.0
config.background_color = "#111111"


class MainScene(Scene):
    def construct(self):
        self.camera.background_color = BLACK

        # --- Colors ---
        TEAL_A = "#00FFFF"  # Neon Cyan Glow
        PINK = "#FF69B4"    # Hot Pink
        GREEN = "#00FF00"   # Success Green
        WHITE = "#FFFFFF"
        RED_B = "#FF4500"   # Problem Red-Orange

        # --- Scene 1: Hook (4s) ---
        title = Text("Pythagorean Theorem", font_size=72, weight=BOLD, color=TEAL_A)
        question = Text("How does it help us?", font_size=48, color=WHITE).next_to(title, DOWN, buff=0.8)

        self.play(Write(title), run_time=0.6) # Animation: 0.6s
        self.play(FadeIn(question, shift=DOWN), run_time=0.5) # Animation: 0.5s
        self.wait(2.6)

        self.play(FadeOut(title, question))

        # --- Scene 2: Setup (4s) ---
        context_text = Text("Imagine building a ramp.", font_size=48, color=WHITE).to_edge(UP)

        # Base and Height lines
        line_b = Line(ORIGIN, 4 * RIGHT, color=TEAL_A, stroke_width=8) # Base
        line_a = Line(ORIGIN, 3 * UP, color=TEAL_A, stroke_width=8)  # Height
        
        base_label = Text("Base", font_size=36, color=WHITE).next_to(line_b, DOWN)
        height_label = Text("Height", font_size=36, color=WHITE).next_to(line_a, LEFT)

        diagram_group_s2 = VGroup(line_a, line_b, base_label, height_label).move_to(ORIGIN)

        self.play(Write(context_text), run_time=0.6) # Animation: 0.6s
        self.play(Create(line_b), Create(line_a), FadeIn(base_label), FadeIn(height_label), run_time=0.6) # Animation: 0.6s
        self.wait(2.6)

        self.play(FadeOut(context_text, base_label, height_label))

        # --- Scene 3: Problem (4s) ---
        # Recreate the elements for a clean start and controlled positioning
        line_a_s3 = Line(ORIGIN, 3 * UP, color=TEAL_A, stroke_width=8).shift(LEFT * 2 + DOWN * 0.5)
        line_b_s3 = Line(ORIGIN, 4 * RIGHT, color=TEAL_A, stroke_width=8).shift(LEFT * 2 + DOWN * 0.5)

        # Hypotenuse
        line_c_s3 = Line(line_a_s3.get_end(), line_b_s3.get_end(), color=RED_B, stroke_width=8)

        # Right angle indicator
        right_angle_square = Square(side_length=0.4, color=PINK, fill_opacity=1).move_to(line_b_s3.get_start() + 0.2*RIGHT + 0.2*UP)

        # Labels for a, b, c
        label_a_text = Text("a", font_size=48, color=WHITE).next_to(line_a_s3, LEFT)
        label_b_text = Text("b", font_size=48, color=WHITE).next_to(line_b_s3, DOWN)
        label_c_text = Text("c", font_size=48, color=WHITE).next_to(line_c_s3, RIGHT * 0.5 + UP * 0.5)

        self.play(Create(VGroup(line_a_s3, line_b_s3)), run_time=0.5) # Animation: 0.5s
        self.play(Create(line_c_s3), run_time=0.6) # Animation: 0.6s
        self.play(
            FadeIn(right_angle_square),
            FadeIn(label_a_text),
            FadeIn(label_b_text),
            FadeIn(label_c_text),
            run_time=0.5 # Animation: 0.5s
        )
        self.wait(2.6)

        triangle_group_s3 = VGroup(line_a_s3, line_b_s3, line_c_s3, right_angle_square, label_a_text, label_b_text, label_c_text)
        self.play(FadeOut(triangle_group_s3))


        # --- Scene 4: Explanation (4s) ---
        theorem_text = Text("a^2 + b^2 = c^2", font_size=72, color=TEAL_A)

        # Simplified representation of squares
        square_a_vis = Square(side_length=1.5, color=PINK, fill_opacity=0.8) # Represents 3*3
        square_b_vis = Square(side_length=2.0, color=PINK, fill_opacity=0.8) # Represents 4*4
        square_c_vis = Square(side_length=2.5, color=GREEN, fill_opacity=0.8) # Represents 5*5

        plus_sign = Text("+", font_size=72, color=WHITE)
        equals_sign = Text("=", font_size=72, color=WHITE)

        squares_group_s4 = VGroup(square_a_vis, plus_sign, square_b_vis, equals_sign, square_c_vis).arrange(RIGHT, buff=0.7).move_to(ORIGIN)

        self.play(Write(theorem_text), run_time=0.6) # Animation: 0.6s
        self.play(theorem_text.animate.to_edge(UP), run_time=0.5) # Animation: 0.5s
        self.play(Create(squares_group_s4), run_time=0.5) # Animation: 0.5s
        self.wait(2.6)

        self.play(FadeOut(theorem_text, squares_group_s4))


        # --- Scene 5: Solution (4s) ---
        # Recalculate triangle position for clarity
        triangle_base_point = LEFT * 4 + DOWN * 1.5
        s5_line_b = Line(triangle_base_point, triangle_base_point + 4 * RIGHT, color=TEAL_A, stroke_width=8) # Base = 4
        s5_line_a = Line(triangle_base_point, triangle_base_point + 3 * UP, color=TEAL_A, stroke_width=8)  # Height = 3
        s5_line_c = Line(s5_line_a.get_end(), s5_line_b.get_end(), color=TEAL_A, stroke_width=8) # Hypotenuse = ?

        s5_triangle_group = VGroup(s5_line_a, s5_line_b, s5_line_c)
        s5_triangle_group.move_to(LEFT * 4)

        s5_label_a_val = Text("a=3", font_size=40, color=WHITE).next_to(s5_line_a, LEFT)
        s5_label_b_val = Text("b=4", font_size=40, color=WHITE).next_to(s5_line_b, DOWN)
        s5_label_c_unknown = Text("c=?", font_size=40, color=RED_B).next_to(s5_line_c, RIGHT * 0.5 + UP * 0.5)

        formula_display_pos = ORIGIN + RIGHT*3 + UP*1.5

        formula_step1 = Text("3^2 + 4^2 = c^2", font_size=60, color=TEAL_A).move_to(formula_display_pos)
        formula_step2 = Text("9 + 16 = c^2", font_size=60, color=TEAL_A).move_to(formula_display_pos)
        formula_step3 = Text("25 = c^2", font_size=60, color=TEAL_A).move_to(formula_display_pos)
        final_c_val = Text("c = 5", font_size=72, color=GREEN).move_to(formula_display_pos)

        self.play(
            Create(s5_triangle_group),
            FadeIn(s5_label_a_val), FadeIn(s5_label_b_val), FadeIn(s5_label_c_unknown),
            run_time=0.6 # Animation: 0.6s
        )
        self.play(Write(formula_step1), run_time=0.6) # Animation: 0.6s
        self.play(TransformMatchingStrings(formula_step1, formula_step2, run_time=0.6)) # Animation: 0.6s
        self.play(TransformMatchingStrings(formula_step2, formula_step3, run_time=0.7)) # Animation: 0.7s (THE one 0.7s call)
        self.play(TransformMatchingStrings(formula_step3, final_c_val, run_time=0.6)) # Animation: 0.6s
        self.wait(2.6)

        self.play(FadeOut(s5_triangle_group, s5_label_a_val, s5_label_b_val, s5_label_c_unknown, final_c_val))


        # --- Scene 6: Impact (4s) ---
        impact_text_1 = Text("Crucial for:", font_size=48, color=WHITE).to_edge(UP)

        # Simple icons
        # Construction (House)
        house_roof = Triangle(color=TEAL_A, fill_opacity=0.8).scale(0.8).shift(UP * 0.5)
        house_base = Rectangle(width=2, height=1.5, color=TEAL_A, fill_opacity=0.8).next_to(house_roof, DOWN, buff=0)
        icon_construction = VGroup(house_roof, house_base).next_to(impact_text_1, DOWN, buff=1).shift(LEFT * 4)
        construction_label = Text("Construction", font_size=36, color=WHITE).next_to(icon_construction, DOWN)

        # Navigation (Arrow)
        icon_navigation = Arrow(start=ORIGIN, end=UP*1.5, color=TEAL_A, stroke_width=10).next_to(icon_construction, RIGHT, buff=2)
        navigation_label = Text("Navigation", font_size=36, color=WHITE).next_to(icon_navigation, DOWN)

        # Gaming (Controller/Screen)
        game_screen = Rectangle(width=2.5, height=1.5, color=TEAL_A, fill_opacity=0.8)
        game_button1 = Circle(radius=0.2, color=PINK, fill_opacity=0.8).next_to(game_screen, RIGHT*0.8 + DOWN*0.5)
        game_button2 = Circle(radius=0.2, color=PINK, fill_opacity=0.8).next_to(game_screen, RIGHT*0.4 + DOWN*0.5)
        icon_gaming = VGroup(game_screen, game_button1, game_button2).next_to(icon_navigation, RIGHT, buff=2)
        gaming_label = Text("Gaming", font_size=36, color=WHITE).next_to(icon_gaming, DOWN)

        impact_group_all = VGroup(icon_construction, construction_label,
                                  icon_navigation, navigation_label,
                                  icon_gaming, gaming_label)

        self.play(Write(impact_text_1), run_time=0.6) # Animation: 0.6s
        self.play(FadeIn(impact_group_all), run_time=0.5) # Animation: 0.5s
        self.wait(2.6)

        self.play(FadeOut(impact_text_1, impact_group_all))

        # --- Scene 7: Summary (4s) ---
        summary_title = Text("Key Takeaways:", font_size=60, color=TEAL_A).to_edge(UP)

        bullet1_text = Text("Right triangles are key.", font_size=40, color=WHITE).next_to(summary_title, DOWN, buff=0.8).align_to(ORIGIN, LEFT).shift(LEFT*2)
        bullet1_dot = Dot(color=PINK).next_to(bullet1_text, LEFT)
        bullet1 = VGroup(bullet1_dot, bullet1_text)

        bullet2_text = Text("a^2 + b^2 = c^2.", font_size=40, color=WHITE).next_to(bullet1_text, DOWN, buff=0.5).align_to(bullet1_text, LEFT)
        bullet2_dot = Dot(color=PINK).next_to(bullet2_text, LEFT)
        bullet2 = VGroup(bullet2_dot, bullet2_text)

        bullet3_text = Text("Finds unknown side lengths.", font_size=40, color=WHITE).next_to(bullet2_text, DOWN, buff=0.5).align_to(bullet2_text, LEFT)
        bullet3_dot = Dot(color=PINK).next_to(bullet3_text, LEFT)
        bullet3 = VGroup(bullet3_dot, bullet3_text)

        self.play(Write(summary_title), run_time=0.6) # Animation: 0.6s
        self.play(FadeIn(bullet1, shift=UP), run_time=0.5) # Animation: 0.5s
        self.play(FadeIn(bullet2, shift=UP), run_time=0.5) # Animation: 0.5s
        self.play(FadeIn(bullet3, shift=UP), run_time=0.5) # Animation: 0.5s
        self.wait(2.6)

        self.play(FadeOut(summary_title, bullet1, bullet2, bullet3))
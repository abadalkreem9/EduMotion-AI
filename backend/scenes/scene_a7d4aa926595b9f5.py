from manim import *

config.pixel_width = 854
config.pixel_height = 480
config.frame_width = 14.22
config.frame_height = 8.0
config.background_color = "#111111"


class MainScene(Scene):
    def construct(self):
        self.camera.background_color = BLACK

        # --- Visual System Colors ---
        primary_color = TEAL_A       # Neon cyan glow
        accent_color = PINK          # Hot pink highlights
        success_color = GREEN        # Correct answers, final state
        text_color = WHITE           # Standard text color
        problem_color = RED_B        # Problem highlights

        # --- Define Triangle Points for a 3-4-5 Triangle ---
        # Centered roughly around the origin for clear visibility
        p1 = ORIGIN + LEFT*2 + DOWN*1.5 # Bottom-left vertex
        p2 = ORIGIN + LEFT*2 + UP*1.5   # Top-left vertex
        p3 = ORIGIN + RIGHT*2 + DOWN*1.5 # Bottom-right vertex

        # --- Helper function to create square points on a diagonal side ---
        def get_square_on_diagonal_points(p_start, p_end, side_length):
            vec_side = p_end - p_start
            unit_vec_side = vec_side / np.linalg.norm(vec_side)
            # Perpendicular vector (rotated 90 degrees counter-clockwise from the line p_start to p_end)
            perp_vec = np.array([-unit_vec_side[1], unit_vec_side[0], 0]) * side_length
            return [p_start, p_end, p_end + perp_vec, p_start + perp_vec]

        # --- Scene 1 (Hook): Bold title + question ---
        title_text = Text("Pythagorean Theorem", font_size=72, weight=BOLD, color=primary_color).to_edge(UP)
        question_text = Text("How does it simplify right triangles?", font_size=36, color=text_color).next_to(title_text, DOWN)
        self.play(
            Write(title_text),
            FadeIn(question_text, shift=DOWN),
            run_time=0.7 # Animation 1/8 (0.7s)
        )
        self.wait(1.3) # Total wait: 1.3s

        # --- Scene 2 (Setup): Real-world context ---
        # Represent wall and ground lines
        ground_line = Line(start=LEFT*4, end=RIGHT*4, color=text_color).shift(DOWN*2)
        wall_line = Line(start=DOWN*2, end=UP*2, color=text_color).shift(LEFT*2)
        wall_label = Text("Wall", font_size=24, color=text_color).next_to(wall_line, LEFT)
        ground_label = Text("Ground", font_size=24, color=text_color).next_to(ground_line, DOWN)
        
        self.play(
            FadeOut(title_text, question_text),
            Create(ground_line),
            Create(wall_line),
            FadeIn(wall_label),
            FadeIn(ground_label),
            run_time=0.7 # Animation 2/8 (0.7s)
        )
        self.wait(1.3) # Total wait: 2.6s

        # --- Scene 3 (Problem): Show the challenge visually ---
        # Introduce the right triangle with 'a', 'b', 'c' labels and right angle
        simple_triangle = Polygon(p1, p2, p3, color=primary_color, fill_opacity=0.2)
        # Right angle indicator (small square)
        right_angle_square = Square(side_length=0.4, color=problem_color, fill_opacity=1).move_to(p1 + RIGHT*0.2 + UP*0.2)

        # Labels for sides 'a', 'b', 'c'
        a_label = Text("a", color=accent_color).next_to(Line(p1, p2), LEFT, buff=0.1)
        b_label = Text("b", color=accent_color).next_to(Line(p1, p3), DOWN, buff=0.1)
        c_label = Text("c", color=primary_color).next_to(Line(p2, p3), UP, buff=0.1).shift(RIGHT*0.2)
        
        self.play(
            FadeOut(ground_line, wall_line, wall_label, ground_label),
            Create(simple_triangle),
            FadeIn(right_angle_square),
            FadeIn(a_label),
            FadeIn(b_label),
            FadeIn(c_label),
            run_time=0.7 # Animation 3/8 (0.7s)
        )
        self.wait(1.3) # Total wait: 3.9s

        # --- Scene 4 (Explanation): Core concept animated in detail ---
        # Create squares on each side of the triangle
        square_a_obj = Polygon(*[p1, p2, p2 + LEFT*3, p1 + LEFT*3], color=accent_color, fill_opacity=0.5) # Side 'a' (length 3)
        square_b_obj = Polygon(*[p1, p3, p3 + DOWN*4, p1 + DOWN*4], color=accent_color, fill_opacity=0.5) # Side 'b' (length 4)
        square_c_obj = Polygon(*get_square_on_diagonal_points(p2, p3, 5), color=primary_color, fill_opacity=0.5) # Side 'c' (length 5)

        self.play(
            FadeOut(simple_triangle, right_angle_square, a_label, b_label, c_label),
            Create(square_a_obj),
            Create(square_b_obj),
            Create(square_c_obj),
            run_time=0.7 # Animation 4/8 (0.7s)
        )
        self.wait(1.3) # Total wait: 5.2s

        # --- Scene 5 (Solution): Step-by-step animated answer ---
        formula_text = Text("a^2 + b^2 = c^2", font_size=48, color=primary_color).move_to(UP*2.5)
        text_explanation = Text("The sum of the smaller areas...", font_size=28, color=text_color).next_to(formula_text, DOWN)
        text_explanation2 = Text("...equals the largest area.", font_size=28, color=text_color).next_to(text_explanation, DOWN)

        self.play(
            Write(formula_text),
            FadeIn(text_explanation),
            FadeIn(text_explanation2),
            run_time=0.7 # Animation 5/8 (0.7s)
        )
        self.play(
            Indicate(square_a_obj, color=accent_color), # Highlight smaller squares
            Indicate(square_b_obj, color=accent_color),
            Indicate(square_c_obj, color=primary_color), # Highlight larger square
            run_time=0.8 # Animation 6/8 (0.8s)
        )
        self.wait(1.3) # Total wait: 6.5s + 1.3s = 7.8s

        # --- Scene 6 (Impact): Why it matters ---
        impact_text1 = Text("Essential for building and design.", font_size=36, color=primary_color).move_to(UP*1)
        impact_text2 = Text("Calculates distances accurately.", font_size=36, color=text_color).next_to(impact_text1, DOWN)
        
        self.play(
            FadeOut(square_a_obj, square_b_obj, square_c_obj, formula_text, text_explanation, text_explanation2),
            FadeIn(impact_text1, shift=UP),
            FadeIn(impact_text2, shift=UP),
            run_time=0.8 # Animation 7/8 (0.8s)
        )
        self.wait(1.3) # Total wait: 7.8s + 1.3s = 9.1s

        # --- Scene 7 (Summary): 3 bullet points animated ---
        bullet1 = Text("1. Only for right triangles.", font_size=32, color=success_color).move_to(UP*1.5 + LEFT*2.5).align_to(LEFT, LEFT)
        bullet2 = Text("2. a^2 + b^2 = c^2 is the rule.", font_size=32, color=success_color).next_to(bullet1, DOWN, align_to=LEFT)
        bullet3 = Text("3. Finds any unknown side.", font_size=32, color=success_color).next_to(bullet2, DOWN, align_to=LEFT)
        
        self.play(
            FadeOut(impact_text1, impact_text2),
            FadeIn(bullet1, shift=RIGHT),
            FadeIn(bullet2, shift=RIGHT),
            FadeIn(bullet3, shift=RIGHT),
            lag_ratio=0.2, # Stagger the bullet points slightly
            run_time=0.8 # Animation 8/8 (0.8s)
        )
        self.wait(1.3) # Total wait: 9.1s + 1.3s = 10.4s

# Total animation run_time: 0.7*5 + 0.8*3 = 3.5 + 2.4 = 5.9 seconds
# Total self.wait() time: 7 * 1.3 = 9.1 seconds
# Total video duration: 5.9 + 9.1 = 15.0 seconds
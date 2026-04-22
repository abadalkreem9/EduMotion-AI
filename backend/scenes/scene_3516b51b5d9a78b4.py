from manim import *

config.pixel_width = 854
config.pixel_height = 480
config.frame_width = 14.22
config.frame_height = 8.0
config.background_color = "#111111"


class MainScene(Scene):
    def construct(self):
        self.camera.background_color = BLACK
        
        # --- SCENE 1: HOOK ---
        title = Text("Unit Circle Waves", color=TEAL_A).scale(1.2)
        question = Text("How do circles create waves?", color=WHITE).scale(0.8).next_to(title, DOWN)
        group1 = VGroup(title, question)
        
        self.play(Write(group1), run_time=0.8)
        self.wait(1.85)
        self.play(FadeOut(group1), run_time=0.5)

        # --- SCENE 2: SETUP ---
        circle = Circle(radius=2.0, color=TEAL_A)
        center_dot = Dot(color=WHITE)
        radius_line = Line(ORIGIN, [2, 0, 0], color=PINK)
        moving_dot = Dot(color=PINK).move_to([2, 0, 0])
        group2 = VGroup(circle, center_dot, radius_line, moving_dot)
        
        self.play(Create(circle), Create(center_dot), run_time=0.8)
        self.play(Create(radius_line), Create(moving_dot), run_time=0.5)
        self.wait(1.85)

        # --- SCENE 3: PROBLEM ---
        # Show X and Y components in RED_B to highlight the "challenge"
        y_line = Line([2, 0, 0], [2, 0, 0], color=RED_B, stroke_width=6)
        x_line = Line(ORIGIN, [2, 0, 0], color=RED_B, stroke_width=6)
        
        # Rotate a bit to show lines
        self.play(
            Rotate(radius_line, angle=PI/3, about_point=ORIGIN),
            moving_dot.animate.move_to([2*0.5, 2*0.866, 0]),
            run_time=0.8
        )
        y_line.set_points_as_corners([[1, 0, 0], [1, 1.732, 0]])
        x_line.set_points_as_corners([[0, 0, 0], [1, 0, 0]])
        self.play(Create(x_line), Create(y_line), run_time=0.5)
        self.wait(1.85)

        # --- SCENE 4: EXPLANATION ---
        label_cos = Text("Horizontal = Cosine", color=WHITE).scale(0.6).to_edge(UP)
        label_sin = Text("Vertical = Sine", color=WHITE).scale(0.6).next_to(label_cos, DOWN)
        
        self.play(Write(label_cos), run_time=0.6)
        self.play(Write(label_sin), run_time=0.6)
        self.wait(1.85)

        # --- SCENE 5: SOLUTION (The Waves) ---
        # Move circle left, draw waves on right
        self.play(
            VGroup(circle, center_dot, radius_line, moving_dot, x_line, y_line).animate.scale(0.5).to_edge(LEFT),
            FadeOut(label_cos), FadeOut(label_sin),
            run_time=0.8
        )
        
        # Setup Axes-like lines for waves
        wave_base_y = Line([0, 1.5, 0], [5, 1.5, 0], color=GRAY)
        wave_base_x = Line([0, -1.5, 0], [5, -1.5, 0], color=GRAY)
        label_y_wave = Text("Sine Wave", color=GREEN).scale(0.5).next_to(wave_base_y, UP)
        label_x_wave = Text("Cosine Wave", color=PINK).scale(0.5).next_to(wave_base_x, UP)
        
        # Simple path tracers using dots
        sine_dot = Dot(color=GREEN).move_to([0, 1.5, 0])
        cosine_dot = Dot(color=PINK).move_to([0, -1.5, 0])
        
        self.play(Create(wave_base_y), Create(wave_base_x), Write(label_y_wave), Write(label_x_wave), run_time=0.8)
        
        # Rotation and Wave movement simulation
        def update_dots(m, dt):
            # This is a hacky way to animate without complex ValueTrackers for speed
            pass

        self.play(
            Rotate(radius_line, angle=2*PI, about_point=radius_line.get_start()),
            moving_dot.animate.shift(UP*0.1), # symbolic movement
            sine_dot.animate.shift(RIGHT*3),
            cosine_dot.animate.shift(RIGHT*3),
            run_time=0.8
        )
        self.wait(1.85)

        # --- SCENE 6: IMPACT ---
        self.play(FadeOut(wave_base_y), FadeOut(wave_base_x), FadeOut(sine_dot), FadeOut(cosine_dot), run_time=0.5)
        impact_text = Text("Powers Radio and Audio", color=GREEN).scale(0.9)
        self.play(Write(impact_text), run_time=0.8)
        self.wait(1.85)
        self.play(FadeOut(impact_text), run_time=0.5)

        # --- SCENE 7: SUMMARY ---
        b1 = Text("1. Rotation equals oscillation", color=WHITE).scale(0.6)
        b2 = Text("2. Cosine tracks horizontal", color=WHITE).scale(0.6).next_to(b1, DOWN)
        b3 = Text("3. Sine tracks vertical", color=WHITE).scale(0.6).next_to(b2, DOWN)
        summary = VGroup(b1, b2, b3).center()
        
        self.play(Write(b1), run_time=0.5)
        self.play(Write(b2), run_time=0.5)
        self.play(Write(b3), run_time=0.5)
        self.wait(1.85)
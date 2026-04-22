from manim import *

config.pixel_width = 854
config.pixel_height = 480
config.frame_width = 14.22
config.frame_height = 8.0
config.background_color = "#1E1E2E"


class MainScene(Scene):
    def construct(self):
        self.camera.background_color = BLACK

        # --- Scene 1 (Hook): Bold title + question ---
        title = Text("Unlocking the Unit Circle", font_size=50, color=TEAL_A, weight=BOLD)
        question = Text("Sine & Cosine: How do they emerge?", font_size=32, color=WHITE).next_to(title, DOWN, buff=0.7)
        
        self.play(
            FadeIn(title, shift=UP),
            Write(question),
            run_time=0.8
        )
        self.wait(1.3)

        # --- Scene 2 (Setup): Real-world context ---
        circle_setup = Circle(radius=1.5, color=TEAL_A).shift(LEFT*3)
        dot_on_circle_start = Dot(circle_setup.point_at_angle(PI/2), color=PINK)
        motion_label = Text("Circular Motion", font_size=28, color=WHITE).next_to(circle_setup, UP)
        
        self.play(
            Create(circle_setup),
            FadeIn(dot_on_circle_start),
            FadeIn(motion_label),
            dot_on_circle_start.animate.move_to(circle_setup.point_at_angle(PI/2 - PI/4)), # Brief initial rotation
            run_time=0.8
        )
        self.wait(1.3)

        # --- Scene 3 (Problem): Show the challenge visually ---
        axes_problem = Axes(
            x_range=[-2, 2, 1], y_range=[-2, 2, 1],
            x_length=3, y_length=3,
            axis_config={"color": GRAY, "stroke_width": 2},
        ).move_to(circle_setup.get_center()) # Align with the circle
        question_mark = Text("?", font_size=60, color=RED_B).move_to(RIGHT*2 + UP*1)
        problem_text = Text("Connecting motion to waves?", font_size=28, color=RED_B).next_to(question_mark, DOWN, buff=0.5)
        
        self.play(
            # Transform circle_setup to itself, just to ensure it's still present
            Transform(dot_on_circle_start, Dot(circle_setup.point_at_angle(PI/2), color=PINK)), # Reset dot position
            Create(axes_problem),
            FadeOut(motion_label),
            FadeIn(question_mark, shift=UP),
            FadeIn(problem_text, shift=DOWN),
            run_time=0.8
        )
        self.wait(1.3)
        
        # --- Scene 4 (Explanation): Core concept animated in detail ---
        # Clear specific elements from previous scenes that won't be reused or are transformed
        self.remove(question_mark, problem_text, dot_on_circle_start)

        unit_circle = Circle(radius=1.5, color=TEAL_A).shift(LEFT*3)
        axes_full = Axes(
            x_range=[-PI, 2*PI, PI/2], y_range=[-1.5, 1.5, 0.5],
            x_length=7, y_length=3,
            axis_config={"color": GRAY, "stroke_width": 2},
            x_axis_config={"numbers_to_include": [0, PI/2, PI, 3*PI/2, 2*PI]},
            y_axis_config={"numbers_to_include": [-1, 0, 1]}
        ).shift(RIGHT*2.5 + UP*0.5)

        x_axis_labels = VGroup(
            Text("0", font_size=20, color=WHITE).next_to(axes_full.c2p(0,0), DOWN),
            Text("π/2", font_size=20, color=WHITE).next_to(axes_full.c2p(PI/2,0), DOWN),
            Text("π", font_size=20, color=WHITE).next_to(axes_full.c2p(PI,0), DOWN),
            Text("3π/2", font_size=20, color=WHITE).next_to(axes_full.c2p(3*PI/2,0), DOWN),
            Text("2π", font_size=20, color=WHITE).next_to(axes_full.c2p(2*PI,0), DOWN)
        )
        y_axis_labels = VGroup(
            Text("1", font_size=20, color=WHITE).next_to(axes_full.c2p(0,1), LEFT),
            Text("-1", font_size=20, color=WHITE).next_to(axes_full.c2p(0,-1), LEFT),
        )

        theta = ValueTracker(0)
        point_on_circle = Dot(color=PINK)
        line_to_point = always_redraw(lambda: Line(unit_circle.get_center(), point_on_circle.get_center(), color=WHITE))
        
        # Projections to the unit circle's x and y axes
        x_proj_line = always_redraw(lambda: Line(point_on_circle.get_center(), unit_circle.get_center() + RIGHT * (point_on_circle.get_center()[0] - unit_circle.get_center()[0]), color=PINK, stroke_width=2, stroke_opacity=0.7))
        y_proj_line = always_redraw(lambda: Line(point_on_circle.get_center(), unit_circle.get_center() + UP * (point_on_circle.get_center()[1] - unit_circle.get_center()[1]), color=TEAL_A, stroke_width=2, stroke_opacity=0.7))
        
        point_on_circle.add_updater(lambda m: m.move_to(unit_circle.get_center() + unit_circle.radius * np.array([np.cos(theta.get_value()), np.sin(theta.get_value()), 0])))

        x_label_expl = Text("x = cos(θ)", font_size=24, color=PINK).next_to(unit_circle.get_center() + RIGHT*1.5 + DOWN*0.5, RIGHT, buff=0.1)
        y_label_expl = Text("y = sin(θ)", font_size=24, color=TEAL_A).next_to(unit_circle.get_center() + UP*1.5 + RIGHT*0.5, UP, buff=0.1)

        self.add(unit_circle, axes_full, x_axis_labels, y_axis_labels) # Add static background elements
        self.play(
            FadeOut(axes_problem, target_mode="animation"), # Fade out previous axes
            # circle_setup is kept, just implicitly becoming the unit_circle
            FadeIn(point_on_circle),
            Create(line_to_point),
            Create(x_proj_line),
            Create(y_proj_line),
            FadeIn(x_label_expl),
            FadeIn(y_label_expl),
            theta.animate.set_value(PI/4), # Show initial angle and projections
            run_time=0.8
        )
        self.wait(1.3)
        
        # --- Scene 5 (Solution): Step-by-step animated answer ---
        sine_graph = always_redraw(
            lambda: axes_full.plot(
                lambda x: np.sin(x),
                x_range=[0, theta.get_value()],
                color=TEAL_A,
                stroke_width=3
            )
        )
        cosine_graph = always_redraw(
            lambda: axes_full.plot(
                lambda x: np.cos(x),
                x_range=[0, theta.get_value()],
                color=PINK,
                stroke_width=3
            )
        )
        
        # Dashed lines projecting from unit circle to graph
        x_proj_line_to_graph = always_redraw(lambda: DashedLine(
            unit_circle.get_center() + RIGHT * (point_on_circle.get_center()[0] - unit_circle.get_center()[0]),
            axes_full.c2p(theta.get_value(), np.cos(theta.get_value())),
            color=PINK, stroke_width=2
        ))
        y_proj_line_to_graph = always_redraw(lambda: DashedLine(
            unit_circle.get_center() + UP * (point_on_circle.get_center()[1] - unit_circle.get_center()[1]),
            axes_full.c2p(theta.get_value(), np.sin(theta.get_value())),
            color=TEAL_A, stroke_width=2
        ))
        
        self.add(sine_graph, cosine_graph, x_proj_line_to_graph, y_proj_line_to_graph)
        self.play(theta.animate.set_value(2*PI), run_time=0.8, rate_func=linear) # Animate one full cycle
        self.wait(1.3)
        
        # Clear updaters for graphs and remove dynamic projection lines/dots
        sine_graph.clear_updaters()
        cosine_graph.clear_updaters()
        self.remove(point_on_circle, line_to_point, x_proj_line, y_proj_line, x_proj_line_to_graph, y_proj_line_to_graph, x_label_expl, y_label_expl)
        
        # --- Scene 6 (Impact): Why it matters ---
        impact_title = Text("Waves are fundamental!", font_size=40, color=GREEN).to_edge(UP)
        impact_text_group = VGroup(
            Text("Model sound, light, electricity.", font_size=28, color=WHITE).shift(UP*0.5),
            Text("Key to engineering & physics.", font_size=28, color=WHITE).shift(DOWN*0.5)
        ).next_to(unit_circle, RIGHT, buff=0.5).shift(RIGHT*1)

        self.play(
            FadeIn(impact_title, shift=UP),
            FadeIn(impact_text_group),
            run_time=0.8
        )
        self.wait(1.3)

        # --- Scene 7 (Summary): 3 bullet points animated ---
        summary_points = VGroup(
            Text("1. Unit circle links angle to (x, y).", font_size=32, color=WHITE),
            Text("2. X-coordinate creates Cosine wave.", font_size=32, color=PINK),
            Text("3. Y-coordinate creates Sine wave.", font_size=32, color=TEAL_A)
        ).arrange(DOWN, center=False, aligned_edge=LEFT, buff=0.4).shift(LEFT*2 + UP*1)

        self.play(
            FadeOut(unit_circle, axes_full, x_axis_labels, y_axis_labels, sine_graph, cosine_graph, impact_title, impact_text_group),
            run_time=0.5 # Quicker fade out to make space
        )
        self.play(
            LaggedStart(
                Write(summary_points[0]),
                Write(summary_points[1]),
                Write(summary_points[2]),
                lag_ratio=0.5,
                run_time=0.6 # Total animation for lagged start
            )
        )
        self.wait(1.3)
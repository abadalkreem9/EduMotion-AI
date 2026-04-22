from manim import *

config.pixel_width = 854
config.pixel_height = 480
config.frame_width = 14.22
config.frame_height = 8.0
config.background_color = "#111111"


class MainScene(Scene):
    def construct(self):
        self.camera.background_color = BLACK

        # --- Scene 1 (Hook): Bold title + question (Animation: 1.0s, Wait: 1.7s) ---
        title = Text("The Unit Circle's Secret", font_size=60, weight=BOLD, color=TEAL_A)
        question = Text("How do waves emerge?", font_size=36, color=WHITE).next_to(title, DOWN, buff=0.8)
        
        self.play(Write(title), run_time=0.5)
        self.play(Write(question), run_time=0.5)
        self.wait(1.7) 

        # --- Scene 2 (Setup): Real-world context (Animation: 1.0s, Wait: 1.7s) ---
        unit_circle = Circle(radius=2, color=TEAL_A)
        center_dot = Dot(point=ORIGIN, color=PINK)
        radius_line = Line(ORIGIN, 2*RIGHT, color=PINK)
        radius_label = Text("Radius = 1", font_size=24, color=WHITE).next_to(radius_line, UP, buff=0.1)
        
        self.play(FadeOut(VGroup(title, question)), Create(unit_circle), Create(center_dot), run_time=0.5)
        self.play(Create(radius_line), Write(radius_label), run_time=0.5)
        self.wait(1.7) 

        # --- Scene 3 (Problem): Show the challenge visually (Animation: 1.0s, Wait: 1.7s) ---
        x_axis = NumberLine(x_range=[-2.5, 2.5, 1], length=5, color=LIGHT_GRAY, include_numbers=False).shift(unit_circle.get_center())
        y_axis = NumberLine(x_range=[-2.5, 2.5, 1], length=5, color=LIGHT_GRAY, include_numbers=False).rotate(PI/2, about_point=ORIGIN).shift(unit_circle.get_center())
        
        point_on_circle = Dot(point=2*RIGHT, color=GREEN) # Initial position (radius 2)
        proj_x_line = always_redraw(lambda: Line(point_on_circle.get_center()[0]*RIGHT, point_on_circle.get_center(), color=RED_B))
        proj_y_line = always_redraw(lambda: Line(point_on_circle.get_center()[1]*UP, point_on_circle.get_center(), color=RED_B))

        angle_tracker = ValueTracker(0) 
        def update_point_on_circle(mobj):
            angle = angle_tracker.get_value()
            mobj.move_to(unit_circle.point_at_angle(angle))
        point_on_circle.add_updater(update_point_on_circle) # Add updater here

        self.play(FadeOut(radius_label), Create(x_axis), Create(y_axis), run_time=0.5)
        self.add(point_on_circle, proj_x_line, proj_y_line) # Add directly, animation is the movement
        self.play(angle_tracker.animate.set_value(PI * 1.5), run_time=0.5) # Sweep through most of circle to show changing coords
        self.wait(1.7) 

        # --- Scene 4 (Explanation): Core concept animated in detail (Animation: 1.0s, Wait: 1.7s) ---
        self.remove(proj_x_line, proj_y_line) # Remove old updaters
        
        origin_to_point_line = always_redraw(lambda: Line(ORIGIN, point_on_circle.get_center(), color=PINK))
        angle_arc = always_redraw(lambda: AnnularSector(inner_radius=0, outer_radius=0.5, angle=angle_tracker.get_value(), color=TEAL_A, fill_opacity=0.5, arc_center=ORIGIN))
        
        cos_label = always_redraw(lambda: Text("Cos(θ) = X", font_size=24, color=TEAL_A).next_to(unit_circle, UP+RIGHT, buff=0.8).shift(RIGHT*1.5))
        sin_label = always_redraw(lambda: Text("Sin(θ) = Y", font_size=24, color=TEAL_A).next_to(unit_circle, DOWN+RIGHT, buff=0.8).shift(RIGHT*1.5))
        
        x_coord_line = always_redraw(lambda: Line(ORIGIN, point_on_circle.get_center()[0]*RIGHT, color=GREEN))
        y_coord_line = always_redraw(lambda: Line(ORIGIN, point_on_circle.get_center()[1]*UP, color=GREEN))
        
        self.play(Create(origin_to_point_line), Create(angle_arc), run_time=0.5)
        self.play(Create(x_coord_line), Create(y_coord_line), Write(cos_label), Write(sin_label), run_time=0.5)
        self.wait(1.7) 

        # --- Scene 5 (Solution): Step-by-step animated answer (Animation: 1.8s, Wait: 1.7s) ---
        self.remove(point_on_circle, origin_to_point_line, angle_arc, x_coord_line, y_coord_line) # Remove from scene, updaters will stop.
        point_on_circle.remove_updater(update_point_on_circle) # Explicitly remove updater for point_on_circle
        
        sine_graph_axis = NumberLine(x_range=[0, 2*PI, PI/2], length=6, color=LIGHT_GRAY, label_direction=DOWN)
        sine_graph_axis.shift(4*RIGHT + 1.5*DOWN)
        
        cosine_graph_axis = NumberLine(x_range=[0, 2*PI, PI/2], length=6, color=LIGHT_GRAY, label_direction=DOWN)
        cosine_graph_axis.shift(4*RIGHT + 1.5*UP)

        sine_label_text = Text("Sine Wave (Y)", font_size=24, color=TEAL_A).next_to(sine_graph_axis, DOWN, buff=0.5)
        cosine_label_text = Text("Cosine Wave (X)", font_size=24, color=TEAL_A).next_to(cosine_graph_axis, UP, buff=0.5)
        
        self.play(FadeOut(VGroup(unit_circle, center_dot, x_axis, y_axis, cos_label, sin_label)), run_time=0.5)

        # Re-create relevant parts for clear animation with new context
        unit_circle_new = Circle(radius=1.5, color=TEAL_A).move_to(3*LEFT) # Smaller, to the left
        center_dot_new = Dot(point=3*LEFT, color=PINK)
        point_on_circle_new = Dot(point=unit_circle_new.point_at_angle(0), color=GREEN) # Initial pos
        
        angle_tracker.set_value(0) # Reset angle for new animation
        
        self.play(Create(unit_circle_new), Create(center_dot_new),
                  Create(sine_graph_axis), Create(cosine_graph_axis),
                  Write(sine_label_text), Write(cosine_label_text), run_time=0.5)

        # Point for sine wave projection
        sine_dot = Dot(color=PINK)
        cosine_dot = Dot(color=PINK)
        
        sine_path = VMobject(color=TEAL_A)
        cosine_path = VMobject(color=TEAL_A)

        # Set initial positions for dots to prevent a jump for the first segment
        sine_dot.move_to(np.array([sine_graph_axis.point_from_proportion(0)[0], sine_graph_axis.get_y() + np.sin(0) * 1.5, 0]))
        cosine_dot.move_to(np.array([cosine_graph_axis.point_from_proportion(0)[0], cosine_graph_axis.get_y() + np.cos(0) * 1.5, 0]))

        sine_path.set_points_as_corners([sine_dot.get_center(), sine_dot.get_center()])
        cosine_path.set_points_as_corners([cosine_dot.get_center(), cosine_dot.get_center()])

        sine_path.add_updater(lambda mobj: mobj.add_points_as_corners([mobj.get_last_point(), sine_dot.get_center()]))
        cosine_path.add_updater(lambda mobj: mobj.add_points_as_corners([mobj.get_last_point(), cosine_dot.get_center()]))
        
        self.add(sine_path, cosine_path, point_on_circle_new, sine_dot, cosine_dot)

        self.play(
            angle_tracker.animate(run_time=0.8, rate_func=rate_functions.LINEAR).set_value(2 * PI),
            UpdateFromFunc(point_on_circle_new, 
                           lambda mobj: mobj.move_to(unit_circle_new.point_at_angle(angle_tracker.get_value()))),
            UpdateFromFunc(sine_dot,
                           lambda mobj: mobj.move_to(np.array([sine_graph_axis.point_from_proportion(angle_tracker.get_value() / (2 * PI))[0], 
                                                               sine_graph_axis.get_y() + np.sin(angle_tracker.get_value()) * 1.5, 0]))),
            UpdateFromFunc(cosine_dot,
                           lambda mobj: mobj.move_to(np.array([cosine_graph_axis.point_from_proportion(angle_tracker.get_value() / (2 * PI))[0], 
                                                               cosine_graph_axis.get_y() + np.cos(angle_tracker.get_value()) * 1.5, 0]))),
        )
        self.wait(1.7) 
        
        # --- Scene 6 (Impact): Why it matters (Animation: 1.0s, Wait: 1.7s) ---
        self.remove(point_on_circle_new, sine_dot, cosine_dot) # Remove updaters after animation
        sine_path.clear_updaters()
        cosine_path.clear_updaters()
        
        def get_graph_from_line(func, number_line, amplitude=1.5):
            graph = FunctionGraph(lambda t: func(t) * amplitude, x_range=[0, 2*PI], color=TEAL_A)
            graph.stretch_to_fit_width(number_line.get_length())
            graph.align_to(number_line, LEFT)
            graph.shift(number_line.get_y()*UP - graph.get_y()*UP)
            return graph
            
        final_sine_wave_obj = get_graph_from_line(np.sin, sine_graph_axis)
        final_cosine_wave_obj = get_graph_from_line(np.cos, cosine_graph_axis)

        self.play(FadeOut(sine_path, cosine_path, unit_circle_new, center_dot_new),
                  Create(final_sine_wave_obj), Create(final_cosine_wave_obj), run_time=0.5)
        impact_text = Text("These waves describe light, sound, and more.", font_size=32, color=WHITE).to_edge(UP)
        self.play(Write(impact_text), run_time=0.5)
        self.wait(1.7) 

        # --- Scene 7 (Summary): 3 bullet points animated (Animation: 1.3s, Wait: 1.7s) ---
        self.play(FadeOut(VGroup(sine_graph_axis, cosine_graph_axis, sine_label_text, cosine_label_text, final_sine_wave_obj, final_cosine_wave_obj, impact_text)), run_time=0.5)

        bullet1 = Text("1. Unit Circle: The wave generator.", font_size=36, color=WHITE).shift(UP * 1.5)
        bullet2 = Text("2. Sine is Y, Cosine is X.", font_size=36, color=WHITE).next_to(bullet1, DOWN, buff=0.8)
        bullet3 = Text("3. Waves are everywhere!", font_size=36, color=WHITE).next_to(bullet2, DOWN, buff=0.8)
        
        bullets = VGroup(bullet1, bullet2, bullet3).center()

        self.play(Write(bullet1), run_time=0.5)
        self.play(Write(bullet2), run_time=0.5)
        self.play(Write(bullet3), run_time=0.3) 
        self.wait(1.7)
from manim import *

config.pixel_width = 854
config.pixel_height = 480
config.frame_width = 14.22
config.frame_height = 8.0
config.background_color = "#1E1E2E"


class MainScene(Scene):
    def construct(self):
        self.camera.background_color = BLACK

        # --- Scene 1: Hook ---
        title = Text("The Salesman's Puzzle", color=TEAL_A, font_size=48)
        question = Text("How to find the best route?", color=PINK, font_size=36).next_to(title, DOWN)
        self.play(Write(title), run_time=0.7)
        self.play(FadeIn(question, shift=UP), run_time=0.7)
        self.wait(2.6)
        self.play(FadeOut(title), FadeOut(question))

        # --- Scene 2: Setup ---
        cities = VGroup(
            Dot(point=[-2, 1, 0], color=WHITE),
            Dot(point=[2, 2, 0], color=WHITE),
            Dot(point=[1, -2, 0], color=WHITE),
            Dot(point=[-1, -1, 0], color=WHITE),
            Dot(point=[0, 1.5, 0], color=WHITE)
        )
        labels = VGroup(*[Text(f"City {i}", font_size=20).next_to(cities[i], UP) for i in range(5)])
        initial_path = VGroup(
            Arrow(cities[0], cities[1], color=PINK, buff=0.1),
            Arrow(cities[1], cities[2], color=PINK, buff=0.1),
            Arrow(cities[2], cities[3], color=PINK, buff=0.1),
            Arrow(cities[3], cities[4], color=PINK, buff=0.1)
        )
        self.play(Create(cities), Write(labels), run_time=0.8)
        self.play(Create(initial_path), run_time=0.8)
        self.wait(2.6)

        # --- Scene 3: Problem ---
        complex_lines = VGroup()
        for i in range(5):
            for j in range(i+1, 5):
                complex_lines.add(Line(cities[i], cities[j], color=RED_B, stroke_opacity=0.3))
        
        problem_text = Text("Factorial Complexity!", color=RED_B).to_edge(UP)
        self.play(FadeIn(complex_lines), Write(problem_text), run_time=0.8)
        self.play(problem_text.animate.scale(1.2), run_time=0.6)
        self.wait(2.6)
        self.play(FadeOut(complex_lines), FadeOut(problem_text), FadeOut(initial_path))

        # --- Scene 4: Explanation ---
        tabu_box = Rectangle(width=4, height=2, color=TEAL_A).to_edge(RIGHT)
        tabu_label = Text("Tabu List", color=TEAL_A, font_size=24).next_to(tabu_box, UP)
        forbidden_move = Text("Edge 1-2 Forbidden", color=RED_B, font_size=20).move_to(tabu_box.get_center())
        
        bad_arrow = Arrow(cities[1], cities[2], color=RED_B, buff=0.1)
        self.play(Create(tabu_box), Write(tabu_label), run_time=0.7)
        self.play(Create(bad_arrow), Write(forbidden_move), run_time=0.7)
        self.wait(2.6)

        # --- Scene 5: Solution ---
        best_path = VGroup(
            Arrow(cities[0], cities[4], color=GREEN, buff=0.1),
            Arrow(cities[4], cities[1], color=GREEN, buff=0.1),
            Arrow(cities[1], cities[2], color=GREEN, buff=0.1),
            Arrow(cities[2], cities[3], color=GREEN, buff=0.1),
            Arrow(cities[3], cities[0], color=GREEN, buff=0.1)
        )
        found_text = Text("Shortest Path Found", color=GREEN).to_edge(DOWN)
        self.play(FadeOut(bad_arrow), FadeOut(tabu_box), FadeOut(tabu_label), FadeOut(forbidden_move), run_time=0.5)
        self.play(Create(best_path), Write(found_text), run_time=0.8)
        self.wait(2.6)

        # --- Scene 6: Impact ---
        impact_text = Text("Optimized Logistics", color=TEAL_A).to_edge(UP)
        benefit = Text("Saves Fuel and Time", color=PINK, font_size=32).next_to(impact_text, DOWN)
        self.play(FadeOut(found_text), Write(impact_text), run_time=0.7)
        self.play(FadeIn(benefit, shift=DOWN), run_time=0.7)
        self.wait(2.6)
        self.play(FadeOut(impact_text), FadeOut(benefit), FadeOut(best_path), FadeOut(cities), FadeOut(labels))

        # --- Scene 7: Summary ---
        summary_title = Text("Tabu Search Key Points", color=TEAL_A, font_size=36).to_edge(UP)
        b1 = Text("1. Uses Memory to avoid loops", font_size=28).shift(UP*0.5)
        b2 = Text("2. Explores new search areas", font_size=28).next_to(b1, DOWN)
        b3 = Text("3. Solves complex routing fast", font_size=28).next_to(b2, DOWN)
        
        self.play(Write(summary_title), run_time=0.6)
        self.play(Write(VGroup(b1, b2, b3)), run_time=0.8)
        self.wait(2.6)
from manim import *

config.pixel_width = 854
config.pixel_height = 480
config.frame_width = 14.22
config.frame_height = 8.0
config.background_color = "#1E1E2E"


class MainScene(Scene):
    def construct(self):
        # Set background
        self.camera.background_color = BLACK

        # Scene 1: Hook
        title = Text("Solving the TSP", color=TEAL_A).scale(1.2)
        subtitle = Text("With Tabu Search", color=PINK).next_to(title, DOWN)
        self.play(Write(title, run_time=0.8))
        self.play(FadeIn(subtitle, run_time=0.8))
        self.wait(2.6)
        self.play(FadeOut(title), FadeOut(subtitle), run_time=0.5)

        # Scene 2: Setup
        city_dots = VGroup(
            Dot(UP*2 + LEFT*2, color=TEAL_A),
            Dot(UP*1.5 + RIGHT*2, color=TEAL_A),
            Dot(DOWN*0.5 + RIGHT*3, color=TEAL_A),
            Dot(DOWN*2 + LEFT*1, color=TEAL_A),
            Dot(ORIGIN, color=TEAL_A)
        )
        labels = Text("Cities to Visit", color=WHITE).scale(0.8).to_edge(UP)
        self.play(Create(city_dots, run_time=0.9))
        self.play(Write(labels, run_time=0.8))
        self.wait(2.6)

        # Scene 3: Problem
        messy_paths = VGroup(
            Arrow(city_dots[0].get_center(), city_dots[2].get_center(), color=PINK, buff=0.1),
            Arrow(city_dots[2].get_center(), city_dots[4].get_center(), color=PINK, buff=0.1),
            Arrow(city_dots[4].get_center(), city_dots[1].get_center(), color=PINK, buff=0.1),
            Arrow(city_dots[1].get_center(), city_dots[3].get_center(), color=PINK, buff=0.1),
            Arrow(city_dots[3].get_center(), city_dots[0].get_center(), color=PINK, buff=0.1)
        )
        problem_text = Text("Too many combinations!", color=RED_B).scale(0.7).to_edge(DOWN)
        self.play(Create(messy_paths, run_time=0.9))
        self.play(Write(problem_text, run_time=0.8))
        self.wait(2.6)
        self.play(FadeOut(messy_paths), FadeOut(problem_text), run_time=0.5)

        # Scene 4: Explanation (Tabu List)
        tabu_box = Rectangle(width=4, height=2, color=WHITE).to_edge(RIGHT)
        tabu_title = Text("Tabu List", color=WHITE).scale(0.6).next_to(tabu_box, UP)
        tabu_entry = Text("Path A -> C: BLOCKED", color=RED_B).scale(0.4).move_to(tabu_box.get_center())
        blocked_arrow = Arrow(city_dots[0].get_center(), city_dots[2].get_center(), color=RED_B, buff=0.1)
        
        self.play(Create(tabu_box), Write(tabu_title), run_time=0.8)
        self.play(Create(blocked_arrow), Write(tabu_entry), run_time=0.9)
        self.wait(2.6)

        # Scene 5: Solution
        optimal_paths = VGroup(
            Arrow(city_dots[0].get_center(), city_dots[1].get_center(), color=GREEN, buff=0.1),
            Arrow(city_dots[1].get_center(), city_dots[2].get_center(), color=GREEN, buff=0.1),
            Arrow(city_dots[2].get_center(), city_dots[4].get_center(), color=GREEN, buff=0.1),
            Arrow(city_dots[4].get_center(), city_dots[3].get_center(), color=GREEN, buff=0.1),
            Arrow(city_dots[3].get_center(), city_dots[0].get_center(), color=GREEN, buff=0.1)
        )
        sol_text = Text("Global Minimum Found", color=GREEN).scale(0.7).to_edge(DOWN)
        self.play(FadeOut(blocked_arrow), FadeOut(tabu_entry), run_time=0.5)
        self.play(Create(optimal_paths), Write(sol_text), run_time=1.2)
        self.wait(2.6)

        # Scene 6: Impact
        self.play(FadeOut(city_dots), FadeOut(optimal_paths), FadeOut(tabu_box), FadeOut(tabu_title), FadeOut(sol_text), run_time=0.5)
        impact_title = Text("Real-World Impact", color=TEAL_A).scale(1.1)
        impact_desc = Text("Faster Logistics & Lower Costs", color=PINK).scale(0.7).next_to(impact_title, DOWN)
        self.play(Write(impact_title, run_time=0.8))
        self.play(FadeIn(impact_desc, run_time=0.8))
        self.wait(2.6)
        self.play(FadeOut(impact_title), FadeOut(impact_desc), run_time=0.5)

        # Scene 7: Summary
        b1 = Text("1. Memory blocks loops", color=WHITE).scale(0.6).shift(UP*1)
        b2 = Text("2. Explores better space", color=WHITE).scale(0.6)
        b3 = Text("3. High speed efficiency", color=WHITE).scale(0.6).shift(DOWN*1)
        
        self.play(Write(b1, run_time=0.6))
        self.play(Write(b2, run_time=0.6))
        self.play(Write(b3, run_time=0.6))
        self.wait(2.6)
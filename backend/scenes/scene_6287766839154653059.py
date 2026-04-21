from manim import *

config.pixel_width = 854
config.pixel_height = 480
config.frame_width = 14.22
config.frame_height = 8.0
config.background_color = "#1E1E2E"


class MainScene(Scene):
    def construct(self):
        # Set background color
        self.camera.background_color = BLACK

        # Scene 1: Hook - Title and Question
        title = Text("The Traveling Salesman", color=TEAL_A).scale(1.2)
        question = Text("Finding the shortest path?", color=WHITE).scale(0.8).next_to(title, DOWN)
        
        self.play(Write(title), run_time=0.8)
        self.play(FadeIn(question), run_time=0.8)
        self.wait(2.6)
        self.play(FadeOut(title), FadeOut(question))

        # Scene 2: Setup - Real-world context (Cities)
        c1 = Dot(point=[-3, 2, 0], color=TEAL_A)
        c2 = Dot(point=[3, 1, 0], color=TEAL_A)
        c3 = Dot(point=[2, -2, 0], color=TEAL_A)
        c4 = Dot(point=[-2, -2, 0], color=TEAL_A)
        c5 = Dot(point=[0, 0, 0], color=TEAL_A)
        cities = VGroup(c1, c2, c3, c4, c5)
        labels = VGroup(
            Text("A").next_to(c1, UP), Text("B").next_to(c2, UP),
            Text("C").next_to(c3, DOWN), Text("D").next_to(c4, DOWN),
            Text("E").next_to(c5, RIGHT)
        ).scale(0.6)
        
        self.play(Create(cities), run_time=0.8)
        self.play(Write(labels), run_time=0.8)
        self.wait(2.6)

        # Scene 3: Problem - Complexity
        bad_path1 = Arrow(c1.get_center(), c3.get_center(), color=RED_B)
        bad_path2 = Arrow(c3.get_center(), c2.get_center(), color=RED_B)
        bad_path3 = Arrow(c2.get_center(), c4.get_center(), color=RED_B)
        bad_paths = VGroup(bad_path1, bad_path2, bad_path3)
        
        warning = Text("Too many combinations!", color=RED_B).to_edge(UP)
        self.play(Create(bad_paths), run_time=0.8)
        self.play(Write(warning), run_time=0.8)
        self.wait(2.6)
        self.play(FadeOut(bad_paths), FadeOut(warning))

        # Scene 4: Explanation - Tabu List
        tabu_box = Rectangle(width=4, height=2, color=PINK).to_edge(RIGHT)
        tabu_title = Text("Tabu List", color=PINK).scale(0.7).next_to(tabu_box, UP)
        tabu_item = Text("Route A -> C", color=WHITE).scale(0.5).move_to(tabu_box.get_center())
        
        cross_line1 = Line(c1.get_center(), c3.get_center(), color=PINK)
        cross_line2 = Line(c1.get_center() + [0.1, 0, 0], c3.get_center() + [0.1, 0, 0], color=PINK)
        blocked_route = VGroup(cross_line1, cross_line2)

        self.play(Create(tabu_box), Write(tabu_title), run_time=0.8)
        self.play(Write(tabu_item), Create(blocked_route), run_time=0.8)
        self.wait(2.6)

        # Scene 5: Solution - Step-by-step optimization
        path1 = Arrow(c1.get_center(), c2.get_center(), color=GREEN)
        path2 = Arrow(c2.get_center(), c3.get_center(), color=GREEN)
        
        self.play(Create(path1), run_time=0.8)
        self.play(Create(path2), run_time=0.8)
        self.wait(2.6)

        # Scene 6: Impact - Shortest Path Found
        path3 = Arrow(c3.get_center(), c4.get_center(), color=GREEN)
        path4 = Arrow(c4.get_center(), c5.get_center(), color=GREEN)
        path5 = Arrow(c5.get_center(), c1.get_center(), color=GREEN)
        full_path = VGroup(path1, path2, path3, path4, path5)
        
        success_msg = Text("Optimal Route Found!", color=GREEN).to_edge(UP)
        self.play(Create(path3), Create(path4), Create(path5), run_time=0.8)
        self.play(full_path.animate.set_stroke(width=8), Write(success_msg), run_time=0.8)
        self.wait(2.6)
        self.play(FadeOut(full_path), FadeOut(success_msg), FadeOut(tabu_box), FadeOut(tabu_title), FadeOut(tabu_item), FadeOut(blocked_route))

        # Scene 7: Summary
        sum1 = Text("1. Block repeat routes", color=WHITE).scale(0.7).shift(UP*1)
        sum2 = Text("2. Escape local traps", color=WHITE).scale(0.7)
        sum3 = Text("3. Optimize everything", color=WHITE).scale(0.7).shift(DOWN*1)
        
        summary_group = VGroup(sum1, sum2, sum3)
        self.play(Write(sum1), run_time=0.8)
        self.play(Write(VGroup(sum2, sum3)), run_time=0.8)
        self.wait(2.6)
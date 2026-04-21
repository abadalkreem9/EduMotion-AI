from manim import *

config.pixel_width = 480
config.pixel_height = 854
config.frame_width = 8.0
config.frame_height = 14.22
config.background_color = "#000000"


class MainScene(Scene):
    def construct(self):
        # Configuration
        self.camera.background_color = BLACK
        primary_color = TEAL_A
        accent_color = PINK
        success_color = GREEN
        text_color = WHITE
        
        # 1. Intro
        title = Text("Bubble Sort", color=primary_color).scale(1.2)
        subtitle = Text("Ordering Numbers", color=text_color).scale(0.6).next_to(title, DOWN)
        intro_grp = VGroup(title, subtitle).to_edge(UP, buff=1.0)
        
        self.play(FadeIn(intro_grp), run_time=0.5)
        self.wait(0.5)

        # Create List of Numbers
        numbers = [5, 2, 8, 3, 1]
        nodes = VGroup()
        for i, num in enumerate(numbers):
            box = Square(side_length=1.2, color=primary_color)
            val = Text(str(num), color=text_color)
            node = VGroup(box, val)
            node.shift(RIGHT * (i - 2) * 1.4 + DOWN * 1)
            nodes.add(node)
        
        self.play(Create(nodes), run_time=0.8)
        self.wait(0.5)

        # 2. Compare first pair (5, 2)
        highlight = Rectangle(width=2.8, height=1.5, color=accent_color, stroke_width=6)
        highlight.move_to(VGroup(nodes[0], nodes[1]).get_center())
        
        step_text = Text("Compare adjacent", color=accent_color).scale(0.7).to_edge(DOWN, buff=1.5)
        self.play(FadeIn(highlight), FadeIn(step_text), run_time=0.5)
        self.wait(0.5)

        # 3. Swap (5 > 2)
        swap_text = Text("5 > 2 : Swap!", color=accent_color).scale(0.7).to_edge(DOWN, buff=1.5)
        self.play(Transform(step_text, swap_text), run_time=0.3)
        
        self.play(
            nodes[0].animate.move_to(nodes[1].get_center()),
            nodes[1].animate.move_to(nodes[0].get_center()),
            run_time=0.5
        )
        # Update indexing in our list for logic
        nodes[0], nodes[1] = nodes[1], nodes[0]
        self.wait(0.5)

        # 4. Move to next pair (5, 8)
        self.play(highlight.animate.move_to(VGroup(nodes[1], nodes[2]).get_center()), run_time=0.4)
        move_text = Text("Move to next pair", color=text_color).scale(0.7).to_edge(DOWN, buff=1.5)
        self.play(Transform(step_text, move_text), run_time=0.3)
        self.wait(0.5)

        # 5. Bubble 8 to the end
        # Compare 5 and 8 (No swap)
        self.play(Indicate(nodes[2][0], color=GREEN_A), run_time=0.4)
        
        # Compare 8 and 3
        self.play(highlight.animate.move_to(VGroup(nodes[2], nodes[3]).get_center()), run_time=0.4)
        self.play(
            nodes[2].animate.move_to(nodes[3].get_center()),
            nodes[3].animate.move_to(nodes[2].get_center()),
            run_time=0.4
        )
        nodes[2], nodes[3] = nodes[3], nodes[2]
        
        # Compare 8 and 1
        self.play(highlight.animate.move_to(VGroup(nodes[3], nodes[4]).get_center()), run_time=0.4)
        self.play(
            nodes[3].animate.move_to(nodes[4].get_center()),
            nodes[4].animate.move_to(nodes[3].get_center()),
            run_time=0.4
        )
        nodes[3], nodes[4] = nodes[4], nodes[3]
        
        bubble_text = Text("8 Bubbled to the end!", color=success_color).scale(0.7).to_edge(DOWN, buff=1.5)
        self.play(Transform(step_text, bubble_text), nodes[4][0].animate.set_color(success_color), run_time=0.5)
        self.play(FadeOut(highlight), run_time=0.3)
        self.wait(0.5)

        # 6. Repeat (Simulate fast)
        repeat_text = Text("Repeat for remaining...", color=primary_color).scale(0.7).to_edge(DOWN, buff=1.5)
        self.play(Transform(step_text, repeat_text), run_time=0.5)
        
        # Fast sort visual (mocking the rest)
        # Current: [2, 5, 3, 1, 8]
        # Sort 2, 5, 3, 1
        self.play(
            nodes[1].animate.move_to(nodes[2].get_center()), # 5 moves to 3rd pos
            nodes[2].animate.move_to(nodes[1].get_center()), # 3 moves to 2nd pos
            run_time=0.3
        )
        nodes[1], nodes[2] = nodes[2], nodes[1] # [2, 3, 5, 1, 8]
        
        self.play(
            nodes[2].animate.move_to(nodes[3].get_center()), # 5 moves to 4th pos
            nodes[3].animate.move_to(nodes[2].get_center()), # 1 moves to 3rd pos
            run_time=0.3
        )
        nodes[2], nodes[3] = nodes[3], nodes[2] # [2, 3, 1, 5, 8]
        self.play(nodes[3][0].animate.set_color(success_color), run_time=0.2)

        # Final pass
        self.play(
            nodes[1].animate.move_to(nodes[2].get_center()), # 3 moves to 3rd pos
            nodes[2].animate.move_to(nodes[1].get_center()), # 1 moves to 2nd pos
            run_time=0.3
        )
        nodes[1], nodes[2] = nodes[2], nodes[1] # [2, 1, 3, 5, 8]
        
        self.play(
            nodes[0].animate.move_to(nodes[1].get_center()), # 2 moves to 2nd pos
            nodes[1].animate.move_to(nodes[0].get_center()), # 1 moves to 1st pos
            run_time=0.3
        )
        nodes[0], nodes[1] = nodes[1], nodes[0] # [1, 2, 3, 5, 8]
        
        # 7. Success
        all_done = Text("List Sorted!", color=success_color).scale(1.1).to_edge(DOWN, buff=1.5)
        self.play(Transform(step_text, all_done), run_time=0.5)
        
        self.play(
            *[n[0].animate.set_color(success_color) for n in nodes],
            *[Indicate(n[1], color=WHITE) for n in nodes],
            run_time=0.8
        )
        
        checkmark = VGroup(
            Line(LEFT*0.3 + DOWN*0.2, ORIGIN, color=success_color, stroke_width=8),
            Line(ORIGIN, RIGHT*0.6 + UP*0.5, color=success_color, stroke_width=8)
        ).next_to(all_done, UP)
        
        self.play(Create(checkmark), run_time=0.5)
        self.wait(1.5)

        # Cleanup
        self.play(FadeOut(nodes), FadeOut(intro_grp), FadeOut(step_text), FadeOut(checkmark), run_time=0.5)
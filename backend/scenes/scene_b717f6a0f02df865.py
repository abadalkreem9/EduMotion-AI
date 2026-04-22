from manim import *

config.pixel_width = 854
config.pixel_height = 480
config.frame_width = 14.22
config.frame_height = 8.0
config.background_color = "#1E1E2E"


class MainScene(Scene):
    def construct(self):
        self.camera.background_color = BLACK

        # Helper function to create a bar group (rectangle + number)
        def create_bar_group(value, x_pos, max_height=3.0, bar_color=TEAL_A, text_color=WHITE):
            height = value / 5 * max_height # Scale value (1-5) to height
            bar = Rectangle(width=0.7, height=height, fill_opacity=0.8, stroke_width=2, stroke_color=bar_color)
            bar.set_color(bar_color)
            bar.move_to(x_pos * RIGHT + (height/2 - max_height/2) * UP)
            number = Text(str(value), font_size=24, color=text_color).next_to(bar, UP, buff=0.1)
            return VGroup(bar, number)

        # SCENE 1 (Hook): Bold title + question — ~0.8s anim
        title = Text("Bubble Sort Explained", font_size=60, weight=BOLD, color=TEAL_A)
        question = Text("How do we sort data efficiently?", font_size=36, color=WHITE).next_to(title, DOWN, buff=0.8)
        self.play(FadeIn(title), FadeIn(question), lag_ratio=0.1, run_time=0.8)
        self.wait(1.3)

        # Setup initial bars for the algorithm
        initial_values = [4, 2, 5, 1, 3]
        max_bar_height = 3.0
        x_offset = -4.0 # Starting x position for the first bar
        bars = VGroup()
        for i, val in enumerate(initial_values):
            bar_group = create_bar_group(val, x_offset + i * 1.5, max_height=max_bar_height)
            bars.add(bar_group)
        bars.center() # Center the entire VGroup of bars

        # SCENE 2 (Setup): Real-world context — ~0.8s anim
        self.play(
            FadeOut(title, question), # Fade out previous scene's elements
            LaggedStart(*[FadeIn(bar) for bar in bars], lag_ratio=0.05, run_time=0.8) # Fade in bars
        )
        self.wait(1.3)

        # SCENE 3 (Problem): Show the challenge visually — ~0.7s anim
        problem_text = Text("Unsorted Data!", color=RED_B, font_size=48).to_edge(UP)
        problem_arrow = Arrow(problem_text.get_bottom(), bars.get_top(), buff=0.2, color=RED_B)
        self.play(FadeIn(problem_text), GrowArrow(problem_arrow), run_time=0.7)
        self.wait(1.3)

        # SCENE 4 (Explanation): Core concept animated in detail — ~0.8s anim
        explanation_text_1 = Text("Compare adjacent elements.", color=WHITE, font_size=32).to_edge(UP)
        explanation_text_2 = Text("Swap if wrong order.", color=WHITE, font_size=32).next_to(explanation_text_1, DOWN, buff=0.3)
        explanation_group = VGroup(explanation_text_1, explanation_text_2)

        # Highlight first two bars for comparison (bars are [4, 2, 5, 1, 3])
        bar_rect_0 = bars[0][0] # Rectangle of the first bar group (value 4)
        bar_rect_1 = bars[1][0] # Rectangle of the second bar group (value 2)

        self.play(
            FadeOut(problem_text, problem_arrow), # Fade out previous scene's elements
            FadeIn(explanation_group), # Fade in explanation text
            bar_rect_0.animate.set_color(PINK),
            bar_rect_1.animate.set_color(PINK),
            run_time=0.8 # Total for this play call
        )
        self.wait(1.3)

        # SCENE 5 (Solution): Step-by-step animated answer — ~0.8s anim
        current_bar_group_0 = bars[0] # VGroup for value 4
        current_bar_group_1 = bars[1] # VGroup for value 2

        # Get current x positions for swapping
        x_pos_0 = current_bar_group_0.get_x()
        x_pos_1 = current_bar_group_1.get_x()

        # Animate swap
        swap_anim_0 = current_bar_group_0.animate.move_to(x_pos_1 * RIGHT + current_bar_group_0.get_y() * UP)
        swap_anim_1 = current_bar_group_1.animate.move_to(x_pos_0 * RIGHT + current_bar_group_1.get_y() * UP)
        
        self.play(swap_anim_0, swap_anim_1, run_time=0.8)

        # Update the 'bars' VGroup to reflect the new logical order
        # (This is important for correctly referencing elements in subsequent scenes)
        bars_list = list(bars)
        bars_list[0], bars_list[1] = bars_list[1], bars_list[0]
        bars = VGroup(*bars_list) # Recreate VGroup with swapped elements
        
        self.wait(1.3)

        # SCENE 6 (Impact): Why it matters — ~0.8s anim
        impact_text = Text("Larger elements 'bubble' to the end.", color=WHITE, font_size=32).to_edge(UP)
        
        # After first swap, bars are visually: [2, 4, 5, 1, 3]
        # The '5' is now at bars[2] (its original index).
        bar_group_5_visual = bars[2] # VGroup for value 5
        
        # Define a conceptual shift amount for the '5' bar to illustrate bubbling
        # It moves towards the end.
        shift_amount = (bars[-1].get_x() - bar_group_5_visual.get_x()) * 0.7 # Move a portion towards the last bar's x

        self.play(
            FadeOut(explanation_group), # Clear previous explanation
            bar_rect_0.animate.set_color(TEAL_A), # Reset colors of previously highlighted bars
            bar_rect_1.animate.set_color(TEAL_A),
            FadeIn(impact_text), # Introduce impact text
            bar_group_5_visual[0].animate.set_color(GREEN).shift(shift_amount), # Highlight '5' and move it
            run_time=0.8 # Total for this play call
        )
        self.wait(1.3)

        # SCENE 7 (Summary): 3 bullet points animated — ~0.8s anim
        summary_title = Text("Bubble Sort Summary", font_size=48, color=TEAL_A).to_edge(UP)
        bullet1 = Text("1. Compares adjacent items.", font_size=30, color=WHITE)
        bullet2 = Text("2. Swaps if out of order.", font_size=30, color=WHITE)
        bullet3 = Text("3. Repeats until sorted.", font_size=30, color=WHITE)
        summary_group = VGroup(bullet1, bullet2, bullet3).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        summary_group.next_to(summary_title, DOWN, buff=0.5).align_to(summary_title, LEFT)

        # Create sorted bars for the final visual
        sorted_values = sorted([4, 2, 5, 1, 3]) # Final sorted values: [1, 2, 3, 4, 5]
        sorted_bars = VGroup()
        for i, val in enumerate(sorted_values):
            bar_group = create_bar_group(val, x_offset + i * 1.5, max_height=max_bar_height, bar_color=GREEN)
            sorted_bars.add(bar_group)
        sorted_bars.center().shift(DOWN*1.5) # Position below summary text

        self.play(
            FadeOut(impact_text, bar_group_5_visual[0].shift(shift_amount*-1)), # Fade out previous scene, move '5' bar back for clean fade out of all bars
            FadeOut(bars), # Fade out all previous bars
            FadeIn(summary_title, summary_group, sorted_bars, lag_ratio=0.1), # Fade in summary elements
            run_time=0.8 # Total for this play call
        )
        self.wait(1.3)
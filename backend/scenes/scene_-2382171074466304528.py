from manim import *

config.pixel_width = 480
config.pixel_height = 854
config.frame_width = 8.0
config.frame_height = 14.22
config.background_color = "#000000"


# Title: Bubble Sort Algorithm
# Aspect Ratio: 9:16 (Vertical)
# Duration: ~30 Seconds

class MainScene(Scene):
    def construct(self):
        # Configuration for vertical video
        self.camera.background_color = BLACK
        
        # Helper function for boxes
        def create_box(val, color=TEAL_A):
            rect = Rectangle(height=1.2, width=1.2, color=color, stroke_width=4)
            num = Text(str(val), color=WHITE, font_size=36)
            return VGroup(rect, num)

        # Scene 1: Unsorted Chaos
        title1 = Text("Computers Sort Data", color=PINK, font_size=42).shift(UP * 5)
        numbers = [5, 1, 4, 2, 8]
        boxes = VGroup(*[create_box(n) for n in numbers]).arrange(RIGHT, buff=0.2).shift(UP * 1)
        sub1 = Text("How to arrange these?", color=WHITE, font_size=32).shift(DOWN * 3)
        q_mark = Text("?", color=PINK, font_size=72).shift(DOWN * 1)

        self.play(FadeIn(title1), Create(boxes), Write(sub1), run_time=0.87)
        self.play(FadeIn(q_mark), run_time=0.3)
        self.wait(2.8)
        self.play(FadeOut(title1), FadeOut(sub1), FadeOut(q_mark), run_time=0.3)

        # Scene 2: Meet Bubble Sort
        title2 = Text("Bubble Sort", color=PINK, font_size=42).shift(UP * 5)
        sub2 = Text("Compare adjacent,\nswap if needed.", color=WHITE, font_size=32, line_spacing=1.5).shift(DOWN * 4)
        arrow = DoubleArrow(boxes[0].get_bottom(), boxes[1].get_bottom(), color=PINK).shift(DOWN * 0.5)
        
        self.play(FadeIn(title2), FadeIn(sub2), Create(arrow), run_time=0.87)
        self.play(boxes[0].animate.set_color(PINK), boxes[1].animate.set_color(PINK), run_time=0.3)
        self.wait(2.8)
        self.play(FadeOut(arrow), run_time=0.3)

        # Scene 3: The First Pass Begins (Swap 5 and 1)
        sub3 = Text("5 is larger than 1.\nSwap them!", color=WHITE, font_size=32, line_spacing=1.5).shift(DOWN * 4)
        
        # Animation: Swap boxes[0] and boxes[1]
        self.play(
            FadeIn(sub3),
            boxes[0].animate.move_to(boxes[1].get_center()),
            boxes[1].animate.move_to(boxes[0].get_center()),
            run_time=0.87
        )
        self.wait(2.8)
        self.play(FadeOut(sub2), FadeOut(sub3), run_time=0.3)

        # Update local array for logic consistency
        # boxes[0] is now physically at pos 1, boxes[1] at pos 0
        
        # Scene 4: Bubbling Up Largest
        title4 = Text("Bubbling Up", color=PINK, font_size=42).shift(UP * 5)
        sub4 = Text("The largest value\nmoves to the end.", color=WHITE, font_size=32, line_spacing=1.5).shift(DOWN * 4)
        
        # Quickly show the '5' moving further (simulate bubbling)
        # Note: 8 is already at end in this set, but 5 moves to index 3
        self.play(
            FadeIn(title4),
            FadeIn(sub4),
            boxes[0].animate.move_to(boxes[2].get_center()),
            boxes[2].animate.move_to(boxes[0].get_center()), # Swapping 5 with 4
            run_time=0.87
        )
        # Highlight 8 as "bubbled" (sorted element)
        self.play(boxes[4].animate.set_color(GREEN), run_time=0.3)
        self.wait(2.8)
        self.play(FadeOut(title2), FadeOut(title4), FadeOut(sub4), run_time=0.3)

        # Scene 5: Multiple Passes
        title5 = Text("Repeat Passes", color=PINK, font_size=42).shift(UP * 5)
        sub5 = Text("Each pass fixes\nthe next largest.", color=WHITE, font_size=32, line_spacing=1.5).shift(DOWN * 4)
        
        # Simulate sorting more
        self.play(
            FadeIn(title5),
            FadeIn(sub5),
            boxes[0].animate.set_color(GREEN), # 5 is now sorted relative to 4
            boxes[2].animate.set_color(WHITE), # 4
            run_time=0.87
        )
        self.play(Indicate(boxes, color=GREEN), run_time=0.3)
        self.wait(2.8)
        self.play(FadeOut(title5), FadeOut(sub5), run_time=0.3)

        # Scene 6: Finally Sorted!
        title6 = Text("Finally Sorted!", color=GREEN, font_size=48).shift(UP * 5)
        sub6 = Text("No more swaps needed.", color=WHITE, font_size=32).shift(DOWN * 4)
        
        # Final sequence [1, 2, 4, 5, 8]
        # We manually position them for the 'finished' look
        sorted_vals = [1, 2, 4, 5, 8]
        sorted_group = VGroup(*[create_box(v, color=GREEN) for v in sorted_vals]).arrange(RIGHT, buff=0.2).shift(UP * 1)
        
        self.play(
            FadeIn(title6),
            FadeIn(sub6),
            ReplacementTransform(boxes, sorted_group),
            run_time=0.87
        )
        self.play(Indicate(title6, scale_factor=1.2), run_time=0.3)
        self.wait(2.8)
        self.play(FadeOut(sub6), FadeOut(sorted_group), run_time=0.3)

        # Scene 7: Bubble Sort Summary
        title7 = Text("Bubble Sort Summary", color=PINK, font_size=42).shift(UP * 5)
        step1 = Text("1. Compare neighbors", color=WHITE, font_size=34).shift(UP * 1)
        step2 = Text("2. Swap if out of order", color=WHITE, font_size=34).shift(DOWN * 0.5)
        step3 = Text("3. Repeat until sorted", color=WHITE, font_size=34).shift(DOWN * 2)
        
        summary = VGroup(step1, step2, step3)
        
        self.play(
            FadeIn(title7),
            Write(summary),
            run_time=0.87
        )
        self.play(summary.animate.set_color(TEAL_A), run_time=0.3)
        self.wait(2.8)
        
        # Final Hold
        self.play(FadeOut(title6), FadeOut(title7), FadeOut(summary), run_time=0.3)
        self.wait(2.2)
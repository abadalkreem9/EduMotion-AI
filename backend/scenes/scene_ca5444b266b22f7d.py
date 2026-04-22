from manim import *

config.pixel_width = 854
config.pixel_height = 480
config.frame_width = 14.22
config.frame_height = 8.0
config.background_color = "#111111"


class MainScene(Scene):
    def construct(self):
        self.camera.background_color = BLACK

        # --- Scene 1: Hook ---
        title = Text("Pythagorean Theorem", font_size=54, color=TEAL_A, weight=BOLD)
        question = Text("How does it work?", font_size=36, color=WHITE).next_to(title, DOWN, buff=0.8)
        
        self.play(FadeIn(title, shift=UP), run_time=0.8)
        self.play(FadeIn(question, shift=DOWN), run_time=0.8)
        self.wait(2.6)

        # --- Scene 2: Setup ---
        context_text1 = Text("Building a ramp?", font_size=32, color=WHITE).shift(UP*0.5 + LEFT*2)
        context_text2 = Text("Measuring a roof?", font_size=32, color=WHITE).next_to(context_text1, RIGHT, buff=1)
        context_text_group = VGroup(context_text1, context_text2)

        self.play(FadeOut(title, question), run_time=0.8)
        self.play(FadeIn(context_text_group), run_time=0.8) # Appear together
        self.wait(2.6)

        # --- Scene 3: Problem ---
        problem_text = Text("Finding unknown lengths...", font_size=36, color=RED_B).to_edge(UP)
        
        # Right triangle vertices (larger for the initial problem)
        p1 = 2*LEFT + 2*DOWN
        p2 = 2*RIGHT + 2*DOWN
        p3 = 2*LEFT + 1*UP 

        triangle = Polygon(p1, p2, p3, color=TEAL_A)
        
        # Labels for sides
        a_label = Text("a", color=TEAL_A).next_to(Line(p1, p3), LEFT)
        b_label = Text("b", color=TEAL_A).next_to(Line(p1, p2), DOWN)
        c_label = Text("c", color=TEAL_A).next_to(Line(p2, p3), RIGHT+UP) # This is the hypotenuse
        
        # Right angle mark for the triangle
        sq_corner_tri = Square(side_length=0.4, color=PINK, fill_opacity=0.7).move_to(p1 + 0.2*RIGHT + 0.2*UP)
        
        triangle_group = VGroup(triangle, a_label, b_label, c_label, sq_corner_tri)

        self.play(FadeOut(context_text_group), run_time=0.8)
        self.play(FadeIn(problem_text, triangle_group), run_time=0.8) # Problem text and triangle appear together
        self.wait(2.6)

        # --- Scene 4: Explanation ---
        # Define the smaller triangle for explanation directly at its final position
        p_expl1 = 3.5 * LEFT + 0.5 * DOWN
        p_expl2 = 1.5 * LEFT + 0.5 * DOWN
        p_expl3 = 3.5 * LEFT + 1.0 * UP # Adjusted for better aspect ratio
        
        expl_triangle = Polygon(p_expl1, p_expl2, p_expl3, color=TEAL_A)
        expl_a_label = Text("a", color=TEAL_A).next_to(Line(p_expl1, p_expl3), LEFT, buff=0.1)
        expl_b_label = Text("b", color=TEAL_A).next_to(Line(p_expl1, p_expl2), DOWN, buff=0.1)
        expl_c_label = Text("c", color=TEAL_A).next_to(Line(p_expl2, p_expl3), RIGHT+UP, buff=0.1)
        expl_sq_corner = Square(side_length=0.2, color=PINK, fill_opacity=0.7).move_to(p_expl1 + 0.1*RIGHT + 0.1*UP)
        
        expl_tri_group = VGroup(expl_triangle, expl_a_label, expl_b_label, expl_c_label, expl_sq_corner)
        
        explanation_eq = Text("a^2 + b^2 = c^2", color=WHITE, font_size=36).to_edge(RIGHT).shift(UP*0.5)

        self.play(FadeOut(problem_text, triangle_group), run_time=0.8)
        self.play(FadeIn(expl_tri_group), FadeIn(explanation_eq), run_time=0.8) # Triangle, labels, and equation appear together
        self.wait(2.6)

        # --- Scene 5: Solution ---
        # Specific triangle for solution
        sol_p1 = 3*LEFT + 2*DOWN
        sol_p2 = 1*RIGHT + 2*DOWN
        sol_p3 = 3*LEFT + 1*UP
        
        sol_triangle = Polygon(sol_p1, sol_p2, sol_p3, color=TEAL_A)
        sol_a_label = Text("3", color=TEAL_A).next_to(Line(sol_p1, sol_p3), LEFT, buff=0.1)
        sol_b_label = Text("4", color=TEAL_A).next_to(Line(sol_p1, sol_p2), DOWN, buff=0.1)
        sol_c_label = Text("c", color=TEAL_A).next_to(Line(sol_p2, sol_p3), RIGHT+UP, buff=0.1)
        
        sol_sq_corner = Square(side_length=0.2, color=PINK, fill_opacity=0.7).move_to(sol_p1 + 0.1*RIGHT + 0.1*UP)
        
        sol_tri_group = VGroup(sol_triangle, sol_a_label, sol_b_label, sol_c_label, sol_sq_corner)

        # Equations for solution
        eq1 = Text("3^2 + 4^2 = c^2", color=WHITE).next_to(explanation_eq, DOWN, buff=0.5).align_to(explanation_eq, LEFT).shift(RIGHT*1)
        eq2 = Text("9 + 16 = c^2", color=WHITE).next_to(eq1, DOWN, buff=0.3).align_to(eq1, LEFT)
        eq4 = Text("c = 5", color=GREEN).next_to(eq2, DOWN, buff=0.3).align_to(eq2, LEFT) # Skipping 25=c^2 for brevity

        self.play(FadeOut(expl_tri_group, explanation_eq), run_time=0.6) # The 0.6s animation
        self.play(FadeIn(sol_tri_group), Write(eq1), run_time=0.8) # Triangle with numbers appears, first eq written
        self.play(FadeOut(eq1, shift=UP), FadeIn(eq2), run_time=0.8) # Transition to second eq
        self.play(FadeOut(eq2, shift=UP), FadeIn(eq4), run_time=0.8) # Transition to final answer
        self.wait(2.6)

        # --- Scene 6: Impact ---
        impact_text1 = Text("Geometry problems become simple.", font_size=36, color=WHITE).shift(UP*1)
        impact_text2 = Text("Used in navigation, construction,", font_size=36, color=WHITE).next_to(impact_text1, DOWN, buff=0.5).align_to(impact_text1, LEFT)
        impact_text3 = Text("and engineering design daily.", font_size=36, color=WHITE).next_to(impact_text2, DOWN, buff=0.3).align_to(impact_text2, LEFT)
        impact_text_group = VGroup(impact_text1, impact_text2, impact_text3)

        self.play(FadeOut(sol_tri_group, eq4), FadeIn(impact_text_group), run_time=0.8)
        self.wait(2.6)

        # --- Scene 7: Summary ---
        summary_title = Text("Key Takeaways:", font_size=42, color=TEAL_A, weight=BOLD).to_edge(UP)
        bullet1 = Text("• Right triangles only.", font_size=36, color=WHITE).next_to(summary_title, DOWN, buff=0.8).align_to(summary_title, LEFT).shift(RIGHT)
        bullet2 = Text("• a^2 + b^2 = c^2", font_size=36, color=WHITE).next_to(bullet1, DOWN, buff=0.5).align_to(bullet1, LEFT)
        bullet3 = Text("• Find any missing side.", font_size=36, color=WHITE).next_to(bullet2, DOWN, buff=0.5).align_to(bullet2, LEFT)
        
        summary_group = VGroup(summary_title, bullet1, bullet2, bullet3)

        self.play(FadeOut(impact_text_group), FadeIn(summary_group), run_time=0.8)
        self.wait(2.6)
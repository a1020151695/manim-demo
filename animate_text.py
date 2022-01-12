from manimlib import *


class AnimateText(Scene):
    def construct(self):    # 左移，变色，变大
        text = Tex("O")
        self.play(text.animate.shift(LEFT))
        self.play(text.animate.set_color(YELLOW))
        self.wait()
        self.play(text.animate.set_height(2))
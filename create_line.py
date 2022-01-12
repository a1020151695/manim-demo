from manimlib import *

class CreateLine(Scene):
    def construct(self):
        line = Line(UL)     # np.array((-1., 1., 0.)) UP+LEFT
        self.play(ShowCreation(line))
from manimlib import *


class FormulaTransformer(Scene):
    def construct(self):
        # 为了美观，字符之间isolate开来
        to_isolate = ["B", "C", "=", "(", ")"]

        # 分割各单位也可以用另外一种方式，拆分成多个字符串
        lines = VGroup(
            Tex("A^2", "+", "B^2", "=", "C^2"),
            Tex("A^2", "=", "C^2", "-", "B^2"),
            Tex("A^2 = (C + B)(C - B)", isolate=["A^2", *to_isolate]),
            Tex("A = \\sqrt{(C + B)(C - B)}", isolate=["A", *to_isolate])
        )

        # 添加高亮
        for line in lines:
            line.set_color_by_tex_to_color_map({
                "A": BLUE,
            })

        # 把n行文本从上往下排列
        lines.arrange(DOWN, buff=LARGE_BUFF)

        # 文本变形参数
        play_kw = {"run_time": 2}

        # 如果直接就变形的话，原本的这个文本就被变走了，不合常理，应该留个原本的式子在那
        # 第一行公式
        self.play(FadeIn(lines[0]))

        # 第二行公式
        self.play(
            TransformMatchingTex(
                # 提供前后两个状态
                lines[0].copy(), lines[1],
                path_arc=90 * DEGREES,
                # 90度，DEGREES = 2pi/360
                # 90度，可以理解为变形开始时发射的角度，对于等式左右两边移项，90度是效果最好的
            ),
            **play_kw
        )
        self.wait()

        # 第三行公式
        self.play(
            TransformMatchingTex(lines[1].copy(), lines[2]),
            **play_kw
        )
        self.wait()

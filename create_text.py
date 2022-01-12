from manimlib import *


class CreateText(Scene):
    def construct(self):
        # t2f表示个别字体不同样式
        # t2c表示个别字体不同颜色
        # t2s表示个别字体斜体
        # t2w表示个别字体粗体
        text = Text("how are you today honey", font="Consolas", font_size=50,
                    t2f={"are": "Arial"},
                    t2c={"honey": BLUE},
                    t2s={"how": ITALIC},
                    t2w={"you": BOLD}
                    )

        # 字体太大的话，会在最大长度内被挤成一堆
        # label.set_width(2)

        # text.set_color(YELLOW)

        # 缩放，缩放后不可以zoom
        # label.scale(0.5)

        # 打印效果
        self.play(Write(text))

        # 逐渐键出
        self.play(ShowCreation(text))

        # 等待2s
        self.wait(2)

        # 向上渐入
        self.play(FadeIn(text,UP))

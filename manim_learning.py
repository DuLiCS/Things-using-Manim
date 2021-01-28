from manimlib.imports import *

class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()
        square = Square()
        square.flip(RIGHT)
        square.rotate(-3 * TAU / 8)
        circle.set_fill(PINK, opacity=0.5)

        self.play(ShowCreation(circle))
        self.play(Transform(square, circle))
        self.play(FadeOut(square))


class WriteStuff(Scene):
    def construct(self):
        example_text = TextMobject(
            "This is a some text",
            tex_to_color_map={"text": YELLOW}
        )
        example_tex = TexMobject(
            "\\sum_{k=1}^\\infty {1 \\over k^2} = {\\pi^2 \\over 6}",
        )
        group = VGroup(example_text, example_tex)
        group.arrange(DOWN)
        group.set_width(FRAME_WIDTH - 2 * LARGE_BUFF)

        self.play(Write(example_text))
        self.play(Write(example_tex))
        self.wait()



class UpdatersExample(Scene):
    def construct(self):
        decimal = DecimalNumber(
            0,
            show_ellipsis=True,
            num_decimal_places=3,
            include_sign=True,
        )
        square = Square().to_edge(UP)

        decimal.add_updater(lambda d: d.next_to(square, RIGHT))
        decimal.add_updater(lambda d: d.set_value(square.get_center()[1]))
        self.add(square, decimal)
        self.play(
            square.to_edge, DOWN,
            rate_func=there_and_back,
            run_time=5,
        )
        self.wait()


class HelloWorld(Scene):
  	def construct(self):
  		helloworld = TextMobject("这是用程序写的哦")


  		self.play(Write(helloworld))
  		self.wait(2)

class OpeningManimExample(Scene):
    def construct(self):
        title = TextMobject("This is some \\LaTeX") # 文字
        basel = TexMobject(                         # 公式
            "\\sum_{n=1}^\\infty "
            "\\frac{1}{n^2} = \\frac{\\pi^2}{6}"
        )
        VGroup(title, basel).arrange(DOWN)          # 集合到一起后排列位置
        self.play(
            Write(title),             # "写"出title文字
            FadeInFrom(basel, UP),    # 将basel公式从上方淡入
        )
        self.wait()  # 停顿一秒

        transform_title = TextMobject("That was a transform")
        transform_title.to_corner(UP + LEFT) # 放到最左上角
        self.play(
            Transform(title, transform_title), # 将title变换为transform_title
            LaggedStart(*map(FadeOutAndShiftDown, basel)), # 将basel公式中的每个字符依次从下方淡出
        )
        self.wait()  # 停顿一秒

        grid = NumberPlane()  # 构建一个坐标平面
        grid_title = TextMobject("This is a grid")
        grid_title.scale(1.5)
        grid_title.move_to(transform_title)

        self.add(grid, grid_title)  # 确保grid_title在grid上方
        self.play(
            FadeOut(title),               # 淡出title
            FadeInFromDown(grid_title),   # 从下方淡入grid_title
            ShowCreation(grid, run_time=3, lag_ratio=0.1), # 创建grid的动画，时长为3，延迟为10%
        )
        self.wait()

        grid_transform_title = TextMobject(
            "That was a non-linear function \\\\"
            "applied to the grid"
        )
        grid_transform_title.move_to(grid_title, UL)
        grid.prepare_for_nonlinear_transform() # 让grid准备进行非线性变换
        self.play(
            grid.apply_function,       # 对grid施加一个函数，实现非线性变换
            lambda p: p + np.array([   # 输入值为一个点，返回值也为一个点
                np.sin(p[1]),
                np.sin(p[0]),
                0,
            ]),
            run_time=3,
        )
        self.wait()
        self.play(
            Transform(grid_title, grid_transform_title)
        )
        self.wait()
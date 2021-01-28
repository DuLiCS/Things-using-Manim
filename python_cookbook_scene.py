from manimlib.imports import *


#1.1 将序列分解为单独的变量

class Cookbook1_1(Scene):
    def construct(self):
        book_name = TextMobject("Python Cookbook")
        section_name = TextMobject("1.1将序列分解为单独的变量")
        author_name = TextMobject("Coding by GTrush").move_to(DOWN*1.5)
        title_group = VGroup(book_name,section_name).arrange(DOWN)          # 集合到一起后排列位置
        self.play(Write(book_name),FadeInFrom(section_name, UP))
        self.play(FadeInFromDown(author_name))
        self.wait(3)

        self.play(*[FadeOutAndShiftDown(mob,DOWN) for mob in title_group])
        self.play(FadeOutAndShiftDown(author_name))


        problem_description =TextMobject('问题：我们有一个包含N个元素的元组或序列\\\\现在想将它分解为N个单独的变量').scale(1)

        problem_solution = TextMobject('解决方案：任何序列(或可迭代的对象)\\\\都可以通过一个简单的赋值操作来分解为单独的变量。唯一\\\\的要求是变量的总数和结构要与序列相吻合').scale(1)

        

        self.play(Write(problem_description))
        self.wait(5)  # 停顿一秒

        self.play(Transform(problem_description, problem_solution))
        self.wait(5)
        self.play(*[FadeOutAndShiftDown(problem_description)])
        self.wait()


        transform_title = TextMobject("代码示例")
        transform_title.to_corner(UP + LEFT)

        self.play(Write(transform_title))

        

        tex_bg = Rectangle(stroke_width=1, stroke_color=GRAY, plot_depth=-1)
        tex_bg.set_height(6.2, stretch=True).set_width(5.4, stretch=True)
        loc = UP * 2.9 + RIGHT * 3.00
        tex_bg.to_corner(RIGHT * 1.25 + UP * 1.25)
        tex_add = CodeLine('>>>p = (4, 5)').move_to(loc)
        tex_shift_l = CodeLine('>>>x, y = p').next_to(tex_add, DOWN).align_to(tex_add, LEFT)
        tex_shift_2 = CodeLine('>>>x').next_to(tex_shift_l, DOWN).align_to(tex_shift_l, LEFT)
        tex_shift_3 = CodeLine('4').next_to(tex_shift_2, DOWN).align_to(tex_shift_2, LEFT)
        tex_shift_4 = CodeLine('>>>y').next_to(tex_shift_3, DOWN).align_to(tex_shift_3, LEFT)
        tex_shift_5 = CodeLine('5').next_to(tex_shift_4, DOWN).align_to(tex_shift_4, LEFT)


        loc_02 = DOWN * 1.4
        caption_add = CodeLine('将元组(4,5)赋予变量p', font='思源黑体 Bold', size=1.0).to_edge(loc_02)
        caption_shift_1 = CodeLine('将元组中的两个元素分别赋予变量x，变量y', font='思源黑体 Bold', size=1.0).to_edge(loc_02)
        caption_shift_1 = CodeLine('将元组中的两个元素分别赋予变量x，变量y', font='思源黑体 Bold', size=1.0).to_edge(loc_02)


        tex_p = TextMobject('p').move_to(LEFT*4.5+UP*2.5)
        tex_value = TextMobject('(','4 ',',','5 ',')').move_to(LEFT*1+UP*2.5)

        tex_x = TextMobject('x').move_to(LEFT*5)
        tex_y = TextMobject('y').move_to(LEFT*2)

        arrow1 = Arrow(LEFT*4+UP*2.5,LEFT*2+UP*2.5)
        arrow2 = Arrow(LEFT*2+UP*2,LEFT*5+UP*0.5)
        arrow3 = Arrow(LEFT*1+UP*2,LEFT*2+UP*0.5)

        scene1 = VGroup(tex_bg,tex_add,tex_shift_l,tex_shift_2,tex_shift_3,tex_shift_4,tex_shift_5,caption_add,caption_shift_1,tex_p,tex_x,tex_value,tex_y,arrow1,arrow2,arrow3)



        self.wait()
        self.play(FadeInFromDown(tex_bg))
        self.play(Write(tex_p),Write(tex_value),Write(arrow1))
        self.play(Write(tex_add), Write(caption_add), run_time=1.5)
        self.wait()

        self.play(Write(tex_shift_l), ReplacementTransform(caption_add, caption_shift_1), run_time=1.5)
        self.play(Write(tex_shift_2),run_time=1.5)
        self.play(Write(tex_shift_3),run_time=1.5)
        self.play(Indicate(tex_value[1]))
        self.play(Write(tex_x),Write(arrow2))
        self.play(Indicate(tex_x))
        self.play(Write(tex_shift_4),run_time=1.5)
        self.play(Write(tex_shift_5),run_time=1.5)
        self.play(Indicate(tex_value[3]))
        self.play(Write(tex_y),Write(arrow3))
        self.play(Indicate(tex_y))




        self.wait(2)

        self.play(*[FadeOutAndShiftDown(mob,DOWN) for mob in scene1])

        tex_bg = Rectangle(stroke_width=1, stroke_color=GRAY, plot_depth=-1)
        tex_bg.set_height(6.2, stretch=True).set_width(6.5, stretch=True)
        loc = UP * 2.9 + RIGHT * 3.1
        tex_bg.to_corner(RIGHT * 1.25 + UP * 1.25)
        self.play(FadeInFromDown(tex_bg))
        tex_1 = CodeLine(">>>data = ['ACME', 50, 91.1, (2012, 12, 21)]",size=0.5).move_to(loc)
        tex_2 = CodeLine(">>>name,shares,price,date = data",size=0.5).next_to(tex_1, DOWN).align_to(tex_1, LEFT)
        tex_8 = CodeLine(">>>name",size=0.5).next_to(tex_2, DOWN).align_to(tex_2, LEFT)
        tex_9 = CodeLine("'ACME'",size=0.5).next_to(tex_8, DOWN).align_to(tex_8, LEFT)
        tex_10 = CodeLine(">>>shares",size=0.5).next_to(tex_9, DOWN).align_to(tex_9, LEFT)
        tex_11 = CodeLine("50",size=0.5).next_to(tex_10, DOWN).align_to(tex_10, LEFT)
        tex_12 = CodeLine(">>>price",size=0.5).next_to(tex_11, DOWN).align_to(tex_11, LEFT)
        tex_13 = CodeLine("91.1",size=0.5).next_to(tex_12, DOWN).align_to(tex_12, LEFT)
        tex_14 = CodeLine(">>>date",size=0.5).next_to(tex_13, DOWN).align_to(tex_13, LEFT)
        tex_15 = CodeLine("(2012, 12, 21)",size=0.5).next_to(tex_14, DOWN).align_to(tex_14, LEFT)
        self.play(Write(tex_1), Write(tex_2), run_time=1.5)

        tex_3 = TextMobject("["," ACME",","," 50",","," 91.1",","," (2012, 12, 21)","]",size = 0.6).move_to(LEFT*3+UP*2.5)
        tex_4 = TextMobject('name').move_to(LEFT*6)
        tex_5 = TextMobject('shares').move_to(LEFT*4)
        tex_6 = TextMobject('price').move_to(LEFT*2)
        tex_7 = TextMobject('date').move_to(LEFT*0.5)

        arrow4 = Arrow(LEFT*5+UP*2,LEFT*6+UP*0.5)
        arrow5 = Arrow(LEFT*4+UP*2,LEFT*4+UP*0.5)
        arrow6 = Arrow(LEFT*3+UP*2,LEFT*2+UP*0.5)
        arrow7 = Arrow(LEFT*1+UP*2,LEFT*0.5+UP*0.5)
        


        self.play(Write(tex_3))
        self.play(Indicate(tex_3[1]))
        self.play(Write(tex_4),Write(tex_8),Write(tex_9),Write(arrow4))
        self.play(Indicate(tex_4))

        self.play(Indicate(tex_3[3]))
        self.play(Write(tex_10),Write(tex_11),Write(tex_5),Write(arrow5))
        self.play(Indicate(tex_5))

        self.play(Indicate(tex_3[5]))

        self.play(Write(tex_12),Write(tex_13),Write(tex_6),Write(arrow6))
        self.play(Indicate(tex_6))

        self.play(Indicate(tex_3[7]))

        self.play(Write(tex_14),Write(tex_15),Write(tex_7),Write(arrow7))
        self.play(Indicate(tex_7))



        self.wait(2)

        scene2 = VGroup(tex_bg,tex_1,tex_2,tex_3,tex_4,tex_5,tex_6,tex_7,tex_8,tex_9,tex_10,tex_11,tex_12,tex_13,tex_14,tex_15,tex_1,arrow4,arrow5,arrow6,arrow7)

        self.play(*[FadeOutAndShiftDown(mob,DOWN) for mob in scene2])
        self.wait(2)

        tex_16 = TextMobject('如果元素的数量不匹配\\\\，将得到一个错误').move_to(LEFT*3+UP*2)

        tex_bg = Rectangle(stroke_width=1, stroke_color=GRAY, plot_depth=-1)
        tex_bg.set_height(6.2, stretch=True).set_width(5.4, stretch=True)
        loc = UP * 2.9 + RIGHT * 3.00
        tex_bg.to_corner(RIGHT * 1.25 + UP * 1.25)
        self.play(FadeInFromDown(tex_bg))
        tex_add = CodeLine('>>>p = (4, 5)').move_to(loc)
        tex_shift_l = CodeLine('>>>x, y, z = p').next_to(tex_add, DOWN).align_to(tex_add, LEFT)
        tex_shift_2 = TextMobject('报错!!!',size = 2,color = RED).move_to(LEFT*3)

        self.play(Write(tex_16),Write(tex_add),Write(tex_shift_l),Write(tex_shift_2))
        self.wait(5)

        scene3 = VGroup(tex_bg,tex_16,tex_add,tex_shift_l,tex_shift_2)
        self.play(*[FadeOutAndShiftDown(mob,DOWN) for mob in scene3])
        self.wait(5)


        Scene_tex = TextMobject("字符串，文件迭代器以及生成器也可进行分解")

        self.play(*[SpinInFromNothing(Scene_tex)])
        self.wait(2)
        self.play(FadeOutAndShiftDown(Scene_tex))


        tex_1 = CodeLine(">>>s = 'Hello'",size=0.5).move_to(loc)
        tex_2 = CodeLine(">>>a, b, c, d, e = s",size=0.5).next_to(tex_1, DOWN).align_to(tex_1, LEFT)
        tex_3 = CodeLine(">>>a",size=0.5).next_to(tex_2, DOWN).align_to(tex_2, LEFT)
        tex_4 = CodeLine("'H'",size=0.5).next_to(tex_3, DOWN).align_to(tex_3, LEFT)
        tex_5 = CodeLine(">>>b",size=0.5).next_to(tex_4, DOWN).align_to(tex_4, LEFT)
        tex_6 = CodeLine("'e'",size=0.5).next_to(tex_5, DOWN).align_to(tex_5, LEFT)
        tex_7 = CodeLine(">>>e",size=0.5).next_to(tex_6, DOWN).align_to(tex_6, LEFT)
        tex_8 = CodeLine("o",size=0.5).next_to(tex_7, DOWN).align_to(tex_7, LEFT)

        code_1 = TextMobject('H','e','l','l','o').move_to(LEFT*3+UP*2.5)
        code_2 = TextMobject('a').move_to(LEFT*5)
        code_3 = TextMobject('b').move_to(LEFT*3)
        code_4 = TextMobject('e').move_to(LEFT*1)

        arrow1 = Arrow(LEFT*3.5+UP*2,LEFT*5+UP*0.5)
        arrow2 = Arrow(LEFT*3+UP*2,LEFT*3+UP*0.5)
        arrow3 = Arrow(LEFT*2.5+UP*2,LEFT*1+UP*0.5)


        self.play(FadeInFromDown(tex_bg))

        self.play(Write(tex_1), Write(tex_2), run_time=1.5)
        self.play(Write(code_1))
        
        self.play(Write(tex_3), Write(tex_4), run_time=1.5)
        
        self.play(Indicate(code_1[0]))
        self.play(Write(arrow1),Write(code_2))
        self.play(Indicate(code_2))

        self.play(Indicate(code_1[1]))

        self.play(Write(tex_5), Write(tex_6), run_time=1.5)
        self.play(Write(arrow2),Write(code_3))
        self.play(Indicate(code_3))


        self.play(Indicate(code_1[4]))
        self.play(Write(tex_7), Write(tex_8), run_time=1.5)
        self.play(Write(arrow3),Write(code_4))
        self.play(Indicate(code_4))

        self.wait(2)

        scene4 = VGroup(tex_1,tex_2,tex_3,tex_4,tex_5,tex_6,tex_7,tex_8,tex_bg,arrow1,arrow2,arrow3,code_1,code_2,code_3,code_4,transform_title)
        self.play(*[FadeOutAndShiftDown(mob,DOWN) for mob in scene4])

        self.wait(3)



        tex_bye = TextMobject("Talk is cheap,show me the code")
        self.play(*[SpinInFromNothing(tex_bye)])
        self.wait(5)









        # grid = NumberPlane()  # 构建一个坐标平面
        # grid_title = TextMobject("This is a grid")
        # grid_title.scale(1.5)
        # grid_title.move_to(transform_title)

        # self.add(grid, grid_title)  # 确保grid_title在grid上方
        # self.play(
        #     FadeOut(title),               # 淡出title
        #     FadeInFromDown(grid_title),   # 从下方淡入grid_title
        #     ShowCreation(grid, run_time=3, lag_ratio=0.1), # 创建grid的动画，时长为3，延迟为10%
        # )
        # self.wait()

        # grid_transform_title = TextMobject(
        #     "That was a non-linear function \\\\"
        #     "applied to the grid"
        # )
        # grid_transform_title.move_to(grid_title, UL)
        # grid.prepare_for_nonlinear_transform() # 让grid准备进行非线性变换
        # self.play(
        #     grid.apply_function,       # 对grid施加一个函数，实现非线性变换
        #     lambda p: p + np.array([   # 输入值为一个点，返回值也为一个点
        #         np.sin(p[1]),
        #         np.sin(p[0]),
        #         0,
        #     ]),
        #     run_time=3,
        # )
        # self.wait()
        # self.play(
        #     Transform(grid_title, grid_transform_title)
        # )
        # self.wait()






class CodeLine(Text):

    CONFIG = {
        't2c': {
            'RIGHT': ORANGE,
            'LEFT': ORANGE,
            'DOWN': ORANGE,
            'UP': ORANGE,
            'UR': ORANGE,
            'UL': ORANGE,
            'DR': ORANGE,
            'DL': ORANGE,
            'ORIGIN': ORANGE,
            'DEGREES': ORANGE,
            'BLACK': ORANGE,
            'Arc': ORANGE,
            'Circle': ORANGE,
            'AnnularSector': ORANGE,
            'ArcBetweenPoints': ORANGE,
            'CurvedArrow': ORANGE,
            'CurvedDoubleArrow': ORANGE,
            'FadeIn': average_color(RED, ORANGE),
            'move_to': BLUE_D,
            'shift': BLUE_D,
            'next_to': BLUE_D,
            'to_corner': BLUE_D,
            'to_edge': BLUE_D,
            'align_to': BLUE_D,
            'scale': BLUE_D,
            'rotate': BLUE_D,
            'flip': BLUE_D,
            'add': BLUE_D,
            'play': BLUE_D,
            'set_width': BLUE_D,
            'set_stroke': BLUE_D,
            '>':RED_A,
            "=":RED_D,
            '0': PURPLE,
            '1': PURPLE,
            '2': average_color(BLUE, PINK),
            '3': average_color(BLUE, PINK),
            '4': PURPLE_D,
            '5': PURPLE_E,
            '6': average_color(BLUE, PINK),
            '7': average_color(BLUE, PINK),
            '8': average_color(BLUE, PINK),
            '9': average_color(BLUE, PINK),
            'p1': average_color(BLUE, PINK),
            'p2': average_color(BLUE, PINK),
            'angle': average_color(BLUE, PINK),
            'self': PINK,
            'mob': RED_D,
            '~': WHITE, # 随便搞个不常用的字符设成白色，以便在有时不能用空格占位时（比如涉及Transform）当空格用
        },
        'font': 'Consolas',
        'size': 1.0,
        'color': WHITE,
        'plot_depth': 2,
    }

    def __init__(self, text, **kwargs):
        # digest_config(self, kwargs)
        Text.__init__(self, text, **kwargs)

class Emote(SVGMobject):

    CONFIG = {
        'file_name': r'D:\Code\Project\Manim\manim\assets\Svg\1.svg',
        'shake_color': average_color(YELLOW, ORANGE),
    }
    def __init__(self, **kwargs):
        digest_config(self, kwargs)
        SVGMobject.__init__(self, file_name=self.file_name, **kwargs)
        self.list = [0, 1, 2, 3, 5, 6, 9]
        for i in self.list:
            self[i].set_fill(self.shake_color, 0)

        self.attribute_list = [self.get_height(), self.get_width(), self.get_center()]
        # self.add_updater(self.update_emote)

    def update_emote(self, mob):
        h, w, c = self.get_height(), self.get_width(), self.get_center()

        add_shake = not((h == self.attribute_list[0]) and (w == self.attribute_list[1])
                        and (c[0] == self.attribute_list[2][0]) and (c[1] == self.attribute_list[2][1]))
        self.attribute_list = [self.get_height(), self.get_width(), self.get_center()]

        if add_shake:
            for i in self.list:
                self[i].set_opacity(1)
        else:
            for i in self.list:
                self[i].set_opacity(0)

    # def update_emote_02(self, mob):
    #     h, w, c = self.get_height(), self.get_width(), self.get_center()
    #
    #     add_shake = not((h == self.attribute_list[0]) and (w == self.attribute_list[1])
    #                     and (c[0] == self.attribute_list[2][0]) and (c[1] == self.attribute_list[2][1]))
    #     self.attribute_list = [self.get_height(), self.get_width(), self.get_center()]
    #
    #     if add_shake:
    #         self.set_opacity(1)
    #     else:
    #         self.set_opacity(0)

    def shake_on(self):
        self.set_opacity(1)
        return self

    def shake_off(self):
         for i in self.list:
            self[i].set_fill(self.shake_color, 0)
         return self

class Emote_new(VGroup):
    CONFIG = {
        'file_name': r'D:\Code\Project\Manim\manim\assets\Svg\1.svg',
        'shake_color': average_color(YELLOW, ORANGE),
        'height': 2.5,
    }
    def __init__(self, **kwargs):
        VGroup.__init__(self, **kwargs)
        self.emote = SVGMobject(self.file_name, **kwargs).set_height(self.height)
        self.emote_02 = SVGMobject(self.file_name, **kwargs).set_height(self.height)
        self.center_dot = Dot().move_to(self.emote.get_center()).shift((DOWN + RIGHT*0.4) * self.height * 0.18).set_opacity(0)
        list = [0, 1, 2, 3, 5, 6, 9]
        for i in list:
            self.emote[i].set_fill(self.shake_color, 0)
            self.emote_02[i].set_fill(self.shake_color, 0)
        self.add(self.emote_02, self.center_dot, self.emote)
        self.attribute_list = [self.get_height(), self.get_width(), self.get_center()]
        self.emote_02.add_updater(self.update_emote)

    def update_emote(self, mob):
        h, w, c = self.get_height(), self.get_width(), self.get_center()

        add_shake = not((h == self.attribute_list[0]) and (w == self.attribute_list[1])
                        and (c[0] == self.attribute_list[2][0]) and (c[1] == self.attribute_list[2][1]))
        self.attribute_list = [self.get_height(), self.get_width(), self.get_center()]

        if add_shake:
            mob.set_opacity(1)
        else:
            mob.set_opacity(0)

    def shake_on(self):
        self.emote_02.set_opacity(1)
        return self
    def shake_off(self):
        self.emote_02.set_opacity(0)
        return self

class 代码风格测试(Scene):

    CONFIG = {
        'camera_config': {
            'background_color': WHITE,
        }
    }

    def construct(self):

        emote = Emote_new(color=BLACK, plot_depth=1).set_height(2.4).shift(LEFT * 4 + UP)

        tex_bg = Rectangle(stroke_width=1, stroke_color=GRAY, fill_color=LIGHT_GREY, fill_opacity=0.25, plot_depth=-1)
        tex_bg.set_height(6.2, stretch=True).set_width(5.4, stretch=True)
        loc = UP * 2.9 + RIGHT * 2.64
        tex_bg.to_corner(RIGHT * 1.25 + UP * 1.25)
        tex_add = CodeLine('self.add(mob)').move_to(loc)
        tex_shift_l = CodeLine('mob.shift(LEFT)').next_to(tex_add, DOWN).align_to(tex_add, LEFT)
        tex_flip_1 = CodeLine('mob.flip()').next_to(tex_shift_l, DOWN).align_to(tex_shift_l, LEFT)
        tex_flip_2 = CodeLine('mob.flip()').next_to(tex_flip_1, DOWN).align_to(tex_flip_1, LEFT)
        tex_shift_r2 = CodeLine('mob.shift(RIGHT * 2)').next_to(tex_flip_2, DOWN).align_to(tex_flip_2, LEFT)
        tex_scale_2 = CodeLine('mob.scale(2)').next_to(tex_shift_r2, DOWN).align_to(tex_shift_r2, LEFT)
        tex_annotation = CodeLine('# 所有对mob的变换均为瞬间完成的，\n\n'
                                  '# 但为了演示变换过程，\n\n'
                                  '# 实际执行的是将变换放入\n\n'
                                  '# self.play()后的对应动画过程', font='思源黑体 Bold', size=0.29)\
                        .next_to(tex_scale_2, DOWN).align_to(tex_scale_2, LEFT).set_color(GREEN)

        loc_02 = DOWN * 1.2
        caption_add = CodeLine('使用self.add(mob)将物体（mob）加入场景', font='思源黑体 Bold', size=0.32).to_edge(loc_02)
        caption_shift_1 = CodeLine('使用mob.shift(LEFT)将mob向左移动1个单位', font='思源黑体 Bold', size=0.32).to_edge(loc_02)
        caption_flip_1 = CodeLine('使用mob.flip()将mob翻转', font='思源黑体 Bold', size=0.32).to_edge(loc_02)
        caption_flip_2 = CodeLine('使用mob.flip()将mob再次翻转', font='思源黑体 Bold', size=0.32).to_edge(loc_02)
        caption_shift_r2 = CodeLine('使用mob.shift(RIGHT*2)将mob向右移动2个单位', font='思源黑体 Bold', size=0.32).to_edge(loc_02)
        caption_scale_2 = CodeLine('使用mob.scale(2)将mob沿自身中心放大2倍', font='思源黑体 Bold', size=0.32).to_edge(loc_02)

        self.wait()
        self.play(FadeInFromDown(tex_bg))
        self.play(Write(tex_add), Write(caption_add), run_time=1.5)
        self.add(emote)
        self.wait()

        self.play(Write(tex_shift_l), ReplacementTransform(caption_add, caption_shift_1), run_time=1.5)
        self.play(emote.shift, LEFT, run_time=1.6)
        self.wait()

        self.play(Write(tex_flip_1), ReplacementTransform(caption_shift_1, caption_flip_1), run_time=1.5)
        self.play(emote.flip, run_time=1.25)
        self.wait(0.5)
        self.play(Write(tex_flip_2), ReplacementTransform(caption_flip_1, caption_flip_2), run_time=1.5)
        self.play(emote.flip, run_time=1.25)
        self.wait()

        self.play(Write(tex_shift_r2), ReplacementTransform(caption_flip_2, caption_shift_r2), run_time=1.5)
        self.play(emote.shift, RIGHT * 2, run_time=1.6)
        self.wait()

        self.play(Write(tex_scale_2), ReplacementTransform(caption_shift_r2, caption_scale_2), run_time=1.5)
        self.play(emote.scale, 2, run_time=1.6)

        self.wait(0.4)
        self.play(Write(tex_annotation), FadeOut(caption_scale_2), run_time=4)

        self.wait(5)

class Emote_bounce_around(Scene):

    CONFIG = {
        'camera_config': {
            'background_color': WHITE,
        }
    }

    def construct(self):

        emote = Emote_new(height=3.2, plot_depth=-1, color=BLACK).shift(UP * 1.234) #.set_opacity(0.12)
        emote.emote_02.remove_updater(emote.update_emote)
        self.emote_velocity = (RIGHT * 2 + UP * 1.25) * 2.4e-2
        self.rotate_speed = 2.5 * DEGREES

        def update_emote(l, dt):
            l.shift(self.emote_velocity)
            l.rotate(self.rotate_speed, about_point=l.center_dot.get_center())
            self.emote_velocity += (RIGHT * 2 + UP * 1.25) * 2.8e-5 * np.sign(self.emote_velocity)

            if abs(l.get_center()[1]) > (FRAME_HEIGHT - l.get_height())/2:
                self.emote_velocity *= DR # or we can use self.emote_velocity[1] *= -1
                self.rotate_speed *= -1
                l.shake_on()
            if abs(l.get_center()[0]) > (FRAME_WIDTH - l.get_width())/2:
                self.emote_velocity *= UL # or we can use self.emote_velocity[0] *= -1
                self.rotate_speed *= -1
                l.shake_on()
            else:
                l.emote_02.set_opacity(l.emote_02.get_fill_opacity() - 0.02 if l.emote_02.get_fill_opacity() > 0 else 0)

        emote.add_updater(update_emote)
        self.add(emote)

        self.wait(24)





author_name = TextMobject("GTrush")
series_name = TextMobject("Python Cookbook")


class Cookbook1_2(Scene):
    def construct(self):

        title = TextMobject("1.2 从任意的可迭代对象中分解元素").next_to(series_name, DOWN)
        author_name.next_to(title, DOWN)
        self.play(Write(series_name),*[FadeInFrom(title,DOWN)],Write(author_name)) 



"""
第八周 作业 生成验证码
SWE19033 HWX
"""
import string
from PIL import Image, ImageDraw, ImageFont
from numpy import random


class Captcha:
    """
    这个一个不完善的验证码生成类
    使用 pillow 图形库进行绘制
    """
    # 宽度
    __width = 270
    # 高度
    __height = 60
    # 验证码字符集
    __char_set = list(string.digits + string.ascii_letters)
    # 生成字符个数
    __char_num = 7
    # 创建新的图片
    __code_image = Image.new("RGBA", (__width, __height), '#FFFFFF')
    # 进行绘制的画笔
    __pen = ImageDraw.Draw(__code_image)
    # 验证码字符串
    __identifying_code = ''
    # 验证码使用字体
    __fnt = ImageFont.truetype("impact.ttf", 40)

    def __init__(self, lines_number=5):
        self.__lines_number = lines_number

    def captcha(self):
        """
        产生随机字符并绘制图像

        :return: 验证码字符串， 验证码图片
        """
        self.__identifying_code = ''.join(random.choice(self.__char_set, size=self.__char_num))
        self.__image_generator()
        return self.__identifying_code, self.__code_image

    def __image_generator(self):
        """
        绘制字符，绘制干扰线，绘制噪点
        """
        self.__draw_char()
        self.__draw_lines()
        self.__draw_noise()

    def __draw_char(self):
        """
        绘制单个字符， 旋转之后进行拼接
        """
        for i in range(self.__char_num):
            char_image = Image.new("RGBA", (60, 60), '#FFFFFF')
            pen = ImageDraw.Draw(char_image)
            pen.text((15, 2), self.__identifying_code[i], font=self.__fnt, fill=self.random_color)
            char_image = char_image.rotate(random.randint(0, 360), fillcolor='#FFFFFF')
            # char_image.show()
            self.__code_image.paste(char_image, (0 + i * 45, 0, 60 + i * 45, 60))

    def __draw_lines(self):
        """
        绘制干扰线
        """
        for i in range(self.__lines_number):
            # 随机获取开始位置的坐标
            begin = (random.randint(0, 270 / 2), random.randint(0, 60))
            # 随机获取结束位置的坐标
            end = (random.randint(270 / 2, 270), random.randint(0, 60))
            self.__pen.line([begin, end], fill=self.random_color, width=3)

    def __draw_noise(self):
        """
        绘制噪点
        """
        for _w in range(270):
            for _h in range(60):
                tmp = random.randint(0, 100)
                if tmp < 20:
                    self.__pen.point((_w, _h), fill=self.random_color)

    @property
    def random_color(self):
        """
        返回一个随机RGB颜色
        :return 包含RGB，3个整数的元组
        """
        _r = random.randint(0, 255)
        _g = random.randint(0, 255)
        _b = random.randint(0, 255)
        return _r, _g, _b


code = Captcha()
code_string, image = code.captcha()
image.show()
print(code_string)

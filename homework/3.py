"""
this is a homework file for week 5
SWE19033何文鑫
"""


class MotorVeh:
    """
    这是一个模拟车辆的类
    """
    __number_plate = 'no_set_number_plate'
    __max_speed = 210
    __max_load_capacity = 12
    __current_load_capacity = 0
    __current_speed = 0

    def __init__(self, number_plate, max_speed, load_capacity):
        self.__max_speed = max_speed
        self.__number_plate = number_plate
        self.__max_load_capacity = load_capacity

    def max_load_capacity(self):
        """返回车辆的最大载重量"""
        return self.__max_load_capacity

    def current_load_capacity(self):
        """返回车辆的当前载重量"""
        return self.__current_load_capacity

    def speed_up(self, increment=1):
        """车辆加速，如超过最大速度 将 当前速度设置为车辆的最大速度"""
        if (currentSpeed := self.__current_speed + increment) <= self.__max_speed:
            self.__current_speed = currentSpeed
        else:
            self.__current_speed = self.__max_speed

    def speed_cut(self, decrement=1):
        """车辆减速，如减速之后小于0 将 当前速度设置为0"""
        if (currentSpeed := self.__current_speed - decrement) <= 0:
            self.__current_speed = 0
        else:
            self.__current_speed = currentSpeed

    def update_number_plate(self, new_number_plate):
        """更新车辆的车牌号"""
        self.__number_plate = new_number_plate

    def current_speed(self):
        """返回车辆的当前速度"""
        return self.__current_speed

    def number_plate(self):
        """返回车牌号"""
        return self.__number_plate


# car1 = MotorVeh('闽D5888', 150, 200)
# car1.speed_up(150)
# print(f'当前速度{car1.current_speed()}')
# car1.speed_cut(20)
# print(f'减速20后当前速度为：{car1.current_speed()}')


class ComplexNumber:
    """
    这是一个模拟复数类
    """
    __real = 0
    __imag = 0

    def __init__(self, real_part, imaginary_part):
        self.__real = real_part
        self.__imag = imaginary_part

    def real(self):
        """返回实部"""
        return self.__real

    def imag(self):
        """返回虚部"""
        return self.__imag

    def __add__(self, other: 'ComplexNumber'):
        """重载 + """
        return ComplexNumber((self.__real + other.real()),
                             (self.__imag + other.imag()))

    def __sub__(self, other: 'ComplexNumber'):
        """重载 - """
        return ComplexNumber((self.__real - other.real()),
                             (self.__imag - other.imag()))

    def __repr__(self):
        """重载 repr """
        result = f'{self.__real}'
        if self.__imag != 0:
            result += f'{self.__imag:+}j'
        return result


n1 = ComplexNumber(1, -3)
n2 = ComplexNumber(0, 12)
n3 = ComplexNumber()
print(n1 + n2)
print(n1 - n2)
print(n2)
print(n3)

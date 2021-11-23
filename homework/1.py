"""
this is a homework file
"""
import random
from collections import namedtuple


def str_to_float(strings):
    """将字符串转换成 浮点数，否则返回 FALSE"""
    try:
        return float(strings)
    except ValueError:
        return False


# 第一题
Prices = namedtuple('Prices', ['p01', 'p02', 'p03'], defaults=[(13, 3), (12, 2), (14, 4)])
if weight := str_to_float(input('请输入快递重量：')):  # 这里使用了自定义函数
    areaCode = input("编号01：华东地区 编号02：华南地区 编号03：华北地区\n请输入地区编号: ")
    if area := getattr(Prices(), 'p' + areaCode, False):
        print(f'快递费为: {area[0] + (0 if weight < 2 else area[1] * (weight - 2)):.1f}元')
    else:
        print('请检查收货地区是否存在 ！！！')
else:
    print('请输入合法的重量！')

# 第二题
for i in range(1, 10):
    for j in range(1, i + 1):
        print(f'{i} * {j} = {i * j}\t', end=' ') if j != i else print(f'{i} * {j} = {i * j}')

# 第三题

targetNumber = random.randint(1, 1000)
print(targetNumber)
guessTimes = 0
while True:
    guessTimes += 1
    if userAnswer := str_to_float(input("猜一猜：")):
        if userAnswer == targetNumber:
            break
        print("猜大了！") if targetNumber < userAnswer else print("猜小了！")
    else:
        print("请输入正确的 数字 ！！！")
print(f'猜对了！！！,你一共猜了 {guessTimes} 次！')

# 第四题
counter = 0
if (a := str_to_float(input('请输入a:'))) // 1 is not False and (b := str_to_float(input('请输入b:'))):
    while counter < 5 and a <= b:
        if not a % 7 or '7' in str(a):
            print(a)
            counter += 1
        a += 1
else:
    print("请输入正确的 数字 ！！！")


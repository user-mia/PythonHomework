## 2.03
## 1
# weight=eval(input('请输入快递重量（kg）：'))
# print('编号 01：华东地区','编号 02：华南地区','编号 03：华北地区',sep='\n')
# num=input('请输入地区编号：')
# if(num=='01'):
#     if(weight<=2):
#         print('快递费为13.0元')
#     else:
#         sum=13+(weight-2)*3
#         print('快递费为%0.1f元'%(sum))
# elif (num=='02'):
#     if(weight<=2):
#         print('快递费为12.0元')
#     else:
#         sum=12+(weight-2)*2
#         print('快递费为%0.1f元'%(sum))
# else:
#     if(weight<=2):
#         print('快递费为14.0元')
#     else:
#         sum=14+(weight-2)*4
#         print('快递费为%0.1f元'%(sum))

## 2
# for i in range(1,10):
#     for j in range(1,i+1):
#         print(j,' * ',i,' = ',i*j,end='\t')
#     print()

## 3
# import random
# num=random.randint(1,1000)
# cnt=1
# while 1:
#     guess=eval(input('请输入猜测数字：'))
#     if(guess<num):
#         print('很遗憾，数字猜小了！')
#         cnt+=1
#         continue
#     elif guess>num:
#         print('很遗憾，数字猜大了！')
#         cnt += 1
#         continue;
#     else:
#         print('恭喜猜对了！猜数字次数为：',cnt)
#         break

## 4
# a,b=eval(input('输入a，b数值：'))
# cnt=0
# for i in range(a,b+1):
#     t=i
#     while t:
#         if t%10==7:
#             break
#         t//=10
#     if t or i%7==0:
#         print(i,end='\t')
#         cnt+=1
#     if cnt==5:
#         break


# # 2.04
# # 1
# import random
# def get_avg(*num):  # 平均数
#     return sum(num) // len(num)
#
# def get_mid(*num):  # 中位数
#     l = sorted(num)
#     index = len(l) // 2
#     mid = l[index] if len(l) % 2 != 0 else (l[index] + l[index - 1]) / 2
#     return mid
#
# def get_mode(*num):  # 众数
#     mode = 0  # 无众数则输出0
#     max_cnt = 1
#     for i in set(num):
#         cnt = num.count(i)
#         if cnt > max_cnt:
#             mode = i
#             max_cnt = cnt
#     return mode
#
#
# t = []
# for i in range(10):
#     t.append(random.randint(1, 101))
# # print([print(item,end=' ') for item in input('数据：')],end='')
# # print('数据：',[print(item,end=' ') for item in t],end='')
# print('数据：', end='')
# for item in t:
#     print(item, end=' ')
# print()
#
# avg = get_avg(*t)
# media = get_mid(*t)
# mode = get_mode(*t)
# print('平均数：%.1f \n中位数：%.1f \n众数：%d \n' % (avg, media, mode))


# 2.05
# 1
class MotorVeh:
    __num = '闽D5888'
    __weight = 200
    speed = 150

    def info(self):
        print('车牌号：', self.__num)
        print('当前车速(km/h)：', self.speed)
        print('载重量(kg)：', self.__weight)

    def speed_up(self, up):
        self.speed += up
        print('加速后车速(km/h)：', self.speed)

    def speed_cut(self, cut):
        self.speed -= cut
        print('减速后车速(km/h)：', self.speed)

    def change_num(self, nums):
        self.__num = nums
        print('修改后车牌号：', self.__num)


car = MotorVeh()
car.info()
car.speed_cut(20)
car.change_num('6666')


# 2
class Complex:
    __real = 2
    __imag = 8
    __a = complex(__real, __imag)

    def display(self):
        if self.__real == 0:
            print('当前复数：', self.__imag, 'j')
        else:
            print('当前复数：', self.__real, '+', self.__imag, 'j')

    def get_complex(self):
        return self.__a.real, self.__a.imag

    def set_complex(self, real, imag):
        self.__real = real
        self.__imag = imag
        self.__a = complex(real, imag)
        self.display()

    def add(self, com):
        a_com = self.__a + com
        print('相加后复数：', a_com)

    def minus(self, com):
        m_com = self.__a - com
        print('相减后复数：', m_com)


num = Complex()
num.display()
com = num.get_complex()
print('实部：%d    虚部：%s' % (com[0], com[1]))
a, b = eval(input('请分别输入实部、虚部：'))
num.set_complex(a, b)
com = eval(input('请输入需要加、减运算的复数：'))
num.add(com)
num.minus(com)

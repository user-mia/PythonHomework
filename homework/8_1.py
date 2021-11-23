"""
第8周 作业 画图
SWE19033 HWX
"""
import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams['font.family'] = 'STSong'  # 修改了全局变量
matplotlib.rcParams['font.size'] = 14

course = ('数学', '英语', '语文')
score = [80, 77, 60]

plt.title("主要课程成绩")
bar = plt.bar(x=course, height=score, width=0.4)
plt.bar_label(bar)
plt.show()

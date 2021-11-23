"""
homework week-5
SWE19033何文鑫

"""
import random


def average(*seq):
    """返回序列的平均值"""
    return sum(seq) // len(seq)


def mode(*seq):
    """返回序列的众数，如果所有值都只出现一次 则 无众数"""
    temp = [(i, seq.count(i)) for i in list(set(seq))]
    max_show = max(temp, key=lambda x: x[1])[1]
    result = 0 if max_show == 1 else [item[0] for item in temp if item[1] == max_show]
    return result


def median(*seq):
    """返回一个序列的中位数"""
    seq = sorted(seq)
    half = len(seq) // 2
    return (seq[half] + seq[~half]) / 2


# 列表生成
temp2 = random.choices(range(1, 101), k=10)

print(f'随机序列为：{temp2}')
a, b, c = average(*temp2), mode(*temp2), median(*temp2)
print(f'平均数：{a}\n众数：{b}\n中位数：{c}')

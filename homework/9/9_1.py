"""
第9周 作业 加密
SWE19033 HWX
"""

import string

translation = str.maketrans(string.ascii_letters, 'bcdefghijklmnopqrstuvwxyzaBCDEFGHIJKLMNOPQRSTUVWXYZA')

with open('word_file.txt') as file:
    with open('new_file.txt', 'w') as new_file:
        new_file.write(file.read().translate(translation))

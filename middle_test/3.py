s = 'hello i am hello kitty'
temp = dict()
for i in s:
    temp.setdefault(i, 0)
    temp[i] += 1

for i, j in temp.items():
    print(i, j)

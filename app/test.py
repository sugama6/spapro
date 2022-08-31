size = 10
l = []
for i in range(0, size):
    for n in range(0, size):
        s = '丸' if i == n else '粟'
        l.append(s)
    l.append('\n')
x = ''.join(l)
print(x)




import numpy as np

x = []
size = 20
for row in np.identity(size):
    for i in row:
        s = '丸' if i == 1.0 else '粟'
        x.append(s)
    x.append('\n')
x = ''.join(x)
print(x)
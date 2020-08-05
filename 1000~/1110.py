a = str(input())
if len(a) < 2:
    a = '0' + a
b = int(a[0]) + int(a[1])
c = a[-1] + str(b)[-1]
cycle = 1
while c != a:
    b = int(c[0]) + int(c[1])
    c = c[-1] + str(b)[-1]
    cycle = cycle + 1
print(cycle)

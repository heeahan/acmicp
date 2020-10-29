a = []
for i in range(9):
    b = int(input())
    a.append(b)
print(max(a))
print(a.index(max(a)) + 1)

a = int(input())
b = list(map(int, input().split(" ")))
M = max(b)
result = []
for i in b:
    c = i/M*100
    result.append(c)
sum = 0
for i in result:
    sum = sum + i
print(sum/len(b))


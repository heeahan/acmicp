a = int(input())
inp = list(map(int, input().split()))
result = 0
for i in range(a):
    counter = 0
    for j in range(1, inp[i]+1):
        if inp[i] % j == 0:
            counter = counter + 1
    if counter == 2:
        result = result + 1
print(result)


## Here is a wrong version but cannot understand now even that I wrote this..^^ ##
# a = int(input())
# inp = list(map(int, input().split()))
# result = 0
# for i in range(a):
#     for j in range(2, inp[i]):
#         if inp[i] % j != 0:
#             result = result + 1
#             break
# print(result)

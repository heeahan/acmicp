a = int(input())
for i in reversed(range(1, a+1)):
    print(str(" "*(a-i)) + ('*'*(2*i-1)))
for i in range(2, a+1):
    print(str(" " * (a - i)) + ('*' * (2 * i - 1)))

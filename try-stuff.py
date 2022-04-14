k = 463*1024**3
n = 4
numbers = []

for i in range(n):
    numbers.insert(i, k % 1000)
    k //= 1000

numbers.reverse()
for item in numbers:
    print(item, end=' ')  
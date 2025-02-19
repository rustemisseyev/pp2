def square_generator2(a, b):
    for i in range(a, b + 1):
        yield i ** 2

x = int(input())
y = int(input())
for j in square_generator2(x, y):
    print(j, end=' ')
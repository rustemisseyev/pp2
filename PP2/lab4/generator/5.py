def reverse_generator(n):
    for i in range(n, -1, -1):
        yield i

k = int(input())
for j in reverse_generator(k):
    print(j, end=' ')
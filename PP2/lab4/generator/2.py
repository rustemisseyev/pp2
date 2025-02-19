def even_generator(n):
    for i in range(0, n + 1):
        if i % 2 == 0:
            yield i

k = int(input())
for j in even_generator(k):
    print(j, end=', ')
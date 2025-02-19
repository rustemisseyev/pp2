def generator1(n):
    for i in range(n):
        if i % 3 == 0 or i % 4 == 0:
            yield i

a = int(input())
for j in generator1(a):
    print(j, end=' ')
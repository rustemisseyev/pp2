def uniquelist(list):
    x = []
    for i in list:
        if i not in x:
            x.append(i)
    return x

print(uniquelist([1, 2, 2, 3, 4, 4, 5]))
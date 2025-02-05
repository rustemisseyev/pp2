def checkprime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def filter_prime(list):
    return [i for i in list if checkprime(i)]

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(filter_prime(numbers))
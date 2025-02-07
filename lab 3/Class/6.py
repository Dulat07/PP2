def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return 0
    return True

n = list(map(int, input("Введите числа через пробел: ").split()))

prime_num = list(filter(lambda x: is_prime(x), n))

print(f"Prime numbers : ", prime_num)

    

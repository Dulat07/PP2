def is_prime(x):
    
    if x < 2:
        return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True

def filter_prime(numbers):
   
    return list(filter(is_prime, numbers))

numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
prime_numbers = filter_prime(numbers)
print(f"Prime numbers: {prime_numbers}")
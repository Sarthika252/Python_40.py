import math

def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def check_sqrt(num):
    sqrt_num = math.sqrt(num)
    if sqrt_num.is_integer():
        sqrt_num = int(sqrt_num)
        if is_prime(sqrt_num):
            return "The square root is prime."
        elif sqrt_num % 2 == 1:
            return "The square root is odd."
        else:
            return "The square root is neither prime nor odd."
    else:
        return "The number does not have an integer square root."


num = 49
print(check_sqrt(num))
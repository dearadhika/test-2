def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

num = 25
if is_prime(num):
    print(num, "prime number")
else:
    print(num, "not prime number")
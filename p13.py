
def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

def even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"


num = int(input("Enter a number: "))


if is_prime(num):
    print(f"{num} is a Prime number.")
else:
    print(f"{num} is not a Prime number.")

print(f"{num} is {even_or_odd(num)}.")
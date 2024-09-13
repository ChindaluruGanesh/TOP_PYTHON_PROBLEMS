num = int(input('Enter a number : '))

smaller = 9

while num:
    rem = num % 10
    if smaller > rem:
        smaller = rem
    num = num // 10
print(smaller)
num = int(input('Enter a number : '))

greater = 0

while num:
    rem = num % 10
    if rem > greater:
        greater = rem
    num = num // 10

print(greater)
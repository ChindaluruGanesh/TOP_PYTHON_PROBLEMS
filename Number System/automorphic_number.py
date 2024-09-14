# A number is called an Automorphic number if and only if its square ends in the same digits as the number itself

num = int(input('Enter a number : '))
square = (num ** 2)
count = 0
while num:
    if (num % 10) != (square % 10):
        count += 1
        break
    num = num // 10
    square =  square // 10

if count == 0:
    print('Automorphic Number')
else:
    print('Not a Automorphic Number')

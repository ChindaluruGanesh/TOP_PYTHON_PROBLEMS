import math

nth_num = int(input('Enter a number : '))
count = 0
number = 2

while count < nth_num:
    if number == 2 or number == 3:
        count += 1
    elif number > 2 and number % 2 != 0:
        prime = True
        for i in range(3, int(math.sqrt(number)) + 1, 2):
            if number % i == 0:
                prime = False
                break
        if prime:
            count += 1
            if count == nth_num:
                print(number)
    number += 1

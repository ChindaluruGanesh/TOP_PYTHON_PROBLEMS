nth_num = int(input('Enter a number: '))
count = 0
number = 1

while count != nth_num:
    perfect_num = 0
    for i in range(1, number):
        if number % i == 0:
            perfect_num += i
    if perfect_num == number:
        count += 1
        if count == nth_num:
            print(number)
    number += 1
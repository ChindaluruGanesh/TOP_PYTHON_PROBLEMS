nth_num = int(input('Enter a number : '))
count = 0
number = 1
while count != nth_num:
    temp = number
    strong_num = 0
    while temp:
        rem = temp % 10
        factorial = 1
        for i in range(1,rem + 1):
            factorial *= i
        strong_num += factorial
        temp //= 10
    if strong_num == number:
        count += 1
        if count == nth_num:
            print(number)
    number += 1
    

        

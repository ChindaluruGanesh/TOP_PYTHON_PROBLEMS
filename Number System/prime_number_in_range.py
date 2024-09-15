import math

num1, num2 = map(int, input('Enter two numbers: ').split())

while num1 <= num2:
    temp = num1
    count = 0
    if temp < 2 or (temp % 2 == 0 and temp != 2):
        count += 1
    else:
        for i in range(3, int(math.sqrt(temp)) + 1, 2):
            if temp % i == 0:
                count += 1
                break
    if count == 0:
        print(temp, end=' ')
    num1 += 1

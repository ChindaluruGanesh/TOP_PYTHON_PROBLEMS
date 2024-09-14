num1 , num2 = map(int,input('Enter the range : ').split())

if num2 < 10:
    print('No armstrong number in given range of numbers')
else:
    while num1 != (num2 + 1):
        temp = num1
        count_num = 0
        temp1 = num1
        while temp:
            temp = temp // 10
            count_num += 1
        armstrong_num = 0
        while temp1:
            rem = temp1 % 10
            armstrong_num += rem ** count_num 
            temp1 =  temp1 // 10
        if num1 == armstrong_num:
            print(num1,end=' ')
        num1 += 1

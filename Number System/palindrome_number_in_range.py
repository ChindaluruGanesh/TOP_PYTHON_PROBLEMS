num1 , num2 = map(int,input('Enter a number : ').split())

for i in range(num1,num2+1):
    temp = i
    reverse_num = 0
    while temp:
        rem = temp % 10
        reverse_num = reverse_num * 10 + rem
        temp = temp // 10
    if reverse_num == i:
        print(i,end= ' ')

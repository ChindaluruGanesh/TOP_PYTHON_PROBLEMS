num1,num2 = map(int,input('Enter a number : ').split())

while num1 != num2:
    temp = num1
    sum_of_fact = 0
    for i in range(1,temp//2+1):
        if (temp % i) == 0:
            sum_of_fact += i
    if sum_of_fact == temp:
        print(temp,end=' ')
    num1 += 1






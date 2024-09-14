n1 , n2 = map(int,input('Enter 2 numbers : ').split())

sum_in_range = 0

for i in range(n1,n2+1):
    sum_in_range += i
print('Sum of numbers from',n1,'and',n2,'is',sum_in_range)
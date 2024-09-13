a , b , c = map(int,input('Enter any 3 numbers : ').split())

a = a + b + c
b = a - b - c
c = a - b - c
a = a - b - c

print(a,b,c)
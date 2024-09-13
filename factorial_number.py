num = int(input('Enter a number : '))
factorial = 1

# Method - 1
# for i in range(1,num + 1):
#     factorial *= i
# print(factorial)

# Method - 2
while num > 0:
    factorial *= num
    num -= 1
print(factorial)
first_num = int(input('Enter 1st number : '))
second_num = int(input('Enter 2nd number : '))

print()
print('first number : ',first_num)
print('second number : ',second_num)
print()
print('After swapping two numbers')
print()

# METHOD - 1
# By the help of ( + and - ) operator
# first_num = first_num + second_num
# second_num = first_num - second_num
# first_num = first_num - second_num

# METHOD - 2
# By the help of ( * and // ) operator
first_num = first_num * second_num
second_num = first_num // second_num
first_num = first_num // second_num


print('first number : ',first_num)
print('second number : ',second_num)



first_num = int(input('Enter 1st number : '))
second_num = int(input('Enter 2nd number : '))
temp = 0 # temporary variable

print()
print('first number : ',first_num)
print('second number : ',second_num)
print()
print('After swapping two numbers')
print()

# swap numbers by the help of temporary variable
temp = first_num
first_num =  second_num
second_num = temp

print('first number : ',first_num)
print('second number : ',second_num)

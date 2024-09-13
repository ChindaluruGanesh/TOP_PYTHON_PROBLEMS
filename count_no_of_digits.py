num = int(input('Enter a number : '))
count_no_of_digits = 0

while num:
    num = num // 10 
    count_no_of_digits += 1
print(count_no_of_digits)

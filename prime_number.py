num = int(input('Enter a number : '))

count = 0

# Method - 1
# if num == 0 or num == 1:
#     count += 1
# else:
#     for i in range(2,num):
#         if (num % i) == 0:
#             count += 1
#             break
#
# if count == 0:
#     print('Prime Number')
# else:
#     print('Not a prime number')

# Method - 2
# if num < 2 or (num % 2) == 0:
#     count += 1
# else:
#     for i in range(3,num//2,2):
#         if (num % i) == 0:
#             count += 1
#             break

# if count == 0:
#     print('Prime Number')
# else:
#     print('Not a prime number')

# Method - 3
# int((num ** 0.5)) --> square root of  a number
if num < 2 or (num % 2) == 0:
    count += 1
else:
    for i in range(3,int((num ** 0.5))):
        if (num % i) == 0:
            count += 1
            break
if count == 0:
    print('Prime Number')
else:
    print('Not a prime number')


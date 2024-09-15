num = int(input('Enter a number : '))

count = 0

# if num <= 1:
#     count += 1
# else:
#     for i in range(2, num):
#         if num % i == 0:
#             count += 1
#             break
#
# if count == 0:
#     print('Prime Number')
# else:
#     print('Not a prime number')

# if num < 2 or (num % 2 == 0 and num != 2):
#     count += 1
# else:
#     if num == 2:
#         count = 0  # 2 is a prime number
#     else:
#         for i in range(3,num//2,2):
#             if num % i == 0:
#                 count += 1
#                 break

# if count == 0:
#     print('Prime Number')
# else:
#     print('Not a prime number')

# Method - 3
# int((num ** 0.5)) --> square root of  a number
if num < 2 or (num % 2 == 0 and num != 2):
    count += 1
else:
    if num == 2:
        count = 0  # 2 is a prime number
    else:
        for i in range(3, int(num ** 0.5) + 1, 2):
            if num % i == 0:
                count += 1
                break
if count == 0:
    print('Prime Number')
else:
    print('Not a prime number')


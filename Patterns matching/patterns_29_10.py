# n = int(input('n: '))
# c = 0
# p = True
# for i in range(2*n-1):
#     if i < n:
#         for j in range(i+1):
#             if i % 2 == 0:
#                 print(chr(65+c),end=' ')
#                 c += 1
#                 if c > 25:
#                     c = 0
#             else:
#                 if p:
#                     print('$',end=' ')
#                     p = False
#                 else:
#                     print('*',end=' ')
#                     p = True
#         for k in range(n-i-1):
#             print(' ',end=' ')
#     else:
#         for m in range(n - (i-n+1)):
#             if i % 2 == 1:
#                 if p:
#                     print('$',end=' ')
#                     p = False
#                 else:
#                     print('*',end=' ')
#                     p = True
#             else:
#                 print(chr(65+c),end=' ')
#                 c += 1
#                 if c > 25:
#                     c = 0
#         for r in range(i-n+1):
#             print(' ',end=' ')
#     print()

# n = int(input('N: '))
# v = 1
# c = 0
# p = True
# for i in range(n):
#     for k in range(i):
#         print(' ',end=' ')
#     for j in range(2*(n-i)-1):
#         if p:
#             print(v,end=' ')
#             v += 2
#             if v > 9:
#                 v = 1
#             p = False
#         else:
#             print(chr(65+c),end= ' ')
#             p = True
#     c += 1
#     print()

# n = int(input('N : '))
# c = 0
# v = 1
# p = True
# for i in range(n):
#     for j in range(i):
#         print(' ',end=' ')
#     for k in range(n-i):
#         if p:
#             print(f' {chr(65+c)} ',end=' ')
#             c += 1
#             if c > 25:
#                 c = 0
#             p = False
#         else:
#             print(f' {v} ',end=' ')
#             v += 2
#             if v > 9:
#                 v = 1
#             p = True
#     print()

# n = int(input('N : '))
# v = 1
# c = 0
# for i in range(2*n-1):
#     if i < n:
#         for j in range(i+1):
#             if i % 2 == 0:
#                 print(chr(65+c),end=' ')
#                 c += 1
#                 if c > 25:
#                     c = 0
#             else:
#                 print(v,end=' ')
#                 v += 2
#                 if v > 9:
#                     v = 1
#         for k in range(n-i-1):
#             print(' ',end=' ')
#     else:
#         for m in range(n-(i-n+1)):
#             if i % 2 == 1:
#                 print(v,end=' ')
#                 v += 2
#                 if v > 9:
#                     v = 1
#             else:
#                 print(chr(65+c),end=' ')
#                 c += 1
#                 if c > 25:
#                     c = 0
#     print()

# n = int(input('n : '))
# c = 0
# v = 1
# p = True
# for i in range(n):
#     for j in range(n-i-1):
#         print(' ',end=' ')
#     for k in range(2*i+1):
#         if p:
#             print(v,end=' ')
#             v += 2
#             if v > 9:
#                 v = 1
#             p = False
#         else:
#             print(chr(65+c),end=' ')
#             c += 1
#             if c > 25:
#                 c = 0
#             p = True
#     print()   


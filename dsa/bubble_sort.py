# arr = [4,5,3,7,9,11,1,2,14]

# No of iterations - 64
# for i in range(len(arr)-1):
#     for j in range(len(arr)-1):
#         if arr[j+1] < arr[j]:
#             temp  = arr[j]
#             arr[j] = arr[j+1]
#             arr[j+1] = temp           
# print(arr)

# No of iterations - 36 
# Since the highest value is already sorted at the end, instead of going to that position, change the range to check the elements before it.
# for i in range(len(arr)-1):
#     for j in range(len(arr)-1-i):
#         if arr[j+1] < arr[j]:
#             temp = arr[j]
#             arr[j] = arr[j+1]
#             arr[j+1] = temp
# print(arr)

# This swap condition check is mostly used to break the loop after some iterations if the array is sorted, rather than continuing if no swaps are made.
# for i in range(len(arr) - 1):
#     swap = False
#     for j in range(len(arr) - 1 - i):
#         if arr[j + 1] < arr[j]:
#             # Swap elements
#             temp = arr[j]
#             arr[j] = arr[j + 1]
#             arr[j + 1] = temp
#             swap = True
#     if not swap:
#         break
# print(arr)

arr=[1,0,2,4,0,3,5,6,1,8]

#Time Complexity - 0(n)
# a = -1
# for i in range(len(arr)):
#     if arr[i] == 0:
#         a = i
#         break
# for j in range(a+1,len(arr)):
#     if arr[j] != 0:
#         arr[j],arr[a] = arr[a],arr[j]
#         a += 1
#         print(arr)

a = 0
for i in range(len(arr)):
    if arr[i] != 0:
        arr[a], arr[i] = arr[i], arr[a]
        a += 1
print(arr)
    


n1,n2 = map(int,(input('Enter the range : ').split()))

for i in range(n1,n2+1):
    if ( i % 2 ) == 1:
        print(i,end=' ')
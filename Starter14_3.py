t = int(input())

for i in range(t):

    n,k = map(int,input().split())

    if k==n:
        for i in range(k):
            print(i+1,end=" ")
        print("\n")
        continue

    if k>=n-1:
        print("-1")
        continue

    for i in range(k):
        print(i+1, end=" ")

    for i in range(k,n-1):
        print (i+2, end=" ")

    print(k+1)
    

T = int(input())

for i in range(T):
    N,K = map(int,input().split())

    Arr = list()
    Arr = input().split()

    mymax = max(Arr)

    indexes = [j for j in range(len(Arr)) if Arr[j] == mymax]

    count = 0
    for maxIndex in indexes:

        if ((maxIndex + 1) - K) < 0:
            loopcount = 0

        else:
            loopcount = len(Arr) - (maxIndex + 1) + 1

        count = count + loopcount
    
    print(count)

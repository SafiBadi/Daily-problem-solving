T = int(input())

for i in range(T):
    N = int(input())

    if ( (1+N) + ((N//2)+1) ) % 2 == 0:
        print(N)
    else:
        print(N-1)


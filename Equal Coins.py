t = int(input())

for i in range(t):
    x, y = map( int, input().split() )
    
    # If total value of coins is even then only it can be distributed equally
    # Total value of cons will be even or odd depends on no of 1 rupee coins only
    # So we check if x%2 == 0 -> Total value of coins is even

    if x%2 == 0:  # Check, Total value of coins is even. and x is also even. 
        if x == 0: # Edge case(0 is also even number). So, y needs to be self sufficient to be distributed equally
            if y%2 == 0:
                print("Yes")
                continue
            else:
                print("No")
                continue
        else:
            print("Yes")
            continue
    else:
        print("No")
            
T = int(input())

for i in range(T):
    Arr = list()
    Arr = input().split()

    currentSet = {Arr[0], Arr[1]}
    lang1 = {Arr[2], Arr[3]}
    lang2 = {Arr[4], Arr[5]}

    if currentSet == lang1:
        print("1")
    elif currentSet == lang2:
        print("2")
    else:
        print("0")


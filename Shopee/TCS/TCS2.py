n = int(input())
k = int(input())

avalable = n

while True:
    buy = int(input())

    if buy<= avalable - k:
        print("Sold: ",buy)

        avalable -= buy

    else:
        print("INVALID INPUT")
        break

    if avalable == k:
        avalable = n
    print("Avalable: ",avalable)


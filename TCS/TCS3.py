n = int(input())

x = 0
y = 0

distance = 10
for i in range(n):

    if i%4 == 0:
        x += distance

    elif i%4 == 1:
        y += distance

    elif i%4 ==2:
        x -= distance

    elif i%4 ==3: 
        y -= distance

    distance += 10

print(x,y)
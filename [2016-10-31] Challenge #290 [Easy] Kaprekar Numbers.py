
lis = [2,100]

test = 0
for i in range(lis[0], lis[1]):
    square = str(i**2)
    for num in square: test += int(num)
    if i == test: print(i)
    else: test = 0
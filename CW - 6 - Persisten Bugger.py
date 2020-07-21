def persistence(n):
    n = str(n)
    counter = 0
    while len(n) > 1:
        sum = 1
        for num in n:
            sum *= int(num)
        n = str(sum)
        counter += 1
    return counter

print(persistence(int(input("Num:"))))
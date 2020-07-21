def buddy(start, limit):
    for n in range(start, limit + 1):
        m = proper(n) - 1
        #print(n, m)
        if m < limit:
            if proper(m) - 1 == n:
                return n, m
    return "Nothing"

def proper(num):
    outlist = [1]
    for i in range(2, num):
        if (num / i) % 1 == 0:
            outlist.append(i)
    return sum(outlist)

print(buddy(57345, 90061))
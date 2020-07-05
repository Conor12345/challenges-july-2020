def solve(st):
    st = sorted(list(st))
    print(st)
    for letterLoc in range(len(st) - 1):
        print(st[letterLoc], st[letterLoc + 1])
        if ord(st[letterLoc]) + 1 != ord(st[letterLoc + 1]):
            return False
    return True


print(solve("abc"))
print(solve("abd"))
print(solve("dabc"))
print(solve("abbc"))
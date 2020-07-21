#https://projecteuler.net/problem=46

def primes_sieve(limit):
    limitn = limit+1
    primes = dict()
    for i in range(2, limitn): primes[i] = True

    for i in primes:
        factors = range(i,limitn, i)
        for f in factors[1:]:
            primes[f] = False
    return [i for i in primes if primes[i]==True]

max = 10000
primes = sorted(primes_sieve(max))
nummies2 = list(set(range(2, max)) - set(primes))
nummies = []
for num in nummies2:
    if num % 2 == 1:
        nummies.append(num)

found = []
for prime in primes:
    square = 1
    num = (prime + 2 * (square ** 2))
    while  num < max:
        if num not in found and num % 2 == 1:
            found.append(num)
        square += 1
        num = (prime + 2 * (square ** 2))
        #print(num, prime, square)

final = sorted(list(set(found) - set(primes)))
#print(final)
#print(nummies)
print(set(nummies) - set(final))
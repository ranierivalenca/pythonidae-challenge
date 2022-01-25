#!/usr/bin/python3

def factors(n):
    i = 2
    factors = []
    while n != 1:
        while n % i == 0:
            factors.append(i)
            n /= i
        i = i + 1 if i == 2 else i + 2
    return set(factors)

ret = factors(120)
print(ret)
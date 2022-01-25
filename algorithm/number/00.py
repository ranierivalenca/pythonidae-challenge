#!/usr/bin/python3

def gcd(
  a: int,
  b: int
) -> int:
    if min(a, b) == 0:
        return max(a, b)
    return gcd(min(a, b), max(a, b) % min(a, b))

ret = gcd(15, 27)

print(ret)
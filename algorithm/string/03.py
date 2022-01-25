#!/usr/bin/python3

from random import randint as rand

def randomBytes(
    n: int,
    s: int,
    e: int
) -> str:
    b = bytearray(n)
    b[s:e] = [rand(0, 255) for i in range(e - s)]
    return b

ret = randomBytes(10, 5, 8)
print(ret)
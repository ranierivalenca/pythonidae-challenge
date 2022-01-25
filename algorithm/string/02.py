#!/usr/bin/python3

def rewrite(
    d: str,
    s: int,
    e: int
) -> str:
    return d[:s] + 'x'*(e - s) + d[e:]

ret = rewrite('MII CyberSec Consulting Service', 4, 11)
print(ret)
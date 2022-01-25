#!/usr/bin/python3

def permute(s: str) -> str:
    if len(s) == 0:
        return ['']

    ret = []
    for i in range(len(s)):
        l = s[:i]
        r = s[i + 1:]
        [ret.append(s[i] + perm) for perm in permute(l + r)]
    return ret


ret = permute('rani')
print(ret)
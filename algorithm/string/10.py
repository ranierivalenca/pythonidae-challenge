#!/usr/bin/python3

def index_change(
  s: str,
  p: list
) -> str:
    return ''.join(s[k] for k in p)

ret = index_change(
  'MII-CyberSec',
  [4, 0, 9, 5, 6, 10, 2, 8, 1, 7, 3, 11]
)

print(ret)
assert(ret == 'CMSybeIrIe-c')
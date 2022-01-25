#!/usr/bin/python3

def xor(
  s1: str,
  s2: str
) -> bytearray:
  byte_s1 = bytes.fromhex(s1)
  byte_s2 = bytes.fromhex(s2)
  max_len = max(len(byte_s1), len(byte_s2))
  return ([hex(byte_s1[i % len(byte_s1)] ^ byte_s2[i % len(byte_s2)]) for i in range(max_len)])

ret = xor('d5577f20f541602be01c4001', '87320945')
print(ret)
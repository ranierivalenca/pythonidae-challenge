#!/usr/bin/python3

def xor(
  s1: str,
  s2: str
) -> bytearray:
  byte_s1 = bytes.fromhex(s1)
  byte_s2 = bytes.fromhex(s2)
  return ([hex(byte_s1[i] ^ byte_s2[i]) for i in range(len(byte_s1))])

ret = xor('44355050f07a7e2df0067d45', '165026358209174397283401')
print(ret)
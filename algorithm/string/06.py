#!/usr/bin/python3

def xor(
  s: str,
  c: int
) -> bytearray:
  byte_str = bytes.fromhex(s)
  return bytearray([(sc ^ c) for sc in byte_str])

ret = xor('526576657273696e672e4944', 0x53)
print(ret)
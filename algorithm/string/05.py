#!/usr/bin/python3

def decode(h:str) -> bytearray:
    # return bytes.fromhex(h)
    str_bytes = [h[i:i + 2] for i in range(0, len(h), 2)]
    b = [int(b, 16) for b in str_bytes]
    arr = bytearray(b)
    return arr

ret = decode('526576657273696e672e4944')

print(ret)
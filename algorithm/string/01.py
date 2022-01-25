#!/usr/bin/python3

def concat(u: str, e: list) -> list:
    return [u + s for s in e]

ret = concat('https://pythonidae.herokuapp.com/', [
    'web/generate',
    'web/identify',
    'web/cookies',
])
print(ret)
#!/usr/bin/python3

from re import findall

def extractUrl(s):
    return findall('http(?:s)?://.*?(?:\s|$)', s)

ret = extractUrl('hello world http://google.com and https://google.com/?q=dog and another text here http://ranierivalenca.dev')
print(ret)
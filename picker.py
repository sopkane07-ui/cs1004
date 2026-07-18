#!/usr/bin/env python3

a = int(input())
b = int(input())
c = int(input())
odd = c % 2
even = (c + 1) % 2
answer = a * even + b * odd
print(answer)

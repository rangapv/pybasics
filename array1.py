#!/usr/bin/env python
a = [2,3,4,5]
print(a)
b = []

for i in a:
    if ( i % 2) == 0:
        print(i)
        b.append(i)
print(b)


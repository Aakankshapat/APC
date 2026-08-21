a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}

res1 = a | b
res2 = a.union(b)
print(res1)
print(res2)

res3 = a & b
res4 = a.intersection(b)
print(res3)
print(res4)

res5 = a - b
res6 = a.difference(b)
print(res5)
print(res6)

res7 = a ^ b
res8 = a.symmetric_difference(b)
print(res7)
print(res8)

x = {1, 2}
y = {1, 2, 3}

print(x.issubset(y))
print(y.issuperset(x))
print(x.isdisjoint(b))

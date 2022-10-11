a = {}
a[(1,2,4)] = 8
a[(4,2,1)] = 10
a[(1,2)] = 12
sum = 0
for k in a:
    sum += a[k]
print(sum)
print(a)
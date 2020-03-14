a = [str.lower(i) for i in input().split()]
e = set(a)
for i in e:
    print (i, a.count(i))
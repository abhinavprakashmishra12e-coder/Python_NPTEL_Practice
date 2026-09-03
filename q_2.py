l1 = list(map(int,input().split()))

l2 = list(map(int,input().split()))

for x in l1:
    for y in l2:
        if x == y:
            print(x, end=' ')
def count_1(n) :
    s1 = bin(n1)[2:]
    k1 = s1.count('1')
    return k1
n1 = int(input())
L1 = [ int(x) for x in input().split()]
L2 = []
for i in range(0,n1) :
    L2.append((count_1(L1[i]),L1[i]))
L3 = sorted(L2, key=lambda x : (x[0],x[1]),reverse=True)
L4 = [x[1] for x in L3 ]
for i in range(0,len(L4)) :
    print(L4[i])

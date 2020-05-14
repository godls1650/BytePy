#print(list(n for n in range(1,100) if n%3 == 0 or n % 5 == 0))
#result = [str(i) for i in range(0,10)]
# 1 0 1 1 1 2 1 3 1 5 1 6 1 7 1 8

result = [i*j for i in range(2,10) for j in range(1,10) if j%2 ==0 ]


print(result)

dic = {i : 0 for i in range(0,10)}
for n in range(1,1001) :
    for s in str(n) : # '563'
        for c in s :  # c -> '5'  '6'  '3'
            dic[int(c)] += 1 # dic[5] += 1

print(dic)

dic2 = {i : 0 for i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'}
while True :
    s = input('Upper string > ')
    for c in s :
        dic2[c] += 1
    print(dic2)
    if s == 'exit' :
        break



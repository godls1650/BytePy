Fibo = [1,1]
count = 12
for i in range(2,count) :
    Fibo.append(Fibo[i-2] + Fibo[i-1])   
print(Fibo)
#-------------------------------------------------------------------------
numList = [15,258,71,55,2,11,168,1,25,33,85,32]
l = len(numList)
for i in range(l) :
    for j in range(l - (i+1)) :
        if numList[j] > numList[j+1] :
            numList[j] , numList[j+1] = numList[j+1] , numList[j]
            print(numList)

idx = 0
for i in range(len(numList)-1) :
    var = numList[i]
    for j in range(i+1, len(numList)) : 
        var = numList[j] if var > numList[j] else var
    idx = numList.index(var)
    numList[i], numList[idx] = numList[idx],numList[i]
    print(numList)







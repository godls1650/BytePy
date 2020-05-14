num = 10
num2 = 10

print('num의 id -> ', id(num))
print('num2의 id -> ', id(num2))
num = 100
print('num의 id -> ', id(num))
print('num2의 id -> ', id(num2))

var1 = [1,2,3,4]
print('var1 의 id-> ', id(var1))
var1.append(5)
var2 = [1,2,3,4]
print('var2 의 id-> ', id(var2))

var3 = var4 = [1,2,3,4] # 데이터 복사 방식 중 : 얕은 복사
var5 = list(var4) # int() , str() , list()  : 새로 할당 시킨다. 생성자 

var3 = var5
var3[1] = 1356246
print(var5)

a = list (b = [1,2,3,4])

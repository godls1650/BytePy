# 딕셔너리의 기본 초기화 함수
# 딕셔너리 -> key | value
#var = {'K5':[2018,480],'SM6':[2019,680],'아반떼':[2009,280]}
#print('중고 차량 검색')
#inCar = input('K5, SM6, 아반떼 > ')

#print(var[inCar])
#print(var[inCar][0] , '연식')
#print(var[inCar][1] , '만원')
# key값만 빼낸다.
# 데이터만 빼낸다.


# 사과 , 배 , 바나나를 구매하려 한다,.
# 각각의 과일의 갯수를 입력하고
# 총 얼마가 나오는지 출력하세요
#                금액               갯수 
Fruit = {'사과':[3000,0],'배':[5000,0],'바나나':[2500,0]}

counts = tuple(input('사과 , 배, 바나나 를 살 만큼 입력하세요 (쉼표로 구분)').split(','))
F_list = list(Fruit.keys())
Result = list()

Fruit[F_list[0]][1] = int(counts[0])
Fruit[F_list[1]][1] = int(counts[1])
Fruit[F_list[2]][1] = int(counts[2])

Result.append(Fruit[F_list[0]][1] * Fruit[F_list[0]][0])
Result.append(Fruit[F_list[1]][1] * Fruit[F_list[1]][0])
Result.append(Fruit[F_list[2]][1] * Fruit[F_list[2]][0])

total  = Result[0]+Result[1]+Result[2]
print("총액 > ",total)



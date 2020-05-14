# 딕셔너리 (dictionary / 사전형) 타입  {key : value}
# {식별자 : 내용} 1개의 데이터로 사용
# 식별자 ( key) 하나의 딕셔너리에 중복된 key 는 있을 수 없다.
# 내용 (value)는 중복 될 수 있다.
# dict() {}
#              사원코드   이름   생년월일 3(사원) 220만원 
employees = {1912001: ['남궁민',920817,3,2200000],
             1412013: ['박만수',871221,2,2400000],
             1201001: ['사장님', 550402,0,99999999]}

wiki = dict() 
wiki2 = {}  # tuple  ()   list []   dict {}
# 딕셔너리에 데이터 추가  : 새로 추가할 키 값으로 인덱싱
employees[1201001] = ['사장님', 550402,0,99999999]
# key만 따로 빼서 key_list라는 타입의 데이터로 변환한다.  : dict().keys()
# values만 따로 빼서 value_list 타입의 데이터로 변환한다.

key = list(employees.keys())
print(employees[key[0]][0])
print(employees[key[1]][0])
print(employees[key[2]][0])

print(1922222 in employees)
print(1912001 in employees)
# dict().values()
value = list(employees.values())
# 인덱스 연산을 활용해서 데이터를 꺼낸다.
#dict().get()
print(employees.get(2002002, 'key is not exist'))
print(employees.get(1912001))






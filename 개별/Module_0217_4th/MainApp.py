# 튜플 자료형
# 리스트 타입 : [], list() | 삭제 수정 삽입 가능
# 튜플 타입 : () , tuple() | 삭제 수정 삽입 불가능
tp = (1,)
tp2 = 1,2,3,4
lt = [1,2,3,4]

# 특정 함수의 매개변수로 여러 데이터를 전달할 때
print(lt[0:2]) # 리스트를 전달 -> 상수화 

a = 10
b = 20

a , b = 10, 20

# 데이터를 교환한다. - swap
slot = '무형검'
equip = '유성락'
#temp = ''

print(slot, equip)

slot, equip = [equip, slot]

print(slot, equip)

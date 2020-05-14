#ControlEx01
# if제어문 : 분기의 첫 기준 지점
# 노약자 0원
# 성인 : 1250원
# 중고등학생 : 860원
# 초딩 : 580원
# 애   : 0원


age = int(input('나이를 입력하세요'))
pay = 0
text = ''
metaData = {'노약자':0, '성인':1250,
            '학생' : 860, '초딩ㅋ':580, '미취학':0}
group = list(metaData.keys())
price = list(metaData.values())
#if의 제어조건 : boolean type
if age > 72:
    text, pay = '노약자', 0
elif age > 19 :
    text, pay = '성인', 1250
elif age > 13 :
    text,pay = '학생',860
elif age >= 8 :
    text, pay = '초오오오오오딩', 99999
print('%s입니다. 요금은 %d원 입니다.'%(text,pay))
    
    

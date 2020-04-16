# 서식 : 문자열의 형태 (Formatting)
# 다른 변수의 값을 문자열에 입력해서 정해진 서식을 만들어낼 때 사용

# ???는 이름을
# xxx는 키를
name = '김재민'
tall = 155
#text = '???의 키는 xxxcm 입니다.'

print(name,'의 키는',tall,'cm 입니다.')
# %를 사용한 문장은 문장 완결 이후 %에 들어갈 변수를 나열한다. 
text = '%s 의 키는 %dcm 입니다.'%(name, tall)
print(text)

# 문자열 포맷 코드 : 다른 변수의 값이 출력될 자리를 정한다. (%)
#                   출력할 형태를 정한다 (10진 정수 : d , 8진정수 : o  16진수 : x 
#                                        문자열 : s  , 실수 : f   , %문자 : % )
#
num = 255
#print 매개변수를 formatting
#숫자의 진수 표현을 추가 : %#x
print('10진수 %d 는  8진수로 : %#o'%(num,num))
print('10진수 %d 는 16진수로 : %#x'%(num,num))

#실수값 표현 : %f
pi = 3.141592
rad = 4.2
result = rad**2 * pi
print('반지름이 %f 인 원의 넓이는 %f입니다.'%(rad,result))
print('반지름이 %.2f 인 원의 넓이는 %.4f입니다.'%(rad,result))
print('반지름이 %.2f 인 원의 넓이는 %e입니다.'%(rad,result))







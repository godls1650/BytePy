age = int(input('나이 > '))
if age >= 20 :
    print('성인')
else :
    print('미성년자')
print(' 입니다.')

count = 0

while count != 111 :
    count += 1
    print('나무를 {}번 찍습니다.'.format(count))
    if count == 10 :
        print('나무가 넘어갑니다.')
        break
    

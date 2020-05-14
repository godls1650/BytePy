booklist = [['Do it 점프 투 파이썬', 15500,'이지스 퍼블리싱'],
            ['정보처리 산업기사 필기', 30000,'영진닷컴'],
            ['Java의 정석', 32000,'도우 출판']]

#가격표 tuple을 만들어서 출력하는 프로그램

# Do it 점프 투 파이썬
#            15,500원

temp = tuple(booklist[0][ : 2])
form = "{}\n{}".format(temp[0], temp[1])
print(form)

temp = tuple(booklist[1][ : 2])
form = "{}\n{}".format(temp[0], temp[1])
print(form)

temp = tuple(booklist[2][ : 2])
form = "{}\n{}".format(temp[0], temp[1])
print(form)

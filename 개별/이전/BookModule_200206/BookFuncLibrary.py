#src\BookModule_200206\BookFuncLibrary.py
class BookLst :
    def __init__(self,size = 10, title, author,company, price) :
        self.__size = 10
        self.__storage = list()
        for i in range(size) :
            self.__storage.append(title, author, company, price)

    def append(self):
        self.__storage.append(
            input('제목'),input('저자'),input('출판사'),
            int(input('가격'))
            )

var = BookLst(20,"null","null","null",0)
var.append()
        


def BookLoad(filename) :
    load = dict()
    f = open(filename, 'r')
    data = f.readlines()
    for i in range(len(data)) :
        load[i+1] = data[i].split('\t')
        load[i+1][3] = int(load[i+1][3])
    f.close()
    return load

def BookAppend(dic) :
    title = input('도서명 > ')

    author = input('저  자 > ')
    company = input('출판사 > ')
    price =  int(input('가  격 >'))
    dic[len(dic) + 1] = [title, author,company, price]







def deleteBook(dic) :
    keys = list(dic.keys())
    titles = [dic[i][0] for i in keys ]
    selector = 0
    
    print('삭제 대상 선택')
    for i in range(len(keys)) :
        print('{}. {}'.format(keys[i], titles[i]))
    selector = int(input('select > '))
    del dic[selector]



def viewBookList(dic) :
    key = list(dic.keys())
    value = list(dic.values())
    for i in range(len(key)) :
        print('{}({})'.format(value[i][0],value[i][1]))
        print('{} | {}'.format(value[i][2],value[i][3]))
        print('도서번호 : {}'.format(key[i]))





        
def ExitProgram(dic, fileName) :
    f = open(fileName, 'w')
    for i in list(dic.keys()) : 
        f.write('{}\t{}\t{}\t{}\n'.format(
            dic[i][0],dic[i][1],dic[i][2],dic[i][3]))
    f.close()









    
"""
    출력 형태

 -->
   도서명(저자)
   출판사     가격
   도서번호 : 1

[
['Do it! 점프 투 파이썬	박응용	이지스퍼블리싱	18800'],
[Do it! 데이터 분석을 위한 판다스 입문	다니엘 첸	이지스퍼블리싱	17000],
[NCS 정보처리기사 실기(2020)	NCS 정보기술 연구회	한국정보화기술	31000],
[나의 스파링 파트너	박하령	자음과모음	12000],
[퇴사하기 좋은 날	감자	42미디어콘텐츠	14800]
]

load {1:['Do it! 점프 투 파이썬',	'박응용', '이지스퍼블리싱','18800'] }

"""

#파일에 내용을 쓸 때
"""
WRITE
write : 한줄을 쓴다
writelines() : 한번에 다쓴다.


READ
read() : 파일의 내용을 하나의 문자열로 전부 읽어온다.
readline() : 파일의 내용 한줄을 읽어온다.
readlines() : 파일의 내용 한줄 한줄을 리스트의 요소로 가져온다. 
"""
#   module0421_DataIO.py
import FileLocate as fl

def loadPerson(filename):
    copy = list()
    localf = open(fl.locate(filename), 'r')
    text = localf.read()
    copy.append(text.split(':')[0])
    copy.append(int(text.split(':')[1]))
    copy.append([int(i) for i in text.split(':')[2].split('$')])
    localf.close()
    return copy

if __name__ == '__main__' :
    person = ['홍길동', 30, [10,1234,1234]]
    f = open(fl.locate('personData.txt'), 'w')
    # 각 요소마다 구분점으로 쓸 문자를 정한다.
    form = '%s:%d:%d$%d$%d'%(person[0],person[1],person[2][0],person[2][1],person[2][2])
    f.write(form)
    f.close()

    
    #파일에서 사람하나를 읽어온다.
    copy = loadPerson('personData.txt')
    print(copy)




    

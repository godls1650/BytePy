# Set type : 중복을 허용하지 않는다. / 순서가 없다.
# set Type을 생성


a = set(['apple','banana','melon'])
b = set("hello world")
#{'d', ' ', 'l', 'e', 'h', 'r', 'w', 'o'}
c = set('bed')
# 집합 연산
# 합집합, 차집합 , 교집합
print(b.intersection(c))
print(b & c)

print(b.union(c))
print(b | c)
print(b.difference(c))
print(b - c)

# 값을 추가 : add() 
# 여러 값을 추가 : update()
# 특정 값을 소멸 : remove()

# 집합 타입은   c[1] = 'a'  연산이 불가능 (원소의 수정)
c.remove('e') # --> c --> {b, d}
c.add('a') #        c --> {b,a,d}








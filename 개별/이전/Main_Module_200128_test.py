"""
*
**
***
****
*****

    *
   **
  ***
 ****
***** 

print('*',end = '')
print('')

"""

# 평균 이상의 학생들로 이루어진 B 리스트를 만들어서 B 리스트의 총점 평균을 구하세요
A = [70,60,55,70,95,90,80,85,80,100]
B = list()

total = 0
for score in A :
    total += score
average = total / len(A)
print('총점 : {} 평균 : {}'.format(total, average))
for s in A :
    if s >= average :
        B.append(s)
print(A)
print(B)
total = 0
for score in B :
    total += score
average = total/len(B)
print('총점 : {} 평균 : {}'.format(total, average))








for i in range(1, 6) :
    print('*'*i)

    
for i in range(1, 6) :
    print(' '*(5-i) + '*' * i)

# 1,1,2,3,5,8,13,21,34,55,89,144,233,...




    

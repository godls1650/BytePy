"""
탐색 알고리즘 (Searching Algorithm)
 - 순차 탐색 알고리즘
     ==> 실행의 최악의 경우
          시간 복잡도 O(n) * x회

5 

 7     6 ~ 7   4   7  5   6
                                  4 -> 5 6 
 - 이진 탐색 알고리즘        0                  9 O(nLogn)+ 정렬 시간 
    ==> 정렬된 데이터에 사용 1,2,3,4,5,<<6>>,7,<8>,9,10

분할 : 더이상 나누지 못할 때 까지 데이터를 분할 한다.
정복 : 완료에 해당하는 연산을 시행한다.

Quick Sort

"""
def LinearSearch(targetList, key) :
    index = 0
    data = 0
    bSearched = False
    for i in range(len(targetList)) :
        if key == targetList[i] :
            index = i
            data = targetList[i]
            bSearched = True
            break
        else :
            pass
    if bSearched : 
        targetList[1 : index+1] = targetList[0 : index]
        targetList[0] = data
        return index
    else :
        return -1

def BinarySearch(seq, f, l, key) :
    left = f
    right = l
    while True :
        mid = (left + right) // 2
        if seq[mid] < key :
            left = mid + 1
        elif seq[mid] > key:
            right = mid -1
        else :
            break
    return mid


if __name__ == '__main__' :
    sample = [70,90,30,10,40,80,20,50,60,100]
    sample.sort()
    print(sample)
    
    print(BinarySearch(sample, 0, 9, 70))    
        


    

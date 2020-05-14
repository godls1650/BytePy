"""
정렬 탐색 알고리즘
시퀀스에 저장된 데이터를 오름 , 내림 차순으로 재배열 한다.
데이터와 데이터를 비교해서 교환한다. : 내부정렬

버블 정렬 (Bubble Sort)

알고리즘에 대한 성능 평가
 저장공간 사용의 양에 따라서 : 공간 복잡도
 프로세스가 진행하는 동안 걸린 시간 : 시간 복잡도
   : 최소실행 최악실행횟수 의 평균
   : 최악의 실행 시간  비례
                                                      빅-오표기법 O()
   데이터 수와 비례해서 시간이 증가한다.                    O(n)
   늘어나는 데이터 수에 비해서 급격하게 시간이 증가한다.       O(n**m)
   늘어나는 데이터 수에 비해서 증가 폭이 좁은경우             O(logn)

버블 정렬 :
    작은 인덱스 부터
    
"""
def bubbleSort(seq) :
    for i in range(len(seq)-1) :
        for j in range(len(seq)-i-1) :
            if seq[j] > seq[j+1] :
                seq[j], seq[j+1] = seq[j+1], seq[j]
                print(seq)
            
def SelectionSort(seq) :
    idx = 0 
    for i in range(len(seq)-1):
        idx = i
        for j in range(i, len(seq)):
            if seq[idx] > seq[j] :
                idx = j
        if idx == i :
            continue
        
        seq[i] , seq[idx] = seq[idx], seq[i]
        print(seq)

def InsertSort(seq) :
    idx = 0 # 변경점의 인덱스를 저장
    temp = 0 # 최소값을 저장
    for i in range(len(seq)-1) : # 총 연산 횟수는 9회
        idx = i
        for j in range(i, len(seq)): # i 앞의 인덱스는 이미 연산 끝이므로 볼 필요 없음
            if(seq[idx] > seq[j]):
                idx = j
        temp = seq[j]
        seq[i+1:idx+1] = seq[i:idx]
        seq[i] = temp
        print(seq)
    

if __name__ == '__main__' :
    sample = [3,8,7,5,6,1,2,9,4,0]
    print(sample)
    InsertSort(sample)
    #bubbleSort(sample)
    

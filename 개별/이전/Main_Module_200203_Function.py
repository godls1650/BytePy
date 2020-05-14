# 함수 : 매개변수와 인수
# 파이썬 -> 작성한 모듈을 기반으로 실행  파이썬 VM 실행의 중심점이될 모듈의 이름을 변경
# Main_Module_200203_Function 모듈을 중심으로 동작한다.
# Main_Module_200203_Function 모듈의 이름을 __main__ 으로 변경한다.
# 파일 이름을 저장하는 변수 : __name__
# 기본 상태 __name__ = Main_Module_200203_Function
# 실행 상태 __name__ = __main__

from Func_Module_200203 import func

if __name__ == '__main__' :
    print('hello world')
    func(100,200)
    print('실행중인 모듈 의 __name__ : ' + __name__)

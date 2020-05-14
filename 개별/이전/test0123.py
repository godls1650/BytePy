# 지갑에 신용카드 현금 5000원 주민등록증 증명사진이 있다고 한다.
# 지출할 금액을 입력하고 입력금액이 5000원 이하면 현금지출  5000원 이상이면 신용카드 지출을
#하는 프로그램 작성

Wallet = ['신용카드', {'현금': 5000}, '주민등록증', '증명사진']

pay = int(input('지출금이 얼마입니까 ? > '))

result = Wallet[0] if pay >= Wallet[1]['현금'] else str(list(Wallet[1].keys())[0])
print('{}지출'.format(result))


















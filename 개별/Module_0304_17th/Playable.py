#user
class playable :
    def __init__(self,nickname = '', hp = 50, mp = 50, atk = 10, deff = 12):
        self.__Name = nickname
        self.__HP = hp
        self.__MP = mp
        self.__ATK = atk
        self.__DEF = deff
    def __str__(self):
        form = '이름 : %s\nHP : %d  MP : %d'%(self.__Name, self.__HP, self.__MP)
        return  form
    def Attack(self):
        return self.__ATK
    
    def Defence(self):
        return self.__DEF*2
    
    def SKILL(self) :
        return int(self.__ATK*1.20)
    def DamageCalculate(self, dmg) :
        self.__HP -= dmg
    
    #def update(self, *equip) :
       # for i in equip :
           # self.__ATK
# 동작부
myCharacter = playable(input('닉네임 > '))
Enermy = playable('적 케릭터',atk = 5, deff = 8)
damage = myCharacter.SKILL() - Enermy.Defence()

damage = damage if damage > 0 else 1
Enermy.DamageCalculate(damage)

print(myCharacter)
print(Enermy)

    










#EquipItem
class equip :
    def __init__(self, itemName, atk = 0,deff = 0,hp = 0,mp = 0):
        self.__name = itemName
        self.__atk = atk
        self.__def = deff
        self.__hp = hp
        self.__mp = mp

    def __str__(self) :
        form = """아이템 명 : %s
 아이템 옵션
atk : %d def : %d
hp  : %d  mp : %d
"""%(self.__name,self.__atk,self.__def,self.__hp,self.__mp)
        return form


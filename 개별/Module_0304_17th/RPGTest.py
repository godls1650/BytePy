from Playable import playable
from EquipItem import equip
#유저입력 
warrior = playable(input('닉네임 > '))

equipList = [equip('장검',10,0,3,0),
             equip('대검',20,-10,15,0),
             equip('방패',0,5,0,0)]

warrior.update(equipList[1])
print(warrior)


from Playable import playable as user
from Monster import monster as mon

#
Warrior = user(input('닉네임 > '))
Slime = mon('슬라임',atk = 8, deff = 10)
print(Warrior)
print(Slime)

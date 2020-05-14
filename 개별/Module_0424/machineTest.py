class Tester :
    def __init__(self):
        self.__powerLamp = False
        self.__presVoltage = 0.0
        self.__presTemp = 0.0

    def setTemp(self, newTemp) :
        self.__presTemp = newTemp

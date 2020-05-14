#Desktop\Python_개별\src\OOP_200211\MyStack.py
class Stack :
    def __init__(self, capacity = 10) :
        self.__Storage = list()
        self.__Capacity = capacity
        self.__Size = 0
    def __str__(self) :
        return '{}'.format(self.__Storage)
    def __repr__(self) :
        return self.__str__()

    def Push(self, value) :
        if self.isFull() :
            print('Stack OverFlow')
        else : 
            self.__Storage.append(value)
            self.__Size += 1
        return
    
    
    def Pop(self) :
        data = None
        if self.isEmpty() :
            print('Stack UnderFlow')
            return -1
        else :
            data = self.__Storage[self.__Size - 1]
            del self.__Storage[self.__Size - 1]
            self.__Size -= 1
            
        return data
    
    def isEmpty(self) :
        if self.__Size == 0 :
            return True
        else :
            return False
    
    def isFull(self) :
        return True if self.__Size == self.__Capacity else False

    

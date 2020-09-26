'''
面相對象的三大特性(繼承、多態、封裝)之一
把屬性和方法都隱藏起來
'''

class Person:
    __key = str(1253456)  #靜態私有屬性，只能給class內部使用
    def __init__(self,name ,passwd):
        self.name = name
        self.__passwd =passwd + self.__key     #私有屬性
    def __murmur(self):             #私有方法，只能在類內部調用
        print('{}murmurmurmur'.format(self.name))
    def speak(self):
        self.__murmur()
Jack = Person('Jackkkkk','jacky0922')
print(Jack.__dict__)
print(Jack.__dir__())
print(Jack._Person__key)
Jack.speak()
from math import pi
'''
self 為普通方法
@property(屬性方法)基礎功能為將class 函數偽裝成一個屬性
setter 可以將class的屬性作修改
deleter 可以將class的屬性作刪除
該方法的使用原因是因為對象(object)無法刪除類的屬性，必須要由類內部才能刪除
@classmethod (類方法)實現修改類固定屬性的功能
@staticmethod 如果一個函數和class 或object都沒有關係，就用之將轉換為靜態方法

'''

class Circle :
    def __init__(self,r):
        self.r = r
    @property
    def perimeter(self):
        return 2 *pi*self.r
    @property
    def area(self):
        return self.r**2*pi

circle1 =Circle(5)
print(circle1.area)
print(circle1.perimeter)

class Person:
    def __init__(self,name):
        self.__name =name
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,newname):
        self.__name =newname
    @name.deleter
    def name(self):
        del self.__name
Jack =Person('JACkkkkkkkkkkk')
print(Jack.name)
del Jack.name
Jack.name ='JACKKKKKKKKKK'
print(Jack.name)


class Product:
    __discount =0.7
    def __init__(self,price):
        self.__price =price
    def get_price(self):
        return self.__price*self.__discount
    @classmethod
    def change_discount(cls,new_discount):
        cls.__discount = new_discount
apple = Product(40)
print(apple.get_price())
Product.change_discount(0.9)
print(apple.get_price())


class Login:
    def __init__(self,name,passwd):
        self.__name = name
        self.__passwd = passwd
    def login(self):
        print('{}LOG in ing'.format(self.__name))
    @staticmethod
    def get_user_info():
        user = 'Jack'
        pwd = 'asdfasdfasdf'
        Login(user,pwd)
        print('login')
Login.get_user_info()


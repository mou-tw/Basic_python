'''
__getitem__ & __setitem__ :字典以及list倚靠此完成，靠[]觸發
__delitem__ :刪除一對象的屬性
在創建class時，所使用的init是初始化方法，而創建本身的是__new方法
ex:使用__instance私有固定屬性和__new__方法創造單例
__eq__:判斷兩者是否相等，由==觸發
__hash__:可hash()的類型必備的方法，預設是按照記憶體地址轉換，自定義hash方法，可實現訂製功能
'''

class A:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __getitem__(self, item):
        return self.__dict__[item]
    def __setitem__(self, key, value):
         self.__dict__[key]= value
    def __delitem__(self, key):
        del self.__dict__[key]

a = A('Jack',30)
a['sex'] = 'Male'
print(a['name'])
print(a['sex'])
print(a.__dict__)
del a['sex']
print(a.__dict__)

#單例
#第一次時例化的時候創建一個對象，之後再創建還是使用同一個對象

class A:
    __instance = False
    def __init__(self,name ,age):
        self.name =name
        self.age = age
    def __new__(cls, *args, **kwargs):
        if cls.__instance :
            return cls.__instance
        cls.__instance = object.__new__(A)
        return cls.__instance

aa = A('JACK',31)
print(aa)
print(aa.name)
print(aa.__dict__)
aa2 = A('AMY',15)
aa3 = A('JACK',31)
print(aa2)
print(aa2.name)
print('>>>>>'+str(id(aa)))
print('>>>>>'+str(id(aa2)))
print('>>>>>'+str(id(aa3)))

class B:
    def __init__(self,name):
        self.name = name
    def __eq__(self, other):
        if self.name == other.name:
            return True
        else:
            return False
    def __hash__(self):
        return hash(self.name +'abc')
b = B('Jack')
b2 = B('Jackk')
print(b == b2)


print(hash(aa))
print(hash(aa2))
print(hash(aa3))
print(hash(b))
print(hash(b2))




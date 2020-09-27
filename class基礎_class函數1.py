'''
__str__ & __repr__
當在python 中調用print(),str(),.format時，即在調用__str__函數，並執行內部的命令
如該class中沒有設置__str__變量，當請求時會向該calss的物件求取__str__函數，取得一個記憶體地址
當沒有設置__str__時，__repr__可替代其使用，亦可使用repr()使用之
__str__呼喚順序:
1.自己的str 2.自己的repr 3.父輩的str
repr的呼喚順序:
1.自己的repr 2.父輩的repr
__len__函數
可調用len()計算長度
也可與內置變量配合實現訂製
__del__ 析購函數
當刪除時調用
但變量超過一定量，解釋器會自動執行篩除的函數功能
__call__可呼叫函數
當一個對象加上()即實行該方法
'''


#1
class A:
    def __str__(self):
        return 'its A str'
a=A()
print(str(a))
print(a)

class B:
    pass
b=B()
print(b)

#2
class A:
    def __repr__(self):
        return 'its A repr'
a=A()
print(a)
print(repr(a))

#3
class A:
    def __len__(self):
        return 10
a =A()
print(len(a))

class Classes:
    def __init__(self,name):
        self.name =name
        self.student =[]
    def __len__(self):
        return len(self.student)
EB102 = Classes('大數據班')
print(EB102.name)
EB102.student.append('ERIC')
EB102.student.append('JUDY')
EB102.student.append('LALA')
print(len(EB102))

#4
class A:
    def __del__(self):
        print('delete NOOOOOOOO')
a =A()
del a

#5
class A:
    def __call__(self):
        print( 'CALL ME mAYBE')
a =A()()





'''
利用 isinstance & issubclass確認是否某對象是某類的對象和子類對象
getattr 取得某類、某module的屬性或者函數
通常用hasattr 單配getattr做if判斷
另用setattr &delattr做新增和刪除，但不常使用

'''

test = 6666

class Person :
    age = 50
    def func(self):
        print('Humannnnnnnnnnnn')

class Teacher(Person):
    pass

Jack = Person()
print(isinstance(Jack,Person))          #印出Jack是否為Person類對象的布林值
print(issubclass(Teacher,Person))       #印出Teacher是否為Person類的子類的布林值
print(hasattr(Jack,'age'))              #印出Jack是否有age屬性的布林值
print(getattr(Jack,'age'))              #印出Jack的age屬性值
print(getattr(Jack,'func'))             #為記憶體地址
getattr(Jack,'func')()                  #真正執行函式

import for_import_test

print(getattr(for_import_test,'test'))        #另一專案內是否有test的參數

def test_func():
    print('testttttttt')


# 反射自己
# import sys
# print(sys.modules)
# print(sys.modules['__main__'].test)
# if hasattr(sys.modules['__main__'],'test_func'):
#     getattr(sys.modules['__main__'],'test_func')()
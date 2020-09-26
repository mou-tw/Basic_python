'''
根據ID 和性別 判斷是否為同一人
'''

class Person:
    def __init__(self,id_num,name,sex,age):
        self.id_num = id_num
        self.name = name
        self.sex = sex
        self.age = age
    def __eq__(self, other):
        if hash(self.id_num)+hash(self.sex) == hash(other .id_num)+hash(other.sex):
            return True
        return False
Jack = Person(322131,'JACKKKK','Male',15)
Jack1 = Person(322131,'JACKKKkkKKKK','Male',25)
print(Jack == Jack1)


'''
組合-一個類的屬性，是另一個類的對象
好處是當一個對象的屬性發生改變，使用組合不需要另行改變，組合會連動性的改變
'''

class Hero:
    def __init__(self,*args): # *args即代表可接受多個參數的代入
        self.name = args[0]
        self.hp = args[1]
        self.mp = args[2]
        self.speed = args[3]
        self.atk = args[4]
        self.deffense = args[5]
    def attack(self,name):
        name.hp -= self.atk
    def get_weapon(self,weapon):
        self.weapon =weapon
        self.atk += weapon.attack

class Weapon:
    def __init__(self,name,attack,price):
        self.name = name
        self.attack = attack
        self.price = price
    def weapon_attack(self,person):
        person.hp -= (self.attack *2)


#實例化物件
Jack = Hero('JACKKKK',100,20,10,20,10)
Mary = Hero('MARYYYY',120,10,10,30,20)
sword = Weapon('Big Sword',20,100)

print(Jack.__dict__)

Jack.get_weapon(sword)
print(Jack.weapon)                  #為一個函式記憶體地址

Jack.attack(Mary)
print(Mary.hp)
Jack.weapon.weapon_attack(Mary)     #可使用另一class的函式
print(Mary.hp)
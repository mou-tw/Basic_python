class Hero:
    def __init__(self,hp,atk):
        self.hp = hp
        self.atk = atk
    def eat(self):
        self.hp += 20
        print('murrrrrr')
class MaleHero(Hero):
    def __init__(self,name,hp,atk):
        super().__init__(hp,atk)   #python3 新式類可使用
        self.name =name
    def eat(self):
        Hero.eat()
        if self.mussle > 0:
            self.mussle +=2
        else:
            self.mussle =2
    def attack(self,name):
        name.hp -= self.atk

class FemaleHero(Hero):
    def __init__(self,name,hp,atk,):
        super().__init__(hp,atk)
        self.name =name  #派生屬性
    def eat(self):     #派生方法
        Hero.eat()
        if self.hair > 0:
            self.hair +=2
        else:
            self.hair =2
    def get_weapon(self,weapon):
        self.weapon =weapon
        self.atk += weapon.attack
    def attack(self,name):
        name.hp -= self.atk
    def speak_lot(self):
        print('{}murrrrrrrrrrrrrrrrrrrr'.format(self.name))

class Weapon:
    def __init__(self,name,attack,price):
        self.name = name
        self.attack = attack
        self.price = price
    def weapon_attack(self,person):
        person.hp -= (self.attack *2)

Jack = MaleHero('JACKKKKK',200,40)
Mary = FemaleHero('Maryyyyy',150,50)
sword = Weapon('Big Sword',20,100)
Mary.get_weapon(sword)

Jack.attack(Mary)
print(Mary.hp)
Mary.attack(Jack)
print(Jack.hp)
print(Jack.__dict__)
Mary.weapon.weapon_attack(Jack)
print(Jack.hp)

super(FemaleHero,Mary).eat()  #使用super 調用父類的方法
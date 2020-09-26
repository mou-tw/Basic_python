#定義class屬性和class函式
class Hero:
    def __init__(self,*args):
        self.name = args[0]
        self.hp = args[1]
        self.mp = args[2]
        self.speed = args[3]
        self.atk = args[4]
        self.deffense = args[5]
    def attack(self,name):
        print('{}對{}發起了攻擊'.format(self.name,name.name))
        print('{}損失了{}血量'.format(name.name,self.atk))
        print('{}剩餘{}血量'.format(name.name,name.hp-self.atk))

Jack = Hero('JACKKKK',50,20,10,20,10)
Mary = Hero('MARYYYY',20,10,10,30,20)


Jack.attack(Mary)
print(Jack.__dict__)    #以字典方式查看實例化物件的參數
print(Hero.__dict__)    #以字典方式查看class的各參數
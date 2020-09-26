from abc import abstractmethod,ABCMeta
#為面相對象開發思想&規範
#滿足接口隔離原則，即應對應多個接口類繼承，而非單一類
'''
接口類與抽象類是在java中的代碼設計概念，目的是為了在子類中的類別中能實現父類的功能
因java代碼特性關係，本身就支持單繼承，因此自有抽象類的概念，但因為要先預宣告型態的特性，無法直接實現多繼承
因此有了接口類的概念，又為了滿足接口隔離原則，設計了接口類，以支持多繼承
python 中因為代碼為動態語言，因此支持多繼承也支持單繼承，因此接口類和抽象類的概念並不明顯，甚至沒有接口類
python 中是倚靠abc module的 metaclass=ABCMeta  和 @abstractmethod 實現抽象類

'''


class MaleHero(metaclass=ABCMeta):
    @abstractmethod
    def hit(self):pass

class FemaleHero(metaclass=ABCMeta):
    @abstractmethod
    def kiss(self):pass
class StongHero(metaclass=ABCMeta):
    @abstractmethod
    def imperialhit(self):pass
class speedHero(metaclass=ABCMeta):
    @abstractmethod
    def run(self):pass
class HumanHero(metaclass=ABCMeta):
    @abstractmethod
    def work(self):pass

class Soildier(MaleHero,StongHero,HumanHero):
    def __init__(self,name):
        self.name =name
    def hit(self,person):
        print('{} hit {}'.format(self.name,person.name))
    def imperialhit(self):
        print('HitHit')
    def work(self):
        print('work')

Jack = Soildier('Jack')
Mary = Soildier('Mary')

Jack.hit(Mary)
Jack.run()
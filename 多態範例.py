'''
因為java的特性，產生抽象類和接口類的設計，進而多態的設計會使用繼承的方式
python天生支持多態
python裡不崇尚父類約束子類(繼承的的設計模式)
python崇尚鴨子類型 -不倚靠繼承父類功能的方式，實現兩個相似類中的同名方法
ex(兩個相向的類型list &tuple類型都有len()方法，但不是使用父子類的約束方式)
'''
class LinePay:
    def pay(self,money):
        print('LinePay Pay {} Dollars'.format(money))

class ApplePay():
    def pay(self,money):
        print('ApplePay Pay {} Dollars'.format(money))

def pay(pay_way ,money):
    pay_way.pay(money)


pay(LinePay(),300)
#LinePay Pay 300 Dollars


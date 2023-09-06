# 선생님답
class Account:
    def __init__(self, ano, owner, balance):
        self.ano = ano
        self.owner = owner
        self.__balance = 0
        if 0 <= balance <= 10000000:
            self.__balance = balance
    def deposit(self, amount):
        if self.__balance + amount > 10000000:
            print('일천만원이 초과할 수 없습니다.')
            return
        self.__balance += amount
    def withdraw(self, amount):
        if self.__balance < amount:
            print('잔액이 부족합니다.')
            return
        self.__balance -= amount
    def __str__(self):
        return f'계좌번호: {self.ano}, 소유주: {self.owner}, 잔액: {self.__balance:10,d}'
    
if __name__ == '__main__':      #==>프로그램 실행되는지 확인
    acc = Account('2300906', '제임스', 100000)
    print(acc)
    acc.deposit(200000)
    print(acc)
    acc.withdraw(400000)
    acc.withdraw(250000)
    print(acc)

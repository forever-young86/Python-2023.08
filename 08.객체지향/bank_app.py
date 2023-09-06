import os, sys, joblib
import sys
import bank_util as bu
from account import Account

account_filename = 'account.jl'
if os.path.exists(account_filename):
    acc_list = joblib.load(account_filename)
else:
    acc_list = []

while True:
    try:
        menu = int(input('1:계좌생성, 2:계좌목록, 3:입금, 4:출금, 5:종료> '))
    except ValueError:      #int가 아닌것을 입력했을때
        print('잘못된 명령입니다. 1~5 사이의 숫자를 입력하세요.\n')
        continue

    if menu == 1:
        bu.creat_account(acc_list)  #계좌 생성후 acc_list에 넣는다
    elif menu == 2:
        for acc in acc_list:
            print(acc)
    elif menu == 3:
        bu.deposit(acc_list)
    elif menu == 4:
        bu.withdraw(acc_list)
    elif menu == 5:
        joblib.dump(acc_list, account_filename) #acc_list를 종료시에 account_filename에 저장
        sys.exit()      #프로그램을 빠져나간다 import sys 해야함!
    else:
        print('잘못된 명령입니다.\n')
    print()
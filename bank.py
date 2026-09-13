import json

class BankAccount:
    def __init__(self,name,money):
        self.name=name
        self.money=money
    
    def show_info(self):
        print(self.name)
        print(self.money)
        
    def deposit(self,a):
        self.money+=a
        print("Итог:",self.money)
        
    def withdraw(self,a):
        if self.money-a<0:
            print("Невозможно снять сумму")
        else:
            self.money-=a
            print("Итог:",self.money)
    
    def transfer(self,other,mon):
        if self.money<mon:
            print("Невозможно провести операцию")
        else:
            self.money-=mon
            print(self.name,self.money,sep="\n")
            other.money+=mon
            print(other.name, other.money,sep='\n')
    
def save_accounts(accounts):
    
    users=[]
    
    for i in accounts:
        
        name=i.name
        money=i.money
        
        user={
            "name":name,
            "money":money
                }
        
        users.append(user)
    
    with open("user.json","w") as file:
        json.dump(users, file)
            
def load_accounts():
    with open("user.json","r") as file:

        users=json.load(file)
        
        accounts=[]
        
        for i in users:
            account=BankAccount(i["name"],i["money"])
            accounts.append(account)
            
    return accounts

def create_account():
    name=input("Введите имя:")
    money=int(input("Введите счет:"))
    
    account=BankAccount(name,money)

    return account

accounts=[]

while True:
    try:
        load_accounts()
        break
    except FileNotFoundError:
        print("Пока аккаунтов нет, создайте свой")
        
        accounts.append(create_account())
        
        save_accounts(accounts)
        

while True:
    
    accounts=load_accounts()
    
    print("Выбирите действие:","1. увеличить баланс","2. уменьшить баланс","3. Инфо","4. создать акк","5. Перевести деньги","6. Показать аккаунты","7. Сохранить аккаунты","8. вывести сохраненные аккаунты","9. Выход",sep="\n")
    
    ans=int(input())
    #1. увеличить баланс
    if ans==1:
        while True:
            c=0
            for i in accounts:
                i.show_info()
                
            acc1=input("выберите аккаунт:")
            
            for i in accounts:
                if i.name==acc1:
                    while True:
                        try:
                            answer=int(input("Введите сумму:"))
                            i.deposit(answer)
                            c=1
                            break
                        except ValueError:
                            print("Введены неправильные данные")
                    break
            else:
                print("Аккаунт не найден")
            if c==1:
                break
                
    #2. уменьшить баланс   
    elif ans==2:
        while True:
            c=0
            for i in accounts:
                i.show_info()
            acc1=input("выберите аккаунт:")
            for i in accounts:
                if i.name==acc1:
                    while True:
                        try:
                            answer=int(input("Введите сумму:"))
                            i.withdraw(answer)
                            c=1
                            break
                        except ValueError:
                            print("Введены неправильные данные")
                    break
            else:
                print("Аккаунт не найден")
                
            if c==1:
                break
            
    #3. Инфо
    elif ans==3:
        while True:
            c=0
            for i in accounts:
                print(i.name,i.money,sep='\n')
            acc1=input("выберите аккаунт:")
            
            for i in accounts:
                if i.name==acc1:
                    i.show_info()
                    c=1
                else:
                    print("аккаунт не найден")
                    
            if c==1:
                break
    #  4. создать акк
    elif ans==4:
        while True:
            c=0
            name=input("Введите имя:")
            for i in accounts:
                if i.name==name:
                    print("Аккаунт с таким именем уже есть")
                else:
                    c=1
            if c==1:
                break
                    
        while True:
            try:
                money=int(input("Введите счет:"))
                break
            except ValueError:
                print("Введена неправильная сумма")
        
        new_account=BankAccount(name,money)
        accounts.append(new_account)
        save_accounts(accounts)
    #  5. Перевести деньги
    elif ans==5:
        if len(accounts)>1:
            
            sender=None
            receiver=None
            
            for i in accounts:
                i.show_info()
            while True:
                c=0
                acc1=input("Выберите аккаунт:")      
                acc2=input("Выберите куда перевести:")
                if acc1==acc2:
                    print("Нельзя переводить самому себе!!!","Выберите другой аккаунт",sep="\n")
                else:
                    for i in accounts:
                        if i.name==acc1:
                            sender=i
                        if i.name==acc2:
                            receiver=i
                    c=1
                if c==1:
                    break
            mon=int(input("Введите сумму перевода:"))
            
            sender.transfer(receiver,mon)
        else:
            print("Некому переводить(создайте аккаунт)")
    #6. Показать аккаунты
    elif ans==6:
        c=1

        for i in load_accounts():
            print("----",c,"----")
            i.show_info()
            c+=1
    #7. Сохранить аккаунты
    elif ans==7:
        save_accounts(accounts)
    #8. вывести сохраненные аккаунты
    elif ans==8:
        accounts=load_accounts()
        for i in accounts:
            i.show_info()
    #9. Выход
    elif ans==9:
        break
    #
    else:
        print("неправильная команда")
            
        
    
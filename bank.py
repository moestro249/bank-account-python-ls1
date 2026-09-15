import json

class BankAccount:
    def __init__(self,name,money):
        self.name=name
        self.money=money
    
    def show_info(self):
        print(self.name)
        print(self.money)
        
    def deposit(self,a):
        y=self.money
        self.money+=a
        print("Итог:",self.money)
        his={
            "Name":self.name,
            "Deposit":(self.money-y)
        }
        
        history.append(his)
            
    def withdraw(self,a):
        if self.money-a<0:
            print("Невозможно снять сумму")
        else:
            y=self.money
            self.money-=a
            print("Итог:",self.money)
            his={
                "Name":self.name,
                "Withdraw":y-self.money
            }
            
            history.append(his)
                
    def transfer(self,other,mon):
        if self.money<mon:
            print("Невозможно провести операцию")
        else:
            a=self.money
            y=other.money
            
            self.money-=mon
            print(self.name,self.money,sep="\n")
            other.money+=mon
            print(other.name, other.money,sep='\n')
            
            his={
                "Name1":self.name,
                "перевел":a-self.money,
                "Name2":other.name,
                "получил":other.money-y
            }
            
            history.append(his)          
        
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
history=[]

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
    
    print("Выбирите действие:","1. Увеличить баланс","2. Уменьшить баланс","3. Инфо","4. Создать акк","5. Перевести деньги","6. Показать аккаунты","7. Сохранить аккаунты","8. Вывести сохраненные аккаунты","9. Посмотреть историю","10. Посмтореть полную историю","11. Выход",sep="\n")
    
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
                            if answer>0:
                                i.deposit(answer)
                                save_accounts(accounts)
                                c=1
                                break
                            else:
                                print("Введена неверная сумма")
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
                            if answer>0:
                                i.withdraw(answer)
                                save_accounts(accounts)
                                c=1
                                break
                            else:
                                print("Введена неверная сумма")
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
                while True:
                    acc1=input("Выберите аккаунт:")
                    for i in accounts:
                        if i.name==acc1:
                            sender=i
                            c=2
                            break
                    else:
                        print("Такого аккаунта нет")
                    if c==2:
                        break
                                
                while True:
                    acc2=input("Выберите куда перевести:") 
                    for j in accounts:
                        if j.name==acc2:
                            receiver=j
                            c=3
                            break
                    else:
                        print("Такого аккаунта нет")
                    if c==3:
                        break
                if acc1==acc2:
                    print("Нельзя переводить самому себе!!!","Выберите другой аккаунт",sep="\n")
                else:
                    c=1
                if c==1:
                    break
            mon=int(input("Введите сумму перевода:"))
            
            sender.transfer(receiver,mon)
            save_accounts(accounts)
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
    #9. история
    elif ans==9:
        if not history:
            print("Пока ничего небыло")
        else:
            print(history)
            
    elif ans==10:
        with open("history.json","r") as file:
            for i in file:
                print(i, end='\n')
    #11. Выход
    elif ans==11:
        save_accounts(accounts)
        with open("history.json","w") as file:
            json.dump(history, file)
        break
    #
    else:
        print("неправильная команда")
            
        
    
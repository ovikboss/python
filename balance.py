class CheckBalance(object):
    Balance=0
    Time=""
    Description=""
    TyOper="income expense"
    Value=0

    def __init__(self,time:str,description:str,tyoper,value:str):
        self.Time=time
        self.Description=description
        self.Value=int(value) 
        self.TyOper=tyoper
        self.Balance+=int(value)


    def show(self,): 
       return self.Value,self.Time,self.Description,self.TyOper


def searchopertime():
    time=input("Какой время вас интересует ")
    result=[]
    for oper in operations:
        if oper.Time==time:
         result.append(oper)

    print("Всего операций ",len(result))
    for x in result:
        print(x.show())



def addOper():
   time=input("Время операции ")
   desc=input("Описание ")
   value=input("Сумма операции ")
   if int(value)>0:
       tyoper="income"
   else:
       tyoper="expense"
   operation=CheckBalance(time,desc,tyoper,value)
   operations.append(operation)


def removeOper():
    a=int(input("Какую операцию удалить"))
    for oper in operations:
        if operations.index(oper)==a:
            operations.remove(oper)
    

def showBal(List):
   result=0
   for bal in List:
      result+=bal.Balance
   return result


with open("text.txt","r")as f:
    text=""
    for t in f:
        text+=t
    f.close()
    
text=text.splitlines()
 

operations=[]


for t in text:
    operation=CheckBalance(*t.split(", "))
    operations.append((operation))




for x in operations:
    print(operations.index(x))
    print(x.show())

print(showBal(operations))


removeOper()

addOper()

with open("text.txt","w")as f:
   for oper in operations:
      f.writelines(f"{oper.Time}, {oper.Description}, {oper.TyOper}, {oper.Value} \n")

print(searchopertime())








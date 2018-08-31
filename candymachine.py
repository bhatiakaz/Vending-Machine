class CVM:
    def __init__(self,q,c,p):
        self.__q=q
        self.__p=p
        self.__c=c
    def sale(self):
        self.__q-=1
        self.__c+=self.__p
    def GetQuantity(self):
        return self.__q
    def GetPrice(self):
         return self.__p
    def GetCash(self):
        return self.__c
        

def MakeSale(c):
    price=c.GetPrice()
    print("The price is:"+str(price))
    amt=int(input("Enter the amount: "))
    if(price>amt):
        print("Transaction decline:insufficient money\n\n")
    else:
        print("Please take your food and cash....!")
        print("Cash returned:"+str(amt-price)+"\n\n")
candy=CVM(1000,0,10)
cookies=CVM(200,0,20)
chips=CVM(50,0,30)
while(1):
    print("1:Buy Candy...!")
    print("2:Buy Cookies...!")
    print("3:Buy chips...!")

    option=int(input('enter your choice: '))

    if(option==1):
        MakeSale(candy)
        candy.sale()
    elif(option==2):
        MakeSale(cookies)
        cookies.sale()
    elif(option==3):
        MakeSale(chips)
        chips.sale()

    elif(option==0):
        break
    elif(option==999):
        print('machine\t\t\tQuantity\t\tcash')
        print("Candys\t\t\t"+str(candy.GetQuantity())+"\t\t\t"+str(candy.GetCash()))
        print("Cookies\t\t\t"+str(cookies.GetQuantity())+"\t\t\t"+str(cookies.GetCash()))
        print("Chips\t\t\t"+str(chips.GetQuantity())+"\t\t\t"+str(chips.GetCash())+"\n\n")
    else:
        print("wrong choice entered..try again!!!!\n\n")
        
    
            
        

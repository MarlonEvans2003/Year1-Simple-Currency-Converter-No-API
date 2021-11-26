print("Welcome to the bank of HSDC. \n To convert £ to $ please press 1 \n To convert £ to € please press 2\n To convert £ to ¥ please press 3")

UserChoice = int(input())
Num = int(input("Please input the amount of £ you want to convert: "))

def ExchangeEuro():
    Final = Num * 1.11
    return Final
def ExchangeDollar():
    Final = Num * 1.27
    return Final
def ExchangeYen():
    Final = Num * 1.36
    return Final 

if UserChoice == 1:
    Euros = ExchangeEuro()
    print ("Your new balance is:", round(Euros,2))
elif UserChoice == 2:
    Dollars = ExchangeDollar()
    print ("Your new balance is:", round(Dollars,2))
elif UserChoice == 3:
    Yen = ExchangeYen()
    print ("Your new balance is:", round(Yen,2))
money = input("how much money do you start with: ")

growMoney = int(money)

for x in range(0, 25):

    growMoney= growMoney*.07 + growMoney + 200

    print(growMoney)
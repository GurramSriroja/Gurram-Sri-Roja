class Expense:
    def __init__(self,expense):
        self.expense=expense
    def calculate(self):
        total=sum(self.expense.values())
        maxi=max(self.expense.values())
        mini=min(self.expense.values())
        return total,maxi,mini
dicti={}
n=int(input("enter the number of items you bought:"))
for i in range(n):
    item=input("enter the name of the product:")
    price=int(input("enter the price of the product:"))
    dicti[item]=price
inputs=Expense(dicti)
total,maxi,mini=inputs.calculate()
print("/The details of your expense:/")
print("The total amount is:",total)
print("The maximum price is:",maxi)
print("The minimum price is:",mini)
print("Thank you for visiting!!,please visit again")
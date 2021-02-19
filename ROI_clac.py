

class Income():

    def __init__(self, rentalI, extraI= 0): #takes in all the variables you will need to calcuate income
        self.rentalI = rentalI
        self.extraI = extraI

    def calcIncome(self): #claculates the total income of the property
        self.income = self.rentalI + self.extraI
        return self.income

class Expenses():

    def __init__(self, tax,insurance,utilities,HOA,lsCare,vacancy,repairs,capex,management,mortgage): #takes in all the varaibles need to to calculate expenses
        self.tax = tax
        self.insurance = insurance
        self.utilities = utilities
        self.HOA = HOA
        self.lsCare = lsCare
        self.vacancy = vacancy
        self.repairs = repairs
        self.capex = capex
        self.management = management
        self.mortgage = mortgage


    def calcExpenses(self): #calculates total expenses
        self.expenses = self.tax + self.insurance + self.utilities + self.HOA + self.lsCare + self.vacancy + self.repairs + self.capex + self.management + self.mortgage
        return self.expenses 

class ROI():

    def __init__(self,downPay,closingCost,repairBudget,misc =0): #takes in all the varaibles you will need to calculate the retrun on investment
        self.downpay = downPay
        self.closingCost = closingCost
        self.repairBudget = repairBudget
        self.misc = misc

    def calcCashFlow(self,income, expenses): #calculates cash flow
        self.cashFlow = income - expenses
        return self.cashFlow    

    def totalInvestment(self): #calculates the total amount of money you put into the property 
        self.totalI = self.downpay + self.closingCost + self.repairBudget + self.misc
        return self.totalI
    
    def annualCashFlow(self): #calcluates the profit you will make in a year
        self.annualCash = self.cashFlow *12
        return self.annualCash

    def totalROI(self): #calculates your return on investment
        self.totalROI = self.annualCash / self.totalI
        self.totalROI *= 100
        return self.totalROI

class Proptery():

    def __init__(self,address,cost,type='Rental Property'): # takes in the intial information about the house
        self.address = address
        self.cost = cost
        self.type = type

    def propInfo(self):
        return f"The {self.type} you are looking to buy at {self.address} costs ${self.cost}"


class Main(): 

    def run():
        address = '8948 31st ave'
        cost = 200000
        rentalType = 'Duplex'
        duplex1 = Proptery(address, cost, rentalType)
        print(duplex1.propInfo())

        rentalIncome = 2000
        extraIncome = 0
        duplex2 = Income(rentalIncome, extraIncome)
        print(f"Your total rental income is ${duplex2.calcIncome()}")

        tax = 150
        insurance = 100
        utilities = 0
        HOA = 0
        lsCare = 0
        vacancy = 100 
        repairs = 100
        capex = 100
        management = 200
        mortgage = 860
        duplex3= Expenses(tax,insurance,utilities, HOA, lsCare, vacancy,repairs,capex,management,mortgage)
        print(f"Your total expenses are ${duplex3.calcExpenses()}")

        

        downPay = 40000
        closingCost = 3000
        repairBudget = 7000
        misc = 0
        duplex4 = ROI(downPay, closingCost,repairBudget,misc)
        print(f"Your total cash flow is ${duplex4.calcCashFlow( duplex2.calcIncome(), duplex3.calcExpenses() )}")
        print(f"Your total investment is ${duplex4.totalInvestment()}")
        print(f"Your total anual cashflow is ${duplex4.annualCashFlow()}")
        print(f"Your total anual ROI is {duplex4.totalROI()}%")









Main.run()





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

    def calcCashFlow(self): #calculates cash flow
        self.cashFlow = self.income - self.expenses
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
        return '{0:.2%}'.format(self.totalROI)

class Proptery(Income,Expenses,ROI):

    def __init__(self,address,cost,type,rentalI, extraI,tax,insurance,utilities,HOA,lsCare,vacancy,repairs,capex,management,mortgage,downPay,closingCost,repairBudget,misc): # takes in all the information about the rental property
        Income.__init__(self, rentalI, extraI)
        Expenses.__init__(self, tax,insurance,utilities,HOA,lsCare,vacancy,repairs,capex,management,mortgage)
        ROI.__init__(self,downPay,closingCost,repairBudget,misc)
        self.address = address
        self.cost = cost
        self.type = type

    def propInfo(self):
        print("=======================================================")
        print(f"The {self.type} you are looking to buy at {self.address} costs ${self.cost}")
        print(f"Your total rental income is ${self.calcIncome()}")
        print(f"Your total expenses are ${self.calcExpenses()}")
        print(f"Your total cash flow is ${self.calcCashFlow()}")
        print(f"Your total investment is ${self.totalInvestment()}")
        print(f"Your total anual cashflow is ${self.annualCashFlow()}")
        print(f"Your total anual ROI is {self.totalROI()}")


class Main(): 

    def run():
        address = input("What is the address of the property you are trying to buy? ").strip()
        cost = int(input("How much is the property you are trying to buy? ").strip())
        rentalType = input("What kind of property is it? (ex: apartment, duplex, house) ").strip()

        rentalI = int(input("How much rental income will you generate? ").strip())
        extraI = int(input("Do you have any extra income you would like to account for? ").strip())

        tax = int(input("How much will you be paying in propety taxes? ").strip())
        insurance = int(input("How much will you be paying in insurance? ").strip())
        utilities = int(input("How much will you be paying for utilities? ").strip())
        HOA = int(input("How much will you have to pay to the Home Oweners Association? ").strip())
        lsCare = int(input("How much will you pay for in lawn care or other services? ").strip())
        vacancy = int(input("How much will you set aside for vacancy? ").strip())
        repairs = int(input("How much will you set aside for repairs? ").strip())
        capex = int(input("How much will you set aside for capital expenses? ").strip())
        management = int(input("How much are you going to pay for property management? ").strip())
        mortgage = int(input("How much will your mortgage payment be? ").strip())

        downPay = int(input("How much will your down payment be? ").strip())
        closingCost = int(input("How much will the closing cost be? ").strip())
        repairBudget = int(input("How much is your repiar budget? ").strip())
        misc = int(input("Do you have miscellaneous costs you would like to account for?").strip())

        rental = Proptery(address,cost,rentalType,rentalI,extraI,tax,insurance,utilities,HOA,lsCare,vacancy,repairs,capex,management,mortgage,downPay,closingCost,repairBudget,misc)

        
        rental.propInfo()
        








Main.run()



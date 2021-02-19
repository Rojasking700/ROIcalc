

class Income():

    def __init__(self, rentalI, extraI= 0): #takes in all the variables you will need to calcuate income
        self.rentalI = int(rentalI)
        self.extraI = int(extraI)

    def calcIncome(self): #claculates the total income of the property
        self.income = self.rentalI + self.extraI
        return self.income

class Expenses():

    def __init__(self, tax,insurance,utilities,HOA,lsCare,vacancy,repairs,capex,management,mortgage): #takes in all the varaibles need to to calculate expenses
        self.tax = int(tax)
        self.insurance = int(insurance)
        self.utilities = int(utilities)
        self.HOA = int(HOA)
        self.lsCare = int(lsCare)
        self.vacancy = int(vacancy)
        self.repairs = int(repairs)
        self.capex = int(capex)
        self.management = int(management)
        self.mortgage = int(mortgage)


    def calcExpenses(self): #calculates total expenses
        self.expenses = self.tax + self.insurance + self.utilities + self.HOA + self.lsCare + self.vacancy + self.repairs + self.capex + self.management + self.mortgage
        return self.expenses 

class ROI():

    def __init__(self,downPay,closingCost,repairBudget,misc =0): #takes in all the varaibles you will need to calculate the retrun on investment
        self.downpay = int(downPay)
        self.closingCost = int(closingCost)
        self.repairBudget = int(repairBudget)
        self.misc = int(misc)

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
        return '{0:.2%}'.format(self.totalROI)

class Proptery(Income,Expenses,ROI):

    def __init__(self,address,cost,type,rentalI,extraI,tax,insurance,utilities,HOA,lsCare,vacancy,repairs,capex,management,mortgage,downPay,closingCost,repairBudget,misc): # takes in all the information about the rental property
        Income.__init__(self, rentalI, extraI)
        Expenses.__init__(self, tax,insurance,utilities,HOA,lsCare,vacancy,repairs,capex,management,mortgage)
        ROI.__init__(self,downPay,closingCost,repairBudget,misc)
        self.address = address
        self.cost = int(cost)
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

    def check(var): #checks if the in put is an integer
        try:
            if isinstance(int(var),int):
                return False
        except ValueError:
            print("Invalid input please try input a integer!")
            return True

    def run():
        
        address = input("What is the address of the property you are trying to buy? ").title().strip()
        rentalType = input("What kind of property is it? (ex: apartment, duplex, house) ").strip()
        a = True
        while a == True:
            cost = input("How much is the property you are trying to buy? ").strip()
            a = Main.check(cost)
        a = True
            

        while a == True:
            rentalI = input("How much rental income will you generate? ").strip()
            a = Main.check(rentalI)
        a = True
        while a == True:
            extraI = input("Do you have any extra income you would like to account for? ").strip()
            a = Main.check(extraI)
        a = True
        while a == True:
            tax = input("How much will you be paying in propety taxes? ").strip()
            a = Main.check(tax)
        a = True
        while a == True:
            insurance = input("How much will you be paying in insurance? ").strip()
            a = Main.check(insurance)
        a = True
        while a == True:
            utilities = input("How much will you be paying for utilities? ").strip()
            a = Main.check(utilities)
        a = True
        while a == True:
            HOA = input("How much will you have to pay to the Home Oweners Association? ").strip()
            a = Main.check(HOA)
        a = True
        while a == True:
            lsCare = input("How much will you pay for in lawn care or other services? ").strip()
            a = Main.check(lsCare)
        a = True
        while a == True:
            vacancy = input("How much will you set aside for vacancy? ").strip()
            a = Main.check(vacancy)
        a = True
        while a == True:
            repairs = input("How much will you set aside for repairs? ").strip()
            a = Main.check(repairs)
        a = True
        while a == True:
            capex = input("How much will you set aside for capital expenses? ").strip()
            a = Main.check(capex)
        a = True
        while a == True:
            management = input("How much are you going to pay for property management? ").strip()
            a = Main.check(management)
        a = True

        # b = False
        while True:
            payInFull = input("Will you be paying in full 'yes' or 'no'? ").lower().strip()
            if payInFull == 'no':
                while a == True:
                    mortgage = input("How much will your mortgage payment be? ").strip()
                    a = Main.check(mortgage)
                a = True
                while a == True:
                    downPay = input("How much will your down payment be? ").strip()
                    a = Main.check(downPay)
                a = True
                # b = False
                break
            elif payInFull == 'yes':
                mortgage = 0
                downPay = cost
                break
            else:
                print("Invalid input please enter 'yes' or 'no'" )

        while a == True:
            closingCost = input("How much will the closing cost be? ").strip()
            a = Main.check(closingCost)
        a = True
        while a == True:
            repairBudget = input("How much is your repiar budget? ").strip()
            a = Main.check(repairBudget)
        a = True
        while a == True:
            misc = input("Do you have miscellaneous costs you would like to account for?").strip()
            a = Main.check(misc)
        a = True

        rental = Proptery(address,cost,rentalType,rentalI,extraI,tax,insurance,utilities,HOA,lsCare,vacancy,repairs,capex,management,mortgage,downPay,closingCost,repairBudget,misc)

        
        rental.propInfo()
        







Main.run()


class Category:
    def __init__(self, category):
        self.category = category
        self.ledger = []

    # Operation Methods #
    def deposit(self, amount, description = ""):
        self.ledger.append({"amount": amount, "description": description})
    def get_balance(self):
        currentBalance = 0
        for i in self.ledger:
            currentBalance += i.get("amount")
        return currentBalance
    def check_funds(self, amount):
        return False if amount > self.get_balance() else True
    def withdraw(self, amount, description = ""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        else:
            return False
    def transfer(self, amount, category):
        check = self.withdraw(amount, "Transfer to " + category.category)
        if check:
            category.deposit(amount, "Transfer from " + self.category)
            return True
        else:
            return False

    # Output Formatting #
    def __str__(self):
        asterisksNum = round((30 - len(self.category)) / 2)
        asterisks = ""
        for i in range(0, asterisksNum):
            asterisks += "*"
        listPrint = ""
        for k in self.ledger:
            if len(k.get("description")) > 23:
                listPrint += k.get("description")[slice(23)]
            else:
                listPrint += k.get("description")
                for l in range (0, 23 - len(k.get("description"))):
                    listPrint += " "
            formattedAmount = "{:.2f}".format(k.get("amount"))
            for m in range (0, 7 - len(str(formattedAmount))):
                listPrint += " "
            listPrint += formattedAmount
            listPrint += "\n"
        totalPrint = "Total: " + str(self.get_balance())
        return asterisks + self.category + asterisks + "\n" + listPrint + totalPrint
        
def create_spend_chart(categories):
    # Output Calculation and Formatting #
    
    # Top Part #
    categoriesSize = len(categories)
    totalSpent = 0
    categoriesSpent = []
    for i in categories:
        tempSpent = 0
        for p in i.ledger:
            if p.get("amount") < 0:
                tempSpent += -1 * p.get("amount")
        totalSpent += tempSpent
        categoriesSpent.append(tempSpent)
    fundsPercentage = []
    for k in categoriesSpent:
        fundsPercentage.append(round((k / totalSpent) * 100))
    percentageNum = 100
    percentageString = ""
    while percentageNum >= 0:
        if percentageNum == 100:
            percentageString += "100|"
            for l in fundsPercentage:
                if l >= percentageNum:
                    percentageString += " o "
                else:
                    percentageString += "   "
        elif percentageNum == 0:
            percentageString += "  0|"
            for l in fundsPercentage:
                if l >= percentageNum:
                    percentageString += " o "
                else:
                    percentageString += "   "
        else:
            percentageString += " " + str(percentageNum) + "|"
            for l in fundsPercentage:
                if l >= percentageNum:
                    percentageString += " o "
                else:
                    percentageString += "   "
        percentageString += " \n"
        percentageNum -= 10

    # Bottom Part #
    categoryNameString = "    "
    for i in range(0, categoriesSize):
        categoryNameString += "---"
    categoryNameString += "-\n"
    longestCategoryNameLength = 0
    for h in categories:
        if len(h.category) > longestCategoryNameLength:
            longestCategoryNameLength = len(h.category)
    for w in range(0, longestCategoryNameLength):
        categoryNameString += "    "
        for j in categories:
            if w < len(j.category):
                categoryNameString += " " + j.category[w] + " "
            else:
                categoryNameString += "   "
        if w == longestCategoryNameLength - 1:
            categoryNameString += " "
        else:
            categoryNameString += " \n"
    return "Percentage spent by category\n" + percentageString + categoryNameString

class stock:
    def __init__(self, symbol, name, previousClosingPrice, currentPrice):
        self.symbol = symbol
        self.name = name
        self.previousClosingPrice = previousClosingPrice
        self.currentPrice = currentPrice

    def getName(self):
        return self.name

    def getSymbol(self):
        return self.symbol

    def getPreviousPrice(self):
        return previousClosingPrice

    def setPreviousPrice(self,previousClosingPrice):
        self.previousClosingPrice = previousClosingPrice

    def getCurrentClosingPrice(self):
        return self.currentPrice

    def setCurrentClosingPrice(self,currentPrice):
        self.currentPrice = currentPrice

    def getChangePercent(self):
        return self.previousClosingPrice - self.currentPrice

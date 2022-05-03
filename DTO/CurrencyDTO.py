from abc import ABC, abstractmethod


class CurrencyDTO(ABC):
    __private_rateBuy = 0
    __private_rateSell = 0
    __private_currencyName = ''

    def __init__(self, rateBuy, rateSell, currencyName):
        self.__private_rateBuy = rateBuy
        self.__private_rateSell = rateSell
        self.__private_currencyName = currencyName

    def __init__(self, arrayFromCurrencyController):
        self.__private_rateBuy = arrayFromCurrencyController[0]
        self.__private_rateSell = arrayFromCurrencyController[1]
        self.__private_currencyName = arrayFromCurrencyController[2]

    def getRateBuy(self):
        return self.__private_rateBuy

    def setRateBuy(self, rateBuy):
        __private_rateBuy = rateBuy

    def getRateSell(self):
        return self.__private_rateSell

    def setRateSell(self, rateSell):
        __private_rateSell = rateSell

    def getCurrencyName(self):
        return self.__private_currencyName

    def sellCurrency(self, amount):
        return self.__private_rateSell * amount

    def buyCurrency(self, amount):
        return self.__private_rateBuy * amount



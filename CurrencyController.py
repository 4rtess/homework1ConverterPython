import requests
from lxml import html


class CurrencyController:
    """Sites where program can get currency"""
    euroSite = "https://www.vbr.ru/banki/kurs-valut/prodaja-eur/"
    usdSite = "https://www.vbr.ru/banki/kurs-valut/prodaja-usd/"
    yuanSite = "https://www.vbr.ru/banki/kurs-valut/prodaja-cny/"

    def getEuroCurrency(self):
        a = self.getCurrencyFromRequet(self.euroSite, 'Евро')
        if (a != None):
            return a
        else:
            return 80, 70, 'Евро'

    def getUsdCurrency(self):
        a = self.getCurrencyFromRequet(self.usdSite, 'Доллар')
        if (a != None):
            return a
        else:
            return 70, 60, 'Доллар'

    def getYuanCurrency(self):
        a = self.getCurrencyFromRequet(self.yuanSite, 'Юань')
        if(a!=None):
             return a
        else:
            return 15,10,'Юань'

    def getCurrencyFromRequet(self, site, currencyName):
        try:
            response = requests.get(site)
            parser_tree = html.fromstring(response.content)
            sellAndBuyRate = parser_tree.xpath("//td[@class='rates-val']/b[@data-quick-converter-rate]")
            sellRate = sellAndBuyRate[0].text.replace(",", ".")
            buyRate = sellAndBuyRate[1].text.replace(",", ".")
            return float(buyRate), float(sellRate), currencyName
        except:
            return None

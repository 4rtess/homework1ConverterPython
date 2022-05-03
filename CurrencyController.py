import requests
from lxml import html

class CurrencyController:
    """Sites where program can get currency"""
    euroSite = "https://www.vbr.ru/banki/kurs-valut/prodaja-eur/"
    usdSite = "https://www.vbr.ru/banki/kurs-valut/prodaja-usd/"
    yuanSite = "https://www.vbr.ru/banki/kurs-valut/prodaja-cny/"

    def getEuroCurrency(self):
        return self.getCurrencyFromRequet(self.euroSite, 'Евро')

    def getUsdCurrency(self):
        return self.getCurrencyFromRequet(self.usdSite, 'Доллар')

    def getYuanCurrency(self):
        return self.getCurrencyFromRequet(self.yuanSite, 'Юань')

    def getCurrencyFromRequet(self, site, currencyName):
        response = requests.get(site)
        parser_tree = html.fromstring(response.content)
        sellAndBuyRate = parser_tree.xpath("//td[@class='rates-val']/b[@data-quick-converter-rate]")
        sellRate = sellAndBuyRate[0].text.replace(",", ".")
        buyRate = sellAndBuyRate[1].text.replace(",", ".")
        return float(buyRate), float(sellRate), currencyName



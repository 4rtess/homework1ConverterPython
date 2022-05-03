from tkinter import *
import tkinter.messagebox as messagebox

from CurrencyController import CurrencyController
from DTO.EuroDTO import EuroDTO
from DTO.UsdDTO import UsdDTO
from DTO.YuanDTO import YuanDTO

# я не хочу комментировать то что снизу, я ненавижу писать gui, потому что в жабе это мертвая тема
# во-вторых, динамическая типизация мне вообще не нравится
# в-третьих, где нормальный интерфейсы, почему так ущербно модификаторы доступа присваиваются
# в-четвертых, на жабе это выглядило бы более лаконично, не нужно аксессоры писать, т.к. есть библиотека lombok
# короче gui - максимальный костыль

# ну и еще можно добавить округление, но мне очень лень!!! задание сделано

currencyController = CurrencyController()
usd = UsdDTO(currencyController.getUsdCurrency())
euro = EuroDTO(currencyController.getEuroCurrency())
yuan = YuanDTO(currencyController.getYuanCurrency())

root = Tk()

def convertCurrency():

    amountBuyUsd = str(inputBuyUsd.get())
    amountSellUsd = str(inputSellUsd.get())

    amountBuyEuro = str(inputBuyEuro.get())
    amountSellEuro = str(inputSellEuro.get())

    amountBuyYuan = str(inputBuyYuan.get())
    amountSellYuan = str(inputSellYuan.get())

    message = ''

    if(amountBuyUsd!=''):
        message+= 'Покупка ' + amountBuyUsd + ' долларов обойдется в ' + str(usd.buyCurrency(float(amountBuyUsd))) + ' руб\n'

    if(amountSellUsd!=''):
        message += 'Продажа ' + amountSellUsd + ' долларов обойдется в ' + str(usd.sellCurrency(float(amountSellUsd))) + '  руб\n'

    if (amountBuyEuro != ''):
        message += 'Покупка ' + amountBuyEuro + ' евро обойдется в ' + str(euro.buyCurrency(float(amountBuyEuro))) + '  руб\n'

    if (amountSellEuro != ''):
        message += 'Продажа ' + amountSellEuro + ' евро обойдется в ' + str(euro.sellCurrency(float(amountSellEuro))) + '  руб\n'

    if (amountBuyYuan != ''):
        message += 'Покупка ' + amountBuyYuan + ' юань обойдется в ' + str(yuan.buyCurrency(float(amountBuyYuan))) + '  руб\n'

    if (amountSellYuan != ''):
        message += 'Продажа ' + amountSellYuan+ ' юань обойдется в ' + str(yuan.sellCurrency(float(amountSellYuan))) + '  руб\n'

    messagebox.showinfo(title='Сколько придется заплатить', message=message)



root.title('Конвертер валют')
root.geometry('500x500')

canvas = Canvas(root, height=500, width=250)
canvas.pack()

frame = Frame(root, bg='white')
frame.place(relwidth=1, relheight=1)
#title = Label(frame, text='Купить USD', bg='white')
#title.pack()
#usdInput = Entry(frame, bg='white')
#usdInput.pack()
#btn = Button(frame, text='Перевести', bg='gray', command=buyUsd)
#btn.pack()

labelBuyUsd = Label(frame, text = 'Купить один доллар: %s' % usd.getRateBuy(), bg='white')
inputBuyUsd = Entry(frame, bg='white')
labelSellUsd = Label(frame, text = 'Продать один доллар: %s' % usd.getRateSell(), bg='white')
inputSellUsd = Entry(frame, bg='white')
labelBuyUsd.pack()
inputBuyUsd.pack()
labelSellUsd.pack()
inputSellUsd.pack()

Label(frame, bg='white').pack()

labelBuyEuro = Label(frame, text = 'Купить один евро: %s' % euro.getRateBuy(), bg='white')
inputBuyEuro = Entry(frame, bg='white')
labelSellEuro = Label(frame, text = 'Продать один евро: %s' % euro.getRateSell(), bg='white')
inputSellEuro = Entry(frame, bg='white')
labelBuyEuro.pack()
inputBuyEuro.pack()
labelSellEuro.pack()
inputSellEuro.pack()

Label(frame, bg='white').pack()

labelBuyYuan = Label(frame, text = 'Купить один юань: %s' % yuan.getRateBuy(), bg='white')
inputBuyYuan = Entry(frame, bg='white')
labelSellYuan = Label(frame, text = 'Продать один юань: %s' % yuan.getRateSell(), bg='white')
inputSellYuan = Entry(frame, bg='white')
labelBuyYuan.pack()
inputBuyYuan.pack()
labelSellYuan.pack()
inputSellYuan.pack()

btn = Button(frame, text='Перевести', bg='gray', command=convertCurrency)
btn.pack()

root.mainloop()

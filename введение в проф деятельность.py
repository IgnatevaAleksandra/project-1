import datetime
import time 
import threading
print("Здравствуйте! Введите наименование вашего продукта.")
product = input()
print("Если у вас есть дата окончания срока годности введите 1, если у вас есть количество месяцев после вскрытия товара введите 2.")
n = int(input())
segodnya = datetime.datetime.today()
if n == 1:
    print("Введите дату в формате дд.мм.гггг")
    print("Введите день")
    a = int(input())
    print("Введите месяц")
    b = int(input())
    print("Введите год")
    c = int(input())
    data = datetime.datetime(c, b, a)
    x = data - segodnya
    x1 = x.total_seconds() 
    print(x1)
    print(data.strftime("%d. %m. %Y"),"Я напомню вам, что следует утилизировать", product, ".")
    def g():
        print("Пора выкинуть", product)
    timer = threading.Timer(x1, g)
    timer.start()
elif n == 2:
    print("Введите количество месяцев")
    m = int(input())
    if m + segodnya.month < 12:
        data = segodnya.replace(month = segodnya.month + m)
        x = data - segodnya
        x1 = x.total_seconds() 
        print(x1)
        print(data.strftime("%d. %m. %Y"),"Я напомню вам, что следует утилизировать", product, ".")
        def g():
            print("Пора выкинуть", product)
        timer = threading.Timer(x1, g)
        timer.start()
    else:
        ost1 = int(m % 12)
        ost2 = int((ost1 + segodnya.month) % 12)
        cel3 = int((ost1 + segodnya.month) // 12)
        cel4 = int(m // 12)
        if ost1 + segodnya.month < 12:
            data = segodnya.replace(month = segodnya.month + ost1)
            data = data.replace(year = data.year + cel3 + cel4)
            x = data - segodnya
            x1 = x.total_seconds() 
            print(x1)
            print(data.strftime("%d. %m. %Y"),"Я напомню вам, что следует утилизировать", product, ".")
            def g():
                print("Пора выкинуть", product)
            timer = threading.Timer(x1, g)
            timer.start()
        else:
            ost5 = 12 - ost1
            data = segodnya.replace(month = segodnya.month - ost5)
            print(data)
            data = data.replace(year = data.year + cel3 + cel4)
            x = data - segodnya
            x1 = x.total_seconds() 
            print(x1)
            print(data.strftime("%d. %m. %Y"),"Я напомню вам, что следует утилизировать", product, ".")
            def g():
                print("Пора выкинуть", product)
            timer = threading.Timer(x1, g)
            timer.start()

else:
    print("ОШИБКА")




        
        
    





















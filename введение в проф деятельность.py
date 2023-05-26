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
    m1 = segodnya.month + m
    if m1 >= 12:
        m2 = m1 // 12
        m3 = m1 % 12
        r = segodnya.replace(month = segodnya.month + m3)
        r2 = r.replace(year = r.year + m2)
        if m < 12:
            r2 = r2.replace(month = r2. month - segodnya.month)
            print(r2)
        else:
            print(r2)
        r3 = r2 - segodnya
        r4 = r3.total_seconds()
        print (r4)
        print(r2.strftime("%d. %m. %Y"),"Я напомню вам, что следует утилизировать", product, ".")
        def g():
            print("Пора выкинуть", product)
        timer = threading.Timer(r4, g)
        timer.start()
    elif m1 < 12:
        r = segodnya.replace(month = segodnya.month + m)
        print(r)
        r2 = r - segodnya
        r3 = r2.total_seconds()
        print(r3)
        print(r.strftime("%d. %m. %Y"),"Я напомню вам, что следует утилизировать", product, ".")
        def g():
            print("Пора выкинуть", product)
        timer = threading.Timer(r3, g)
        timer.start()
else:
    print("ОШИБКА")

        
        
    





















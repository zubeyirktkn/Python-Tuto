#errors

# print(a)#NameError
# int("1a2")#ValueError
# print(10/0) #ZeroDivisonError
# print("denem"e)#SyntaxError

#error handling
while True:
    try:
        x = int(input("x:"))
        y = int(input("y:"))
        print(x/y)
    # except (ZeroDivisionError,ValueError):
    #     print("Yanlış input!")

    # except ValueError:
    #     print("sayı gircen sayı düzgün bas şu tuşlara")

    except Exception as ex:
        print("Yanlış input!",ex)

    else:#except çalışmazsa çalışır sadece
       break
    finally:#her zaman çalışır
        print("try except sonlandı")

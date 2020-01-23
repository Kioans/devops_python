def stringToNumber():
    s = input()
    if s == "cancel":
        print("Bye")
        return ()
    else:
        try:
            i = int(s)
            x = int(i/2) if i % 2 == 0 else  i * 3 + 1
            print(x)
        except:
            print("Не удалось преобразовать введенный текст в число.")
        finally:
            stringToNumber()

stringToNumber()
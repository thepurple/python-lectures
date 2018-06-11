def test(b):
    try:
        a = b[0]
    except TypeError:
        # Если не сработал try и объявлена ошибка Error
        print("except NameError")
    else:
        print("else")
        # Если сработал try и не сработал except
    finally:
        # Выполняется в любом случае
        print("finally")


print("*** TRY IS OK ***")
test("test")
print("*** TRY IS FAILED ***")
test(1)
и
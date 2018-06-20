from concurency import coroutine, sleep, run


@coroutine
def hello(name, timeout):
    while True:
        yield from sleep(timeout)
        print("Привет, {}!".format(name))


hello("Петров", 2.0)
hello("Иванов", 3.0)
hello("Мир", 5.0)
run()

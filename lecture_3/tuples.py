def test(tpl):
    if not isinstance(tpl, tuple):
        raise Exception("Type is not tuple")
    print(type(tpl), tpl)


####################
try:
    test(1, 2, 3, 4)
except Exception as e:
    print(e)

t = (1, 2, 3, 4)
test(t)

test((1, 2, 3, 4))

####################
try:
    test(1)
except Exception as e:
    print(e)
test((1, ))

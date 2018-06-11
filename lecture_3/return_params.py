def test_tuple():
    x1 = 1
    x2 = 2
    y1 = 1
    y2 = 2
    return x1, y1, x2, y2


a = test_tuple()
print("Tuple")
print(test_tuple())
print(f"type a: {type(a)}")

x1, y1, x2, y2 = test_tuple()
print(f"({x1}, {y1}) - ({x2}, {y2})")
print("type x1: {}", type(x1))


def test_dict():
    x1, y1 = 1, 1
    x2, y2 = 2, 2
    return {"x1": x1, "y1": y1, "x2": x2, "y2": y2}


print("Dictionary")
a = test_dict()
print(test_dict())
print(f"type a: {type(a)}")

x1, y1, x2, y2 = test_dict()
print(f"({x1}, {y1}) - ({x2}, {y2})")
print("type x1: {}", type(x1))

print(f"({a['x1']}, {a['y1']}) - ({a['x2']}, {a['y2']})")
print("type a['x1']: {}", type(a['x1']))

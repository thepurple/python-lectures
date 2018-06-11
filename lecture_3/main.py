def test(tpl):
    if not isinstance(tpl, tuple):
        raise Exception("Type is not tuple")
    print(type(tpl), tpl)


if __name__ == "__main__":
    import sys
    test(tuple(sys.argv[1:]))

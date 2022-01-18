import sys


def func(a, b):
    return a + b


if __name__ == '__main__':
    args = sys.argv
    if len(args) >= 2:
        a = args[1]
        b = args[2]
        print(f"a={a}")
        print(f"b={b}")
        c = func(a,b)
        print(f"add(a,b)={c}")
    else:
        print("usage: cmd a b")

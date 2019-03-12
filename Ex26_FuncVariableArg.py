
def add(*args):
    print(type(args))
    print(args)
    result = 0
    for x in args:
        result += x
    return result

def main():
    print(add(1, 2))
    print(add(100, 200, 300))
    print(add(10, 20, 30, 40))

if __name__ == '__main__':
    main()
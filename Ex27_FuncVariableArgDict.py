
def VariableArgDictionary(a, b, *args, **kwargs):
    print(a, b)
    print(type(args), type(kwargs))
    for x in args:
        print(x)
    for x in kwargs:
        print(x, kwargs[x])

def main():
    VariableArgDictionary(10, 20, 1, 2, 3, 4, 5, 6, 7, name="Akshay", hobby="Wildlife")

if __name__ == '__main__':
    main()
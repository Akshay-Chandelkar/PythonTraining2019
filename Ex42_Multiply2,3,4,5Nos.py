
def Mul(a, b, c=1, d=1, e=1):
    return a*b*c*d*e


def main():
    res = Mul(10,20)
    print("The multiplication of two numbers :: {}".format(res))
    res = Mul(10, 20, 30)
    print("The multiplication of three numbers :: {}".format(res))
    res = Mul(10, 20, 30, 40)
    print("The multiplication of four numbers :: {}".format(res))
    res = Mul(10, 20, 30, 40, 50)
    print("The multiplication of five numbers :: {}".format(res))

if __name__ == '__main__':
    main()
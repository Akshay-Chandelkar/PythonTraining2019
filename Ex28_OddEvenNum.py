
def IsOdd(N1):
    if(N1 % 2 == 0):
        return False
    else:
        return True

def main():
    N1 = int(input("Enter a number to find if it is odd ::"))
    print("The number is odd :: {}".format(IsOdd(N1)))

if __name__ == '__main__':
    main()

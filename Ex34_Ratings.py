
def Ratings(name,N1):
    if N1 == 5:
        print("The employee {}'s rating {} is Exceptional.".format(name, N1))
    elif N1 >= 4 and N1 < 5:
        print("The employee {}'s rating {} is Excellent.".format(name, N1))
    elif N1 >= 3 and N1 < 4:
        print("The employee {}'s rating {} is Good.".format(name, N1))
    elif N1 >=2 and N1 < 3:
        print("The employee {}'s rating {} is Needs improvement.".format(name, N1))
    else:
        print("The employee {}'s rating {} is Poor.".format(name, N1))


def main():
    name,N1 = eval(input("Please enter the Employee Name and Rating :: "))
    Ratings(name,N1)

if __name__ == '__main__':
    main()
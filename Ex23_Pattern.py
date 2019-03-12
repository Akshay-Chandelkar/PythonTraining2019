
def Pattern1(n):
    for i in range(1, n+1):
        for j in range(1, i+1):
            print("*\t" , end='')
        print("\n")

def Pattern2(n):
    for i in range(1, n+1):
        for j in range(1, n+1-i):
            print("\t", end='')
        for j in range(1, i+1):
            print("*\t", end='')
        print("\n")

def Pattern3(n):
    for i in range(1, n+1):
        for j in range(1, n+1-i):
            print("\t", end='')
        for j in range(1, i*2):
            print("*\t", end='')
        print("\n")

def Pattern4(n):
    for i in range(1, n+1):
        for j in range(1, n+1-i):
            print("\t", end='')
        x = i
        for j in range(1, i*2):
            print(x, "\t", end='')
            if j < i:
                x = x - 1
            else:
                x = x + 1

        print()

def Pattern5(n):
    for i in range(1, n+1):
        for j in range(n-i, n):
            print("\t", end='')
        for k in range(1, n+2-i):
            print("*\t", end='')
        print("\n")

def Pattern6(n):
    for i in range(1, n+1):
        for j in range(1, n+2-i):
            print("*\t", end='')
        for j in range(1, i+1):
            print("\t", end='')
        print("\n")

def Pattern7(n):
    for i in range(1, n+1):
        for j in range(1, n+1-i):
            print("\t", end='')
        x = i
        for j in range(1, i*2):
            print(chr(x+64), "\t", end='')
            if j < i:
                x = x - 1
            else:
                x = x + 1
        print("\n")

def Pattern8(n):
    for i in range(1, n+1):
        for j in range(1, n+1-i):
            print("\t", end='')
        for j in range(1, i*2):
            print("*\t", end='')
        print("\n")
    for i in range(1, n+1):
        for j in range(1, i+1):
            print("\t", end='')
        for j in range(1, (n-i)*2):
            print("*\t", end='')
        print("\n")

def Pattern9(n):
    for i in range(1, n+1):
        for j in range(1, n+2-i):
            print("*\t", end='')
        for j in range(n-i+1, n):
            print("\t", end='')
        for j in range(1, i):
            print("\t", end='')
        for j in range(1, n+2-i):
            print("*\t", end='')
        print("\n")

def Pattern10(n):
    for i in range(1, n+1):
        for j in range(1, n+2-i):
            print("*\t", end='')
        for j in range(n-i+1, n):
            print("\t", end='')
        for j in range(1, i):
            print("\t", end='')
        for j in range(1, n+2-i):
            print("*\t", end='')
        print("\n")
    for i in range(1, n):
        for j in range(1, i+2):
            print("*\t", end='')
        for j in range(1, n-i):
            print("\t", end='')
        for j in range(1, n-i):
            print("\t", end='')
        for j in range(1, i+2):
            print("*\t", end='')
        print("\n")

def Pattern11(n):
    for i in range(1, n+1):
        for j in range(1, i+1):
            x = j
            print(chr(x+64),"\t",end = '')
            if j < i:
                x = x - 1
            else:
                x = x + 1
        print("\n")

def Menu():
    while True:
        print(" 1. Pattern1\n 2. Pattern2\n 3. Pattern3\n 4. Pattern4\n 5.Pattern5\n 6. Pattern6\n 7. Pattern7\n 8. pattern8\n 9. Pattern9\n 10. pattern10\n 11. pattern11\n 12. Exit ")
        choice = int(input("Enter a choice :: "))
        if choice > 0 and choice < 13:
            return choice
        else:
            print("Enter a valid choice.")

def DrawPatterns(n):
    choice = 0
    while choice != 12:
        choice = Menu()
        if choice == 1:
            Pattern1(n)
        elif choice == 2:
            Pattern2(n)
        elif choice == 3:
            Pattern3(n)
        elif choice == 4:
            Pattern4(n)
        elif choice == 5:
            Pattern5(n)
        elif choice == 6:
            Pattern6(n)
        elif choice == 7:
            Pattern7(n)
        elif choice == 8:
            Pattern8(n)
        elif choice == 9:
            Pattern9(n)
        elif choice == 10:
            Pattern10(n)
        elif choice == 11:
            Pattern11(n)
        elif choice == 12:
            break
        else:
            Menu()






def main():
    n = int(input("Enter the number of rows for the pattern :: "))
    DrawPatterns(n)
    '''
    Pattern1(n)
    Pattern2(n)
    Pattern3(n)
    Pattern4(n)
    Pattern5(n)
    Pattern6(n)
    Pattern7(n)
    Pattern8(n)
    Pattern9(n)
    Pattern10(n)
    Pattern11(n)
    '''


if __name__ == '__main__':
    main()
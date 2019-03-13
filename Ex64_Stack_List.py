def IsStackFull(L1):
    if IsStackEmpty(L1):
        print("\nThe stack is empty.\n")
    elif len(L1) >= 6:
        return True
    else:
        print("\nThe stack is not full.\n")

def IsStackEmpty(L1):
    if L1 == []:
        return True
    else:
        return False

def Push(L1):
    if not IsStackFull(L1):
        no = eval(input("\nEnter the element to push in the stack :: "))
        L1.append(no)
    else:
        print("\nSorry cant add an element as the stack is full\n")
    return L1

def Pop(L1):
    if not IsStackEmpty(L1):
        print("\nRemoved the element {} from top of the stack\n ".format(L1.pop()))
    else:
        print("\nSorry cant remove an element as the stack is empty.\n")

def Peep(L1):
    if not IsStackEmpty(L1):
        print("\nThe current top of the stack element is {}\n".format(L1[len(L1)-1]))
    else:
        print("\nSorry the stack is empty.\n")

def Display(L1):
    if not IsStackEmpty(L1):
        print("\nThe current stack is {}\n".format(L1))
    else:
        print("\nThe stack is empty.\n")
'''
def DeleteStack(L1):
    if not IsStackEmpty(L1):
        del(L1)
        print("The stack deleted successfully.")
    else:
        print("The stack is empty.")
'''
def menu(L1):
    #choice = 0
    while True:
        print("Enter the stack operation ::\n1. Push\n2. Pop\n3. IsStackFull\n4. IsStackEmpty\n5. Peep\n6. Display\n7. DeleteStack\n8. Exit\n")
        choice = eval(input("Enter your choice :: "))
        if choice == 1:
            Push(L1)
        elif choice == 2:
            Pop(L1)
        elif choice == 3:
            if IsStackFull(L1):
                print("\nThe stack is full.\n")
        elif choice == 4:
            if IsStackEmpty(L1):
                print("\nThe stack is empty.\n")
            else:
                print("\nThe stack is not empty.\n")
        elif choice == 5:
            Peep(L1)
        elif choice == 6:
            Display(L1)
        elif choice == 7:
            if not IsStackEmpty(L1):
                del(L1)
                print("\nThe stack deleted successfully.\n")
            else:
                print("\nThe stack is empty.\n")
            L1 = []
        elif choice == 8:
            break
        else:
            print("\nYou have entered an invalid choice.\n")


def main():
    print("Create a stack \n")
    L1 = []
    menu(L1)

if __name__ == '__main__':
    main()
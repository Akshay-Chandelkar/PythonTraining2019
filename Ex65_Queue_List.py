def IsQueueEmpty(L1):
    if L1 == []:
        return True
    else:
        return False

def IsQueueFull(L1):
    if IsQueueEmpty(L1):
        print("The queue is empty.\n")
    elif len(L1) >= 6:
        return True
    else:
        print("The queue is not full.\n")

def EnQueue(L1):
    if not IsQueueFull(L1):
        no = eval(input("Enter the element to enqueue in the queue :: "))
        L1.append(no)
    else:
        print("Sorry cant enqueue an element as the queue is full.\n")
    return L1

def DQueue(L1):
    if not IsQueueEmpty(L1):
        print("The element {} dequeued from the queue.\n ".format(L1.pop(0)))
    else:
        print("Sorry cant dequeue an element as the queue is empty.\n")

def Front(L1):
    if not IsQueueEmpty(L1):
        print("The element {} is in the front of the queue.\n".format(L1[0]))
    else:
        print("The queue is empty.\n")

def DisplayQueue(L1):
    if not IsQueueEmpty(L1):
        print("The current queue is {}\n".format(L1))
    else:
        print("The queue is empty.\n")

def menu(L1):
    while True:
        print("Enter the queue operation ::\n1.EnQueue\n2.DQueue\n3.IsQueueFull\n4.IsQueueEmpty\n5.Front\n6.Display\n7.DeleteQueue\n8.Exit")
        choice = eval(input("Enter your choice ::"))
        if choice == 1:
            EnQueue(L1)
        elif choice == 2:
            DQueue(L1)
        elif choice == 3:
            if IsQueueFull(L1):
                print("\nThe queue is full.\n")
        elif choice == 4:
            if IsQueueEmpty(L1):
                print("\nThe queue is empty.\n")
            else:
                print("\nThe queue is not empty.\n")
        elif choice == 5:
            Front(L1)
        elif choice == 6:
            DisplayQueue(L1)
        elif choice == 7:
            if IsQueueFull(L1):
                del(L1)
                print("\nThe queue is deleted successfully.\n")
            else:
                print("\nThe queue is empty.\n")
            L1 = []
        elif choice == 8:
            break
        else:
            print("\nYou have entered an invalid choice.\n")

def main():
    print("Create a queue ::")
    L1 = []
    menu(L1)

if __name__ == '__main__':
    main()

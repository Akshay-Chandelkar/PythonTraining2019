def CountOccurence(S1, S2):
    count = 0
    index = 0
    while index != -1:
        index = S1.find(S2)
        if index != -1:
            count +=1
            S1 = S1[index+1:]
    return count

def main():
    S1 = eval(input("Enter a string :: "))
    S2 = eval(input("Enter a search string :: "))
    #res = CountOccurence(S1,S2)
    print("The string {} occurs {} times in string {}".format(S2, CountOccurence(S1, S2), S1))

if __name__ == '__main__':
    main()
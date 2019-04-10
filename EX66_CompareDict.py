
def CompareDict(D1, D2):
    retval = True
    if type(D1) != dict or type(D2) != dict:
        retval = False
    elif len(D1) != len(D2):
        retval = False
    else:
        for key in D1:
            if key in D2 and D1[key] == D2[key]:
                continue
            retval = False
            break
    return retval


def main():
    D1 = eval(input("Enter the first dictionary :: "))
    D2 = eval(input("Enter the second dictionary :: "))
    if CompareDict(D1, D2):
        print("The dictionaries {} and {} are same.".format(D1, D2))
    else:
        print("The dictionaries {} and {} are Not same.".format(D1, D2))






if __name__ == '__main__':
    main()
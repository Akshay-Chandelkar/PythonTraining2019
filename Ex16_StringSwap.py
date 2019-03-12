

def StringSwap(S1,S2):
    if len(S1) > 2 and len(S2) > 2:
        return S2[:2] + S1[2:] , S1[:2] + S2[2:]
    else:
        return S1 , S2

if __name__ == '__main__':
    S1 = input("Enter the first string :: ")
    S2 = input("Enter the second string :: ")
    res = StringSwap(S1,S2)
    print("The new strings are as follows :: {}".format(res))
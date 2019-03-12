
def Verb(S1):
    if len(S1) >= 3 and "ing" in S1[-3:]:
        return  S1.replace("ing","ly")
    elif len(S1) >= 3 and "ing" not in S1[-3:]:
        return S1 + "ing"
    else:
        return S1

if __name__ == '__main__':
    S1 = input("Enter a string :: ")
    res = Verb(S1)
    print("The new string is :: {}".format(res))
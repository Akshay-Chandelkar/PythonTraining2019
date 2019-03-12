
def StringConcat(S1):
    if len(S1) >= 5:
        return S1[:2] + S1[-2:]
    else:
        return S1

if __name__ == '__main__':
    S1 = input("Enter a string with 5 or more characters :: ")
    res = StringConcat(S1)
    print("The new string is {}".format(res))
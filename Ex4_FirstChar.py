
def FirstChar(S1):
    S2 = 'T'
    if S1[0] == S2:
        return True
    else:
        return False

if __name__ == '__main__':
    S1 = input("Enter a string to verify first char :: ")
    res = FirstChar(S1)
    print("The entered string starts with 'T' is {}".format(res))


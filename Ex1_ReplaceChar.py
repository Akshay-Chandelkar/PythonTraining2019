
'''
def ReplaceChar(S1,S2):
    return S1[0] + S1[1:].replace(S1[0],S2)


if __name__ == "__main__":
    S1 = input("Please enter a string:: ")
    S2 = input("Please enter the replacement char:: ")
    res = ReplaceChar(S1,S2)
    print("The new string is :: {}".format(res))
'''

def ReplaceChar(S1):
    return S1[0] + S1[1:].replace(S1[0],'*')


if __name__ == "__main__":
    S1 = input("Please enter a string:: ")
    #S2 = input("Please enter the replacement char:: ")
    res = ReplaceChar(S1)
    print("The new string is :: {}".format(res))


def LowerUpper(S1):
    return S1.lower() , S1.upper()

if __name__ == '__main__':
    S1 = input("Enter a string to be converted to lowercase and uppercase :: ")
    res = LowerUpper(S1)
    print("The entered string is converted to lowercase and uppercase as follows {}".format(res))


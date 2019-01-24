
def VerifyRotation(S1,S2):
    S3 = S1[::-1]
    if S2 == S3:
        return True
    else:
        return False

if __name__ == '__main__':
    S1 = input("Enter the first string :: ")
    S2 = input("Enter the second string to verify string rotation :: ")
    res = VerifyRotation(S1,S2)
    print("The second string is a rotation of first string is {}".format(res))

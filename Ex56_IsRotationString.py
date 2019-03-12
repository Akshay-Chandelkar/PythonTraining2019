'''
def RotatedString(S1, S2):
    if len(S1) == len(S2):
        S3 = S1 + S1
        if S2 in S3:
            return True
        else:
            return False
    else:
        return False
'''

def IsRotation(S1, S2):
    if len(S1) != len(S2):
        return False
    return S2 in S1 + S1


def main():
    S1 = eval(input("Enter the first string :: "))
    S2 = eval(input("Enter the second string :: "))
    #print("The string {} is a rotation of string {} :: {}".format(S2, S1, IsRotation(S1,S2)))
    if IsRotation(S1, S2):
        print("The string '{}' is a rotation of string '{}'.".format(S2, S1))
    else:
        print("The string '{}' is not a rotation of string '{}'.".format(S2, S1))

if __name__ == '__main__':
    main()
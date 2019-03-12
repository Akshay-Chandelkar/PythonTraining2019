def Rotation(S1):
    S2 = []
    S3 = S1
    i = 0
    while i != len(S1):
        S3 = S3[-1] + S3[:len(S3)-1]
        S2.append(S3)
        #print(S2)
        i +=1
    return S2

def main():
    S1 = eval(input("Enter a string :: "))
    print("All possible rotations of the string '{}' are :: {}".format(S1, Rotation(S1)))

if __name__ == '__main__':
    main()
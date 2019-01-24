__author__ = 'akshay.chandelkar'

'''
e.g. Input="jeetendra" Output="jeedaetnr"
'''

def JumbleString(S1):
    return S1[::2] + S1[1::2]


if __name__ == '__main__':
    S1 = input("Enter a string to be jumbled up :: ")
    res = JumbleString(S1)
    print("The jumbled up string is {}".format(res))
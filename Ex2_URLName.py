__author__ = 'akshay.chandelkar'


def DomainName(S1):
    return S1[4:-4]
    #return S2

if __name__ == '__main__':
    S1 = input("Enter a URL name :: ")
    res = DomainName(S1)
    print("The domain name for the given URL is {}".format(res))

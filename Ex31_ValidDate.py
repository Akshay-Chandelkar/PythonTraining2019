
def ValidDate(dd,mm,yy):
    if dd > 0 and dd < 32:
        if mm > 0 and mm < 13:
            if yy > 0:
                print("The date {}/{}/{} is valid.".format(dd,mm,yy))
            else:
                print("yy %d is invalid" %yy)
        else:
            print("mm %d is invalid" %mm)
    else:
        print("dd %d is invalid" %dd)


def main():
    dd,mm,yy = eval(input("Enter a date in dd,mm,yy format to check validity:: "))
    ValidDate(dd,mm,yy)

if __name__ == '__main__':
    main()

'''
#!C:\Python27
dd, mm, yy =input("Enter a date in dd,mm,yy format :: ")
if dd > 0 and dd < 32:
    if mm > 0 and mm < 13:
        if yy > 0:
            print("The date {}/{}/{} is valid.".format(dd,mm,yy))
        else:
            print("yy %d is invalid." %yy)
    else:
        print("mm %d is invalid." %mm)
else:
    print("dd %d is invalid." %dd)
'''
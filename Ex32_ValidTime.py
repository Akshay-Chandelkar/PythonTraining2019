
def ValidTime(hh,mm,ss):
    if hh >= 0 and hh < 25:
        if mm >= 0 and mm < 60:
            if ss > 0 and ss < 60:
                print("The time {}:{}:{} is valid.".format(hh,mm,ss))
            else:
                print("ss %d is invalid." %ss)
        else:
            print("mm %d is invalid." %mm)
    else:
        print("hh %d is invalid." %hh)

def main():
    hh,mm,ss = eval(input("Enter time in hh,mm,ss format :: "))
    ValidTime(hh,mm,ss)

if __name__ == '__main__':
    main()

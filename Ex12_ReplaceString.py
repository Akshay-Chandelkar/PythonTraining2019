'''
def ReplaceString(S1):
    if "not that bad" in S1:
        return S1.replace("not that bad","good")
    else:
        return S1

if __name__ == '__main__':
    S1 = input("Enter a string that contains 'not that bad' :: ")
    res = ReplaceString(S1)
    print("The new string is :: {}".format(res))
'''

def ReplaceString(S1):
    start_index = S1.find("not")
    end_index = S1.find("bad")
    return S1.replace(S1[start_index:end_index+3],'good')

def main():
    S1 = eval(input("Enter a string that contains 'not xx bad' :: "))
    print("The new string is :: {}".format(ReplaceString(S1)))

if __name__ == '__main__':
    main()


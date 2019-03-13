def OwnFromKeys(D1,V1=None):
    if type(D1)!= dict:
        print("{} is not a dictionary.".format(D1))
    result_dict = {}
    if type(V1) == list or type(V1) == tuple:
        i = 0
        length = len(D1.keys())
        for key in D1.keys():
            if i+1 == length and i+1 != len(V1):
                result_dict[key] = V1[i:]
            elif i < len(V1):
                result_dict[key] = V1[i]
                i += 1
            else:
                result_dict[key] = None
    else:
        for key in D1:
            result_dict[key] = V1
    return result_dict



def main():
    D1 = {'name':'Akshay', 'Age':'36','Marks':'100'}
    V1 = eval(input("Enter a list of values to be assigned to the keys in dictionary :: "))
    #print(D1)
    print("The dictionary {} with new values :: {} ".format(D1, OwnFromKeys(D1,V1)))
    '''
    print(D1)
    print(OwnFromKeys(D1,[1,'aks',50]))
    print(OwnFromKeys(D1,5))
    print(OwnFromKeys(D1))
    print(OwnFromKeys(D1,['Vikas',24]))
    print(OwnFromKeys(D1,['Braj',41,200,100,'Aks']))
    '''
if __name__ == '__main__':
    main()
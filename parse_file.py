#!/usr/bin/python

def ParseConfigFile(file_name):
    fd = open(file_name, "r+")
    line = fd.readline()
    result = {}
    while line != "":
        line = line.strip("\n")
        if line.__contains__("=") and not line.startswith("#"):
            print (line)
            l1 = line.split("=")
            print (l1)
            if l1[1].__contains__("#"):
                l2 = l1[1].split("#")
                result[l1[0]] = l2[0]
            else:    
                result[l1[0]] = l1[1]
        line = fd.readline()
    return result

if __name__=="__main__":
    file_name = input("Enter File Name:-")
    parsed_data = ParseConfigFile(file_name)
    print (parsed_data)

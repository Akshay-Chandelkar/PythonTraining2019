
def CharConsecutive(S1):
    output_str = " "
    i = 0
    while i < len(S1):
        ch = S1[i]
        count = 1
        while i + 1 < len(S1) and ch == S1[i+1]:
            count +=1
            i +=1
        output_str += ch
        if count > 1:
            output_str += str(count)
        i +=1
    return output_str

def main():
    S1 = input("Enter a string with consecutive characters:: ")
    print("The output string is {} .".format(CharConsecutive(S1)))

if __name__ == '__main__':
    main()




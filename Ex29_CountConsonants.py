
def CountConsonants(S1):
    count = 0
    i = 0
    while i < len(S1):
        #if S1[i] != 'a' and S1[i] != 'e' and S1[i] != 'i' and S1[i] != 'o' and S1[i] != 'u':
        if S1[i] not in ('a','e','i','o','u'):
            count += 1
        i += 1
    return count

def main():
    S1 = eval(input("Enter a string to find number of consonants:: "))
    res = CountConsonants(S1)
    print("The number of consonants in {} are {}".format(S1,res))

if __name__ == '__main__':
    main()

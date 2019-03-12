def CountVowelConstChar(S1):
    count_v = 0
    count_c = 0
    count_ch = 0
    i = 0
    while i < len(S1):
        if not S1[i].isalpha():
            count_ch += 1
        elif S1[i] == 'a' or S1[i] == 'e' or S1[i] == 'i' or S1[i] == 'o' or S1[i] == 'u':
            count_v += 1
        else:
            count_c += 1
        i += 1
    return count_v,count_c,count_ch




def main():
    S1 = eval(input("Enter an alpha-numeric string with characters :: "))
    count_v, count_c, count_ch = CountVowelConstChar(S1)
    print("The string has {} vowels, {} consonants and {} characters . ".format(count_v, count_c, count_ch))


if __name__ == '__main__':
    main()

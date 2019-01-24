
def NoPunctutation(S1):
    Punct = '''!()[]{}'"<>,;?.@#$*&'''
    S2 = ' '
    for char in S1:
        if char not in Punct:
            S2 = S2 + char
    return (S2)

if __name__ == '__main__':
    S1 = input("Enter a string with punctuations ::")
    res = NoPunctutation(S1)
    print("The new string without punctuations :: {}".format(res))
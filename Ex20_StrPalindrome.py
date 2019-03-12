def NumPalindrome(S1):
    S2 = S1[::-1]
    if S2 == S1:
        print("The string is a palindrome")
    else:
        print("The string is not a palindrome")


if __name__=='__main__':
    S1 = input("Enter a string to check for palindrome :: ")
    res = NumPalindrome(S1)
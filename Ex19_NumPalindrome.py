
def NumPalindrome(N1):
    rev = ReverseNumber(N1)
    if rev == N1:
        print("The number is a palindrome")
    else:
        print("The number is not a palindrome")


def ReverseNumber(N1):
    rem = 0
    rev = 0
    while N1 !=0:
        rem = N1 % 10
        rev = rev * 10 + rem
        N1 = int(N1//10)
    return rev

def main():
    N1 = int(input("Enter a number to check for palindrome :: "))
    NumPalindrome(N1)

if __name__=='__main__':
    main()
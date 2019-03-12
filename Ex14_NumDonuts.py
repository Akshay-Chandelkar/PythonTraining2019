
def NumDonuts(D1):
    if D1 > 10:
        print("Number of donuts too many.")
    else:
        print("Number of donuts :: ", D1)

if __name__ == '__main__':
    D1 = int(input("Enter the number of donuts :: "))
    res = NumDonuts(D1)
    #print(res)
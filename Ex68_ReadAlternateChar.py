
def AltChar(file_name):
    fd = open(file_name)
    offset = 20
    while True:
        data = fd.readline(10)
        print(data)
        if data == '':
            break
        fd.seek(offset,0)
        offset += 20
    fd.close()


def main():
    file_name = input("Enter the file to count alternate characters :: ")
    #offset = eval(input("Enter the number of characters to read from the given file :: "))
    AltChar(file_name)

if __name__ == '__main__':
    main()

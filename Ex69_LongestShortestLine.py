
def LongestShortestLine(file_name):
    fd = open(file_name)
    if fd != None:
        line = fd.readline()
        max_line = line
        min_line = line
        while line != '':
            line = fd.readline()
            if line == '':
                break
            if len(line) > len(max_line):
                max_line = line
            if len(line) < len(min_line):
                min_line = line
        return max_line, min_line


def main():
    file_name = input("Enter the filename to find longest and shortest line :: ")
    res1, res2 = LongestShortestLine(file_name)
    print("\nThe longest line is :: {} \nThe shortest line is :: {}".format(res1, res2))
    #print(res1,res2)

if __name__ == '__main__':
    main()

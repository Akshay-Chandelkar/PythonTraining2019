
def ParseConfigFile(file_name):
    result = {}
    fd = open(file_name)
    if fd != None:
        lines = fd.readlines()
        section_name = ""
        section_found = False
        section_details = {}
        for line in lines:
            #print(line)
            if line.startswith("#"):
                continue

            if section_found == True:
                result[section_name] = section_details
                section_found = False

            if line.startswith("["):
                if section_found == False:
                    section_name = line[1:-2]
                    section_found = True
                    section_details = {}
            elif section_found == False:
                line = line.strip("\n")
                config_line = line.split("=")
                #print(config_line)

                if "#" in config_line[1]:
                    config_line[1] = config_line[1].split("#")[0]
                section_details[config_line[0]] = config_line[1]
                #print(section_details)

        else:
            result[section_name] = section_details


        return result






def main():
    file_name = input("Enter the config file name:: ")
    result = ParseConfigFile(file_name)
    print(result)

if __name__ == '__main__':
    main()


def main():
    infile = open("input.txt","r")
    line = infile.readline()
    while line != "":
        print(line)
        line = infile.readline()

    infile.close()


main()
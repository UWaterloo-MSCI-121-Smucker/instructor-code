def main():
    infile = open("tutorial-nov-1-2024/lots-of-numbers.txt","r")
    line = infile.readline()
    sum = 0.0
    count = 0
    while line != "":
        count = count + 1
        sum = sum + float(line)
        line = infile.readline()

    infile.close()
    if count > 0:
        average = sum / count
        print(average)
    else:
        print("File was empty.")

if __name__ == "__main__":
    main()
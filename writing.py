def main():
    outfile = open("output.txt","w")
    outfile.write("No newline")
    outfile.write("with a newline\n")
    print("using print",file=outfile)
    print("no newline",file=outfile, end='')
    outfile.close()


if __name__ == "__main__":
    main()
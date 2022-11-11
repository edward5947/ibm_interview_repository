def detec_log():
    inputfile = str(input("enter the name of the file"))
    allValid = True
    errorCodes = []

    with open(inputfile, "r") as f:
        k = f.readline()
        for lines in f:
            if lines.replace("\n", "").split(" ")[1] == "false":
                allValid = False
                errorCodes.append(lines.replace("\n", "").split(" ")[2])
    if allValid:
        print("Yes")
    else:
        print("No")
        print(" ".join(errorCodes))

detec_log()
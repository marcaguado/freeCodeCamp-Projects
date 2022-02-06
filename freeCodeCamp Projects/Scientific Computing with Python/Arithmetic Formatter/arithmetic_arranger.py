def arithmetic_arranger(problems, doOperation = False):
    # Error handling #
    if len(problems) > 5:
        return "Error: Too many problems."
    finalTopRow = ""
    finalBottomRow = ""
    finalDashRow = ""
    finalResultRow = ""
    fourSpaces = "    "
    for i in problems:
        splitted = i.split()

        # More error handling #
        if splitted[1] != "+":
            if splitted[1] != "-":
                return "Error: Operator must be '+' or '-'."    
        isAddition = True if splitted[1] == "+" else False
        try:
            int(splitted[0]) + int(splitted[2])
        except:
            return "Error: Numbers must only contain digits."
        if int(splitted[0]) > 9999 or int(splitted[2]) > 9999:
            return "Error: Numbers cannot be more than four digits."
        
        # Output handling #
        biggerNum = splitted[0] if int(splitted[0]) >= int(splitted[2]) else splitted[2]
        dashes = "--"
        topNumberSpacing = ""
        bottomNumberSpacing = ""
        operationSpacing = ""
        operationResult = 0
        for k in range(0, len(biggerNum)):
            dashes += "-"
        for l in range(0, len(dashes) - len(splitted[0])):
            topNumberSpacing += " "
        for m in range(0, len(dashes) - len(splitted[2]) - len(splitted[1])):
            bottomNumberSpacing += " "
        if doOperation:
            if isAddition:
                operationResult = int(splitted[0]) + int(splitted[2])
            else:
                operationResult = int(splitted[0]) - int(splitted[2])
            for n in range(0, len(dashes) - len(str(operationResult))):
                operationSpacing += " "
        if i == problems[-1]:
            finalTopRow += topNumberSpacing + splitted[0]
            finalBottomRow += splitted[1] + bottomNumberSpacing + splitted[2]
            finalDashRow += dashes
            finalResultRow += operationSpacing + str(operationResult)
        else:
            finalTopRow += topNumberSpacing + splitted[0] + fourSpaces
            finalBottomRow += splitted[1] + bottomNumberSpacing + splitted[2] + fourSpaces
            finalDashRow += dashes + fourSpaces
            finalResultRow += operationSpacing + str(operationResult) + fourSpaces
    # Return handling
    if doOperation:
        return finalTopRow + "\n" + finalBottomRow + "\n" + finalDashRow + "\n" + finalResultRow
    else:
        return finalTopRow + "\n" + finalBottomRow + "\n" + finalDashRow 
    

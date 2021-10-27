def getChangeMethods(numberOfCents):
    # The variable coinSet defines all the cent values of the Canadian coins.
    coinSet = [1, 5, 10, 25, 100, 200]

    # lengthSet is the length of the array coinSet, which is six, as there are six Canadian coins.
    lengthSet = len(coinSet)

    # changeList is the variable that will be outputted at the end and here it is creating an array of zeroes.
    changeList = (lengthSet + 1) * [0]

    # This makes each entry in the array another array of zeroes each with the length of the parameter numberOfCents.
    for i in range(lengthSet + 1):
        changeList[i] = [0] * (numberOfCents + 1)

    # The following statements debug any problems that could arise from entering problematic numbers into the function,
    # and prime the array changeList for the finding of combinations.
    changeList[0][0] = 1

    for a in range(1, numberOfCents + 1):
        changeList[0][a] = 0

    for b in range(1, lengthSet + 1):
        changeList[b][0] = 1

    # This loop checks for all possible ways to make change for a certain amount of cents with Canadian coins.
    for a in range(1, lengthSet + 1):
        for i in range(1, numberOfCents + 1):
            if i >= coinSet[a - 1]:
                changeList[a][i] = changeList[a - 1][i] + changeList[a][i - coinSet[a - 1]]
            else:
                changeList[a][i] = changeList[a - 1][i]

    return print(changeList[lengthSet][numberOfCents])


getChangeMethods(100)

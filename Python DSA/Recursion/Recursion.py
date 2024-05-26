def printRecursion(x):
    if x < 1:
        return
    else:
        print(x, end=" ")
        printRecursion(x-1)
        print(x, end=" ")
        return

test =3
printRecursion(test)
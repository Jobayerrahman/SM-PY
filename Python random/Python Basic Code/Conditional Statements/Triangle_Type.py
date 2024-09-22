#Triangle Type Checker: Write a Python program that takes three sides of a triangle as input and determines whether 
#it forms an equilateral, isosceles, or scalene triangle.

def valid_triangle(sideA, sideB, sideC):
    if sideA+sideB >= sideC and sideB+sideC >= sideA and sideA+sideC >= sideB:
        return True
    else:
        return False

def type_check_triangle(sideA,sideB,sideC):
    if sideA == sideB  and sideB == sideC:
        print("Triangle is Equilateral.")
    elif sideA == sideB or sideB == sideC or sideA == sideC:
        print("Triangle is Isosceles.")
    else:
        print("Triangle is Scalene.")


sideA = int(input("Enter the side A : "))
sideB = int(input("Enter the side B : "))
sideC = int(input("Enter the side C : "))


if valid_triangle(sideA, sideB, sideC):
    type_check_triangle(sideA, sideB, sideC)
else:
    print('Tringle is not possible from given sides.')
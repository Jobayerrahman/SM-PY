#Data Type Checker: Write a Python function that takes a variable as input and returns the data type of the variable as a string (e.g., “int”, “float”, “str”, “list”, etc.).

def type_Checker(value):
    valueType = type(value)
    return valueType;

print("Your entered value's type is : ",type_Checker(322))
print("Your entered value's type is : ",type_Checker(320.241))
print("Your entered value's type is : ",type_Checker('sdfse'))
print("Your entered value's type is : ",type_Checker([1,2,5,6,23,21]))

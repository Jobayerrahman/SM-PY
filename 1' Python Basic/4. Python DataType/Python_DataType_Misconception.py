#In Python, type casting and type conversion mean the same thing — changing a value from one data type to another. 
#Python does not officially differentiate between these two terms.

x = "10"
y = int(x)  # converting/casting string to integer


#Python does automatic type conversion (implicit conversion) in some cases:

x = 5    # integer
y = 2.5  # float
z = x + y  # int + float → Python automatically converts int to float
print(z)  # 7.5
print(type(z))  # float



#✔ In Python, type casting and type conversion mean the same thing in practice.
#✔ However, technically Python does only type conversion using built-in functions.
#✔ Python does not support real type casting like C/C++ where you can forcefully change data types at memory level.

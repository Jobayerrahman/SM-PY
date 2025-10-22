import os

readNewFile = open("NewFile.txt","r");
readExcelFile = open("ExcelFile.xlsx","r");

print(readNewFile.read())
print(readExcelFile.read())
#Dictionary Sorting: Given a dictionary with names as keys and corresponding ages as values, write a Python program to sort the dictionary based on age in ascending order.

Dict = {
    'A' : 12,
    'N' : 3,
    'D' : 21,
    'B' : 4,
    'C' : 24,
    'W' : 15
}

ResultDict = {}

min_value = float("inf")

for key, value in Dict.items():
    # if min_value > value:
    #     min_value = value
    #     print(min_value)
    print(f"Key: {key}, Value: {value}")
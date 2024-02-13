#List Min & Max
list01 = [62,75,57,2,15]

def minfunc(List):
    min = List[0]
    for x in List:
        if min > x:
            min = x
    return min

def maxfunc(List):
    max = List[0]
    for x in List:
        if max < x:
            max = x
    return max

minResult = minfunc(list01)
maxResult = maxfunc(list01)

print(f'{"Min List Item : "} {minResult}')
print(f'{"Max List Item : "} {maxResult}')
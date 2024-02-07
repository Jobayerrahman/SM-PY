def solve(s):
    name = s.split(' ')
    capitalizeList =[]
    str =' '
    
    for x in name:
        capitalName = x.capitalize()
        capitalizeList.append(capitalName)
    
    return str.join(capitalizeList)


if  __name__ == '__main__' :

    string = 'we lived in bangladesh'

    result = solve(string)

    print(result)
#Pypy3

def solve(s):
    name    = s.split(" ");
    newName = []
    str = " "

    for x in name:
        capitalName = x.capitalize()
        newName.append(capitalName)

    return str.join(newName)

if __name__ == '__main__':

    s = "hello world"

    result = solve(s)

    print(result)
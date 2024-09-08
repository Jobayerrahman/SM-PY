Number = int(input('Enter the number: '))
GivenList = list(map(int, input().split()))

ResultList = []

for i in GivenList:
    if i not in ResultList:
        ResultList.append(i)
print('Duplicated included List',GivenList)
print('Duplicate exclued List', ResultList)


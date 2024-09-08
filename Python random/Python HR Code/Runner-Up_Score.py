if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    highest_score = 0
    sec_highest_score = 0
    nonDuplicate_list = []
    
    for x in arr:
        if x not in nonDuplicate_list:
            nonDuplicate_list.append(x)
    
    for x in nonDuplicate_list:
        if x > highest_score:
            sec_highest_score = highest_score
            highest_score = x
        elif x > sec_highest_score and x != highest_score:
            sec_highest_score = x
            
    
    print(sec_highest_score)

    # print("This is more shortest way :",sorted(list(set(arr)))[-2]) IndexError: list index out of range (showing empty list)
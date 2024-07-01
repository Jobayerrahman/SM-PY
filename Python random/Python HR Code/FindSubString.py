def count_substring(string, sub_string):
    count = 0;
    start_index=0;
    for i in range(0, len(string)):
        subString = string.find(sub_string, start_index)
        if(subString != -1):
            start_index = subString + 1
            count += 1
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
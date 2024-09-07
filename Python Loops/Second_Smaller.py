def Second_Smaller(number):
    sec_smaller = float("inf")
    smaller = float("inf")

    for x in range(len(number)):
        if number[x] < smaller:
            sec_smaller = smaller
            smaller = number[x]

        elif number[x] < sec_smaller and number[x] != smaller:
            sec_smaller = number[x]
        
    print(sec_smaller)

number = [5, 2, 8, 3, 1, 7]
Second_Smaller(number)
        
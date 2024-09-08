if __name__ == '__main__':
    sscore = []
    lowest_score = 100
    second_lowest_score = 0
    python_students =[]
    last_score_names = []
    
    for _ in range(int(input())):
        name = input()
        score = float(input())
        python_students.append([name,score])
        sscore.append(score)
        
    for stu in python_students:
        temp_name = stu[0]
        temp_score = stu[1]
        if temp_score < lowest_score:
            second_lowest_score = lowest_score
            lowest_score = temp_score
        elif temp_score < second_lowest_score and temp_score != lowest_score:
            second_lowest_score = temp_score
    
    student_list = [x[0] for x in python_students if second_lowest_score == x[1]]
    
    sscore = sorted(student_list)
    
    for name in sscore:
        print(name)

if __name__ == '__main__':
    sscore = []
    second_lowest_score = 0
    lowest_score = 100
    python_students = []
    last_score_name = []
    student_number = int(input('Enter the amount of student : '))

    for x in range(student_number):
        name = str(input('Enter the student name : '))
        score = int(input('Enter the student score : '))
        python_students.append([name, score])

    for stu in python_students:
        second_lowest_score = lowest_score
        temp_stu_name = stu[0]
        temp_stu_score = stu[1]

        if temp_stu_score < lowest_score:
            lowest_score = temp_stu_score
            last_score_name = [temp_stu_name]

    
    print(second_lowest_score)
    print(last_score_name)
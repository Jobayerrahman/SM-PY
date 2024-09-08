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
        temp_stu_name = stu[0]
        temp_stu_score = stu[1]

        if temp_stu_score < lowest_score:
            second_lowest_score = lowest_score
            lowest_score = temp_stu_score
        elif temp_stu_score < second_lowest_score and temp_stu_name != lowest_score:
            second_lowest_score = temp_stu_score

    student_list =[x[0] for x in python_students if second_lowest_score == x[1]]

    sorted_student_list = sorted(student_list)

    print(second_lowest_score)
    print(sorted_student_list)
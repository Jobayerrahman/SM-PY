#Dictionary Manipulation: Given a dictionary with student names as keys and their corresponding scores as values, 
# write a Python program to add a new student to the dictionary and update the score of an existing student.

Dict = {
    'Sakib' : '10',
    'Rahim' : '100',
    'Shanto' : '30',
}



Dict.update({'Miraz': '50'})
Dict.update({'Liton': '0'})
Dict.update({'Rahim': '120'})

print(Dict)
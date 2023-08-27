"""name = "angela"
new_list =[letter for letter in name]
print(new_list)"""

"""range_list =[num*2 for num in range(1,5)]
print(range_list)"""

"""names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
print(names)
short_names = [name for name in names if len(name) < 5]
capital_names = [name.upper() for name in names if len(name)>5]

print(short_names)
print(capital_names)"""
"""import random
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
student_scores ={student:random.randint(1,100) for student in names}
passed_students = {student:score for(student,score) in student_scores.items() if(score)>=60}


print(student_scores)
print(passed_students)"""


#iterate in pandas
student_dict ={
    "student": ["Angela", "James", "Lily"],
    "score": [56,76,98]
}

import pandas

student_data_frame = pandas.DataFrame(student_dict)
#print(student_data_frame)

#Loop through rows of a data frame
for (index,row) in student_data_frame.iterrows():
    print(row)
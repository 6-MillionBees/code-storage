# Arden Boettcher
# 10/29/24
# Lists MC

import random

def grades(): # I didn't want to write down the grades
    number = [random.randint(80, 100) for x in range(4)]
    return sum(number) / len(number)


boettcher_sydney = []
baylie_oliver = []
feck_sophie = []
hart_rayden = []


student_name = ['BOETTCHER, Sydney', 'BAYLIE, Oliver', 'FECK, Sophie', 'HART, Rayden']
students = [boettcher_sydney, baylie_oliver, feck_sophie, hart_rayden]
course = ['Writer\'s Studio', 'Engineering Academy', 'Health Studies', 'Information Technology']
num = 0


for student in students:
    student.append(student_name[students.index(student)])
    student.append('Greenspire HS')
    student.append(course[students.index(student)])
    student.append(grades())

students.sort() # Schools LOVE their alphabetical sorts

for student in students:
    print(f'''
# {students.index(student) + 1}
Student: {student[0]}
School:  {student[1]}
Course:  {student[2]}
Grades:  {student[3]}''')
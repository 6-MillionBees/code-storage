# Arden Boettcher
# 11/11/24
# List Comprehensions



# Title Case Names

students_upper = ['GEORG', 'JOSHUA', 'MIKEY', 'LILY', 'PHILOMINA', 'BENJAMIN']
students_title = [student.title() for student in students_upper]
print(students_upper)
print(students_title)


# Filtered Lowercase Names

students_lower = [student.lower() for student in students_upper]

print(students_lower)


# Inches To Centemeters

inches = [14, 20, 36, 40]
centimeters = [inch * 2.54 for inch in inches]

print('Input (inches): ', *inches)
print('Output (centimeters): ', *centimeters)


# filtered last names

last_names = ['Williams', 'Perez', 'Matthes', 'Brown', 'Carlsen', 'Brimley', 'Vincent']

bast_bames = [name for name in last_names if name.lower().startswith('b')]

print(bast_bames)
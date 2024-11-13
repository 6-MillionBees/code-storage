# Arden Boettcher
# 11/11/24
# List Comprehensions



# Title Case Names

students = ['GEORG', 'JOSHUA', 'MIKEY', 'LILY', 'PHILOMINA', 'BENJAMIN']
students_title = [student.title() for student in students]


# Filtered Lowercase Names

students_lower = [student.lower() for student in students if len(student) >= 4]

print(', '.join(students_lower))


# Inches to Centimeters

inches = [14, 20, 36, 40]

centimeters = [inch * 2.54 for inch in inches]

print('Input (inches): ', *inches)
print('Output (centimeters): ', *centimeters)
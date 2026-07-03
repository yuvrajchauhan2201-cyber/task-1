import csv

INPUT_CSV = "students.csv"
OUTPUT_TXT = "student_summary.txt"

students = []

with open(INPUT_CSV, mode="r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append(row)

total_students = len(students)

ages = [int(student["age"]) for student in students]
average_age = sum(ages) / total_students if total_students > 0 else 0

output = f"Total Students: {total_students}\n"
output += f"Average Age: {average_age:.2f}\n\n"
output += "Student List:\n"

for student in students:
    output += f"- {student['name']} (Age: {student['age']})\n"

print(output)

with open(OUTPUT_TXT, mode="w", encoding="utf-8") as file:
    file.write(output)

print(f"Output saved in {OUTPUT_TXT}")
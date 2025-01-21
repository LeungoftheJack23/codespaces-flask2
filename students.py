import json

# Step 1: Read the JSON file
with open('students.json', 'r') as file:
    data = json.load(file)

# Step 2: Process the JSON data
# Assuming the JSON data is a list of students
for student in data:
    print(f"Name: {student['name']}")
    print(f"Age: {student['age']}")
    print("Grades:")
    for subject in student['grade']:
        print(f"  - {subject}")
    print('---')
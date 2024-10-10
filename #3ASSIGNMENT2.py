#ASSIGNMENT2

import csv

#loading the dataset and display the first few records
def load_data(filename):
    students = []
    with open(filename, mode='r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            grade_str = row['grade'].strip().lower()
            grade = int(grade_str[:-2]) if grade_str[-2:] in ['th', 'st', 'nd', 'rd'] else int(grade_str)
            students.append({
                'Student ID': int(row['Student ID']),
                'Student Name': row['student_name'],
                'Gender': row['gender'],
                'Grade': grade,
                'School Name': row['school_name'],
                'Reading Score': int(row['reading_score']),
                'Math Score': int(row['math_score'])
            })
    return students

#displaying the first few records
def display_first_records(students, n=5):
    print("\nPrimeros registros:")
    for student in students[:n]:
        print(student)

#selection sort by Math Score (descending)
def selection_sort_math(students):
    for x in range(len(students)):
        max_idx = x
        for y in range(x + 1, len(students)):
            if students[y]['Math Score'] > students[max_idx]['Math Score']:
                max_idx = y
        students[x], students[max_idx] = students[max_idx], students[x]

#insertion sort by Reading Score
def insertion_sort_reading(students):
    for i in range(1, len(students)):
        key = students[i]
        y = i - 1
        while y >= 0 and key['Reading Score'] < students[y]['Reading Score']:
            students[y + 1] = students[y]
            y -= 1
        students[y + 1] = key

#linear search for student by Student ID
def linear_search_by_id(students, student_id):
    for student in students:
        if student['Student ID'] == student_id:
            return student
    return None

#binary search for student by Reading Score 
def binary_search_by_reading(students, reading_score):
    low, high = 0, len(students) - 1
    while low <= high:
        mid = (low + high) // 2
        if students[mid]['Reading Score'] == reading_score:
            return students[mid]
        elif students[mid]['Reading Score'] < reading_score:
            low = mid + 1
        else:
            high = mid - 1
    return None

#calculation for the average by grade
def calculate_averages_by_grade(students):
    grade_stats = {}
    for student in students:
        grade = student['Grade']
        if grade not in grade_stats:
            grade_stats[grade] = {
                'total_math': 0,
                'total_reading': 0,
                'count': 0
            }
        grade_stats[grade]['total_math'] += student['Math Score']
        grade_stats[grade]['total_reading'] += student['Reading Score']
        grade_stats[grade]['count'] += 1

    for grade, stats in grade_stats.items():
        avg_math = stats['total_math'] / stats['count']
        avg_reading = stats['total_reading'] / stats['count']
        print(f"Grade {grade} - Math average: {avg_math:.2f}, Reading average: {avg_reading:.2f}")

#calculation for pass percentage
def calculate_pass_percentage(students):
    pass_math = 0
    pass_reading = 0
    total_students = len(students)
    
    for student in students:
        if student['Math Score'] >= 70:
            pass_math += 1
        if student['Reading Score'] >= 70:
            pass_reading += 1
    
    pass_math_percentage = (pass_math / total_students) * 100
    pass_reading_percentage = (pass_reading / total_students) * 100
    print(f"\nPass Rate - Mathematics: {pass_math_percentage:.2f}%, Reading: {pass_reading_percentage:.2f}%")

#main function
def main():
    filename = 'students_complete.csv'
    
    #loading and display dataset
    students = load_data(filename)
    display_first_records(students)

    #sort by Math Score using selection sort
    selection_sort_math(students)
    print("\nStudents with higher scores in Mathematics:")
    display_first_records(students)

    #sort by Reading Score using insertion sort
    insertion_sort_reading(students)
    print("\nStudents with lower Reading scores")
    display_first_records(students)

    #linear search by Student ID
    student_id = int(input("\nEnter a student ID to find your scores: "))
    student = linear_search_by_id(students, student_id)
    if student:
        print(f"Student finded: {student}")
    else:
        print("Student not finded")

    #binary search by Reading Score
    reading_score = int(input("\nEnter a Reading score to search for a student: "))
    student = binary_search_by_reading(students, reading_score)
    if student:
        print(f"Student finded: {student}")
    else:
        print("Student not finded")

    #calculation and display average scores for each Grade
    print("\nReading and Mathematics averages by Grade:")
    calculate_averages_by_grade(students)

    #calculation and display pass percentage
    print("\nPercentage of approval:")
    calculate_pass_percentage(students)

main()


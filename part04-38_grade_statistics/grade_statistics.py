# Write your solution here

def convert_points():
    entries = []
    while True:
        line = input("Exam points and exercises completed: ")
        if line == "":
            break
        exam_points_str, exercises_str = line.split()
        exam_points = int(exam_points_str)
        exercises_answered = int(exercises_str)
        exercises_points = exercises_answered // 10
        entries.append((exam_points, exercises_points))
    return entries

def calculate_grade(exam, exercise):
    total = exam + exercise
    if exam < 10:
        return 0
    elif total <= 14:
        return 0
    elif total <= 17:
        return 1
    elif total <= 20:
        return 2
    elif total <= 23:
        return 3
    elif total <= 27:
        return 4
    else:
        return 5

def process_entries(entries):
    grades = []
    total_points = []

    for exam, exercise in entries:
        grade = calculate_grade(exam, exercise)
        grades.append(grade)
        total_points.append(exam + exercise)

    average = sum(total_points) / len(total_points) if total_points else 0.0
    pass_percentage = (sum(g > 0 for g in grades) / len(grades) * 100) if grades else 0.0

    print("Statistics:")
    print(f"Points average: {average:.1f}")
    print(f"Pass percentage: {pass_percentage:.1f}")
    print("Grade distribution:")
    for grade in range(5, -1, -1):
        stars = "*" * grades.count(grade)
        print(f"  {grade}: {stars}")

# Run the program
entries = convert_points()
process_entries(entries)

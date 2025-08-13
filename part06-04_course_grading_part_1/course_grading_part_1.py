def read_csv_file(filename):
    """Read a CSV file and return lines without header"""
    with open(filename, 'r') as file:
        lines = file.readlines()
        # Return lines without header, stripped and non-empty
        return [line.strip() for line in lines[1:] if line.strip()]

def parse_student_data(filename):
    """Parse student CSV file and return student info and order"""
    student_order = []
    students = {}
    student_lines = read_csv_file(filename)
    
    for line in student_lines:
        parts = line.split(';')
        student_id = parts[0]
        first_name = parts[1]
        last_name = parts[2]
        students[student_id] = (first_name, last_name)
        student_order.append(student_id)
    
    return students, student_order

def parse_exercise_data(filename):
    """Parse exercise CSV file and return exercise totals"""
    exercise_totals = {}
    exercise_lines = read_csv_file(filename)
    
    for line in exercise_lines:
        parts = line.split(';')
        student_id = parts[0]
        # Sum up exercises from columns 1-7 (e1 through e7)
        total_exercises = sum(int(parts[i]) for i in range(1, 8))
        exercise_totals[student_id] = total_exercises
    
    return exercise_totals

def print_student_results(students, student_order, exercise_totals):
    """Print student results in the correct order"""
    for student_id in student_order:
        first_name, last_name = students[student_id]
        total = exercise_totals.get(student_id, 0)
        print(f"{first_name} {last_name} {total}")

# Main program
student_info = input("Student information: ")
exercise_data = input("Exercises completed: ")

students, student_order = parse_student_data(student_info)
exercise_totals = parse_exercise_data(exercise_data)
print_student_results(students, student_order, exercise_totals)
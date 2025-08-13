# tee ratkaisu tänne
def read_csv_file(filename):
    """Read a CSV file and return lines without header"""
    with open(filename, 'r') as file:
        lines = file.readlines()
        return [line.strip() for line in lines[1:] if line.strip()]

def parse_student_data(filename):
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
    exercise_totals = {}
    exercise_lines = read_csv_file(filename)
    for line in exercise_lines:
        parts = line.split(';')
        student_id = parts[0]
        total_exercises = sum(int(parts[i]) for i in range(1, 8))
        exercise_totals[student_id] = total_exercises
    return exercise_totals

def parse_exam_data(filename):
    exam_totals = {}
    exam_lines = read_csv_file(filename)
    for line in exam_lines:
        parts = line.split(';')
        student_id = parts[0]
        total_exam = sum(int(parts[i]) for i in range(1, 4))
        exam_totals[student_id] = total_exam
    return exam_totals

def read_course_info(filename):
    with open(filename, 'r') as file:
        lines = [line.strip() for line in file if line.strip()]
        name = lines[0].split(":")[1].strip()
        credits = lines[1].split(":")[1].strip()
    return name, credits

def calculate_grades(students, student_order, exercise_totals, exam_totals):
    results = []
    for student_id in student_order:
        first_name, last_name = students[student_id]
        exercise_total = exercise_totals.get(student_id, 0)
        exam_total = exam_totals.get(student_id, 0)
        exercise_points = exercise_total * 10 // 40
        final_score = exercise_points + exam_total

        if final_score < 15:
            grade = 0
        elif final_score <= 17:
            grade = 1
        elif final_score <= 20:
            grade = 2
        elif final_score <= 23:
            grade = 3
        elif final_score <= 27:
            grade = 4
        else:
            grade = 5

        results.append((student_id, f"{first_name} {last_name}", exercise_total, exercise_points, exam_total, final_score, grade))
    return results

def write_results_txt(course_name, course_credits, results):
    with open("results.txt", "w") as file:
        file.write(f"{course_name}, {course_credits} credits\n")
        file.write("=" * 38 + "\n")
        file.write(f"{'name':29} {'exec_nbr':<9} {'exec_pts.':<9} {'exm_pts.':<9} {'tot_pts.':<9} {'grade':<9}\n")
        for result in results:
            _, name, exec_nbr, exec_pts, exm_pts, tot_pts, grade = result
            file.write(f"{name:29} {exec_nbr:<9} {exec_pts:<9} {exm_pts:<9} {tot_pts:<9} {grade:<9}\n")

def write_results_csv(results):
    with open("results.csv", "w") as file:
        for result in results:
            student_id, name, _, _, _, _, grade = result
            file.write(f"{student_id};{name.lower()};{grade}\n")

# Execution starts here
student_info = input("Student information: ")
exercise_data = input("Exercises completed: ")
exam_data = input("Exam points: ")
course_info = input("Course information: ")

students, student_order = parse_student_data(student_info)
exercise_totals = parse_exercise_data(exercise_data)
exam_totals = parse_exam_data(exam_data)
course_name, course_credits = read_course_info(course_info)

results = calculate_grades(students, student_order, exercise_totals, exam_totals)
write_results_txt(course_name, course_credits, results)
write_results_csv(results)

print("Results written to files results.txt and results.csv")

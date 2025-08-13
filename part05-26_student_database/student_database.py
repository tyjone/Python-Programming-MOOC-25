# Write your solution here
def add_student(students: dict, name: str):
    if name not in students:
        students[name] = {}  # Dictionary of course: grade


def print_student(students: dict, name: str):
    if name not in students:
        print(f"{name}: no such person in the database")
        return

    courses = students[name]
    print(f"{name}:")
    if not courses:
        print(" no completed courses")
    else:
        print(f" {len(courses)} completed courses:")
        for course, grade in courses.items():
            print(f"  {course} {grade}")
        avg = sum(courses.values()) / len(courses)
        print(f" average grade {avg:.1f}")


def add_course(students: dict, name: str, course_info: tuple):
    if name not in students:
        return  # Student not in the database

    course_name, grade = course_info
    if grade == 0:
        return  # Ignore grade 0

    # Only add/update if course is new or grade is higher
    if course_name not in students[name] or students[name][course_name] < grade:
        students[name][course_name] = grade

def summary(students: dict):
    print(f"students {len(students)}")

    if not students:
        return

    most_courses = max(students.items(), key=lambda item: len(item[1]))
    best_avg = max(
        (s for s in students.items() if s[1]),
        key=lambda item: sum(item[1].values()) / len(item[1])
    )

    print(f"most courses completed {len(most_courses[1])} {most_courses[0]}")
    avg_grade = sum(best_avg[1].values()) / len(best_avg[1])
    print(f"best average grade {avg_grade:.1f} {best_avg[0]}")






if __name__ == "__main__":
    students = {}
    add_student(students, "Peter")
    add_course(students, "Peter", ("Introduction to Programming", 3))
    add_course(students, "Peter", ("Advanced Course in Programming", 2))
    print(students)
    print_student(students, "Peter")
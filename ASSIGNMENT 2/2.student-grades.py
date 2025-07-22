# Create a dictionary where the keys are student names and the values are their grades. Allow the user to:
# Add a new student and grade.
# Update an existing student’s grade.
# Print all student grades.

student_grades = {}
ALLOWED_GRADING = ["A", "B", "C", "D", "E", "F"]


def add_student(name, grade):
    if grade not in ALLOWED_GRADING:
        print(f"ERROR: The Grade should be among {ALLOWED_GRADING}")
        return
    if name in student_grades:
        print("ERROR: Cannot add an already existing Student. Select Update for modification.")
        return
    student_grades[name] = grade
    print(f"Successfully added the student {name} with grade {grade}")


def update_student(name, grade):
    if name not in student_grades:
        print(f"ERROR: No such user {name} exists in the students list")
        return
    if grade not in ALLOWED_GRADING:
        print(f"ERROR: The Grade should be among {ALLOWED_GRADING}")
        return
    student_grades[name] = grade
    print(f"Successfully update the grade of student {name} with grade {grade}")


def list_students():
    print()
    for name, grade in student_grades.items():
        print(name, grade, sep=": ", end="\n")
    if not student_grades:
        print("No students are added yet!\n")


if __name__ == "__main__":
    while True:
        print("  1. List all Students with their Grades\n"
              "  2. Add a new Student and their grade\n"
              "  3. Update an existing student's grade\n"
              "  4. Exit")
        num = input("Please select a number between 1-4: ")
        if num not in ["1", "2", "3", "4"]:
            print("ERROR: Not a valid input")
            continue
        if num == "4":
            break
        if num == "1":
            list_students()
        else:
            name = input("Enter the name of the student: ")
            grade = input(f"Enter the grade for student {name}: ")
            if num == "2":
                add_student(name, grade)
            elif num == "3":
                update_student(name, grade)

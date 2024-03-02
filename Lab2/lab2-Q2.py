def process_grades(file_name):
    try:
        with open(file_name, 'r') as file:
            total_grades = 0
            num_students = 0
            failed_students = []

            for line in file:
                name, grade = line.split()
                grade = float(grade)
                total_grades += grade
                num_students += 1
                if grade < 60:
                    failed_students.append(name)

            average_grade = total_grades / num_students if num_students > 0 else 0
            print("Average Grade:", average_grade)
            print("Failed Students:", failed_students)
    except FileNotFoundError:
        print("File not found")
    except ValueError:
        print("Error: Grades must be numeric")

# Example usage
process_grades("students.txt")

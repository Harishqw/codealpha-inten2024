class Student:
    def __init__(self, name):
        self.name = name
        self.grades = {}

    def add_grade(self, subject, grade):
        if subject in self.grades:
            self.grades[subject].append(grade)
        else:
            self.grades[subject] = [grade]

    def calculate_average(self):
        total_grade = 0
        num_grades = 0
        for subject, grades_list in self.grades.items():
            total_grade += sum(grades_list)
            num_grades += len(grades_list)
        if num_grades == 0:
            return 0
        else:
            return total_grade / num_grades

class GradeTracker:
    def __init__(self):
        self.students = {}

    def add_student(self, name):
        self.students[name] = Student(name)

    def add_grade(self, name, subject, grade):
        if name in self.students:
            self.students[name].add_grade(subject, grade)
        else:
            print("Student not found.")

    def calculate_average(self, name):
        if name in self.students:
            return self.students[name].calculate_average()
        else:
            print("Student not found.")
            return None

# Function to get user input for student grades
def get_student_grades(tracker):
    while True:
        name = input("Enter student name (or type 'done' to finish): ").strip()
        if name.lower() == 'done':
            break

        tracker.add_student(name)

        while True:
            subject = input("Enter subject name (or type 'done' to finish adding grades for this student): ").strip()
            if subject.lower() == 'done':
                break
            grade = float(input("Enter grade for this subject: "))
            tracker.add_grade(name, subject, grade)

# Function to calculate and print averages for students
def print_student_averages(tracker):
    print("\nStudent Averages:")
    for name in tracker.students:
        average = tracker.calculate_average(name)
        print(f"{name}: {average:.2f}")

# Main function
def main():
    tracker = GradeTracker()
    get_student_grades(tracker)
    print_student_averages(tracker)

if __name__ == "__main__":
    main()

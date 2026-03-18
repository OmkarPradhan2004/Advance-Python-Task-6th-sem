#student gradebook
students = {}
def calculate_grade(avg):
    if avg >= 90:
        return "A+"
    elif avg >= 80:
        return "A"
    elif avg >= 70:
        return "B"
    elif avg >= 60:
        return "C"
    elif avg >= 50:
        return "D"
    else:
        return "F"


while True:
    print("\n===== STUDENT GUIDEBOOK =====")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Edit Student")
    print("4. Delete Student")
    print("5. Exit")
    choice = input("Enter choice: ")
    if choice == "1":
        roll = input("Enter Roll Number: ")

        if roll in students:
            print("Student already exists!")
        else:
            name = input("Enter Name: ")
            course = input("Enter Course: ")

            try:
                n = int(input("Enter number of subjects: "))
            except ValueError:
                print("Invalid input!")
                continue

            marks = []
            for i in range(n):
                try:
                    m = int(input(f"Enter marks for subject {i+1}: "))
                    marks.append(m)
                except ValueError:
                    print("Invalid marks!")
                    break

            if len(marks) != n:
                continue

            total = sum(marks)
            average = total / n
            grade = calculate_grade(average)

            students[roll] = {
                "name": name,
                "course": course,
                "marks": marks,
                "total": total,
                "average": average,
                "grade": grade
            }
            print("Student Added Successfully!")

    elif choice == "2":
        if not students:
            print("No students found.")

        else:
            print("\n--- Student List ---")
            for roll, data in students.items():
                print("\nRoll No:", roll)
                print("Name:", data["name"])
                print("Course:", data["course"])
                print("Total Marks:", data["total"])
                print("Average:", round(data["average"], 2))
                print("Grade:", data["grade"])

    elif choice == "3":
        roll = input("Enter Roll Number to Edit: ")

        if roll in students:
            print("\n1. Edit Name")
            print("2. Edit Course")
            print("3. Edit Marks")
            print("4. Edit Roll Number")

            edit_choice = input("Enter choice: ")

            if edit_choice == "1":
                students[roll]["name"] = input("Enter new name: ")
                print("Name updated.")

            elif edit_choice == "2":
                students[roll]["course"] = input("Enter new course: ")
                print("Course updated.")

            elif edit_choice == "3":
                try:
                    n = int(input("Enter number of subjects: "))
                except ValueError:
                    print("Invalid input!")
                    continue

                marks = []
                for i in range(n):
                    try:
                        m = int(input(f"Enter marks for subject {i+1}: "))
                        marks.append(m)
                    except ValueError:
                        print("Invalid marks!")
                        break

                if len(marks) != n:
                    continue

                total = sum(marks)
                average = total / n
                grade = calculate_grade(average)

                students[roll]["marks"] = marks
                students[roll]["total"] = total
                students[roll]["average"] = average
                students[roll]["grade"] = grade

                print("Marks updated.")

            elif edit_choice == "4":
                new_roll = input("Enter new roll number: ")
                students[new_roll] = students.pop(roll)
                print("Roll number updated.")

            else:
                print("Invalid choice.")

        else:
            print("Student not found.")

    elif choice == "4":
        roll = input("Enter Roll Number to Delete: ")

        if roll in students:
            del students[roll]
            print("Student deleted successfully.")
        else:
            print("Student not found.")

    elif choice == "5":
        print("Exiting system.")
        break

    else:
        print("Invalid choice.")
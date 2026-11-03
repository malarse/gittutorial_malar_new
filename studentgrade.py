def stu_grde():
    try:
        no_of_students = int(input("Enter the number of students: "))
        s_name = input("Enter the name of the student: ")
        for i in range(no_of_students):
            s_marks = input(f"Enter the marks of student {i+1}: ")
            if s_marks.isdigit():
                s_marks = int(s_marks)
                if s_marks >= 90:
                    grade = 'A'
                elif s_marks >= 80:
                    grade = 'B'
                elif s_marks >= 70:
                    grade = 'C'
                elif s_marks >= 60:
                    grade = 'D'
                else:
                    grade = 'F'
                print(f"Student Name: {s_name}, Marks: {s_marks}, Grade: {grade}")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        return
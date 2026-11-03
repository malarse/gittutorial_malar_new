def stu_grde():
    try:
        no_of_students = int(input("Enter the number of students: "))
        student = []
        marks_list = []
        
        for i in range(no_of_students):
            s_name = input("Enter the name of the student: ")
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
                    
                student.append((s_name, s_marks, grade))
                marks_list.append(s_marks)
                print(f"Student Name: {s_name}, Marks: {s_marks}, Grade: {grade}")

        
        for s_name, s_marks ,grade in student:
            print(f"{s_name:<12}{s_marks:<12}{grade}")
        if marks_list:
                 
            print("Average Marks:", sum(marks_list) / len(marks_list))
            print("Highest Marks:", max(marks_list))
            print("Lowest Marks:", min(marks_list))

    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        return
stu_grde()
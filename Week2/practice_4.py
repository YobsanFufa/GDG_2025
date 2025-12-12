def get_grade(student_grades, student_name):
    try:
        return student_grades[student_name]  
    except KeyError:
        return "Student not found in the system"
# Example usage:
grades = {"Becky": 90,"Nimo": 82,"Moti": 87,}
print(get_grade(grades, "Moti"))  
print(get_grade(grades, "Alazer"))
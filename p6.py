
def assign_grade(marks):
    if marks < 40:
        return 'F'
    elif 40 <= marks < 45:
        return 'D'
    elif 45 <= marks < 50:
        return 'C'
    elif 50 <= marks < 55:
        return 'C+'
    elif 55 <= marks < 60:
        return 'B-'
    elif 60 <= marks < 65:
        return 'B'
    elif 65 <= marks < 70:
        return 'B+'
    elif 70 <= marks < 75:
        return 'A-'
    elif 75 <= marks < 80:
        return 'A'
    else:  # marks >= 80
        return 'A+'


student_marks = 52

student_grade = assign_grade(student_marks)
print(f"The grade for a student with {student_marks} marks is: {student_grade}")





# using R programming




# assign_grade <- function(marks) {
#   if (marks < 40) {
#     return('F')
#   } else if (marks >= 40 && marks < 45) {
#     return('D')
#   } else if (marks >= 45 && marks < 50) {
#     return('C')
#   } else if (marks >= 50 && marks < 55) {
#     return('C+')
#   } else if (marks >= 55 && marks < 60) {
#     return('B-')
#   } else if (marks >= 60 && marks < 65) {
#     return('B')
#   } else if (marks >= 65 && marks < 70) {
#     return('B+')
#   } else if (marks >= 70 && marks < 75) {
#     return('A-')
#   } else if (marks >= 75 && marks < 80) {
#     return('A')
#   } else {
#     return('A+')
#   }
# }


# student_marks <- 52
# student_grade <- assign_grade(student_marks)
# cat("The grade for a student with", student_marks, "marks is:", student_grade)

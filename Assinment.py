assignment1_grade = float(input('Enter Assignment 1 Grade (0-100) : '))
assignment2_grade = float(input('Enter assignment 2 Grade (0-100) : '))
assignment3_grade = float(input('Enter assignment 3 Grade (0-100) : '))
assignment4_grade = float(input('Enter assignment 4 Grade (0-100) : '))

test1_grade = float(input('Enter test 1 grade (0-100): '))
test2_grade = float(input('Enter test 2 grade (0-100): '))

TotalAssignment = (assignment1_grade + assignment2_grade + assignment3_grade + assignment4_grade) / 4 * 0.45
totalTest = (test1_grade + test2_grade) / 2 * 0.55

finalGrade = TotalAssignment + totalTest

if finalGrade >= 90:
        print(f'Final grade: {finalGrade: .1f} A')
elif finalGrade >= 89:
        print(f'Final grade : {finalGrade: .1f} B')
elif finalGrade >= 70:
        print(f'Final grade : {finalGrade: .1f} C')
elif finalGrade >=69:
        print(f'Final grade : {finalGrade: .1f} D')
else:
        print(f'Final grade : {finalGrade: .1f} F')
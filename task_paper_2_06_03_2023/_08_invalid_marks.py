# 8. Take the input marks from the user using input() function and 
# find out the grade of the students. Note the grading will be in 
# this manner – (100 – 91) – A1, (90-81) – A2, (80-71) – B1, 
# (70-61) – B2, (60- 51) – C1 (50-40) – C2 and less than 40 students 
# will ‘Fail’. Also make sure the user should input the  marks in 
# the range 0<=marks<=100, if the user will input some other marks 
# it should print invalid  marks. 

marks = int(input("Enter the marks obtained by the student (out of 100): "))

# Check if the marks are valid
if marks < 0 or marks > 100:
    print("Invalid marks!")
else:
    # Assign grade based on marks obtained
    if marks >= 91:
        grade = "A1"
    elif marks >= 81:
        grade = "A2"
    elif marks >= 71:
        grade = "B1"
    elif marks >= 61:
        grade = "B2"
    elif marks >= 51:
        grade = "C1"
    elif marks >= 40:
        grade = "C2"
    else:
        grade = "Fail"
        
    print(f"The grade obtained by the student is {grade}")

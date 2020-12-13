




"""
Plain English
start
create a list to store 5 number (float)
capture user's input for their grades
each time we capture the user's input, we append the number to the list
sort the list ascending, then splice the items starrting at index 2
once we have three highest number in the full list, we sum them up and divide by 3 oupt a message to the users
end
"""

grades = []

grade = input  ("Enter the 1st grade: ")
grades.append(float(grade)) 

grade = input  ("Enter the 2nd grade: ")
grades.append(float(grade))

grade = input  ("Enter the 3rd grade: ")
grades.append(float(grade))

grade = input  ("Enter the 4th grade: ")
grades.append(float(grade))

grade = input  ("Enter the 5th grade: ")
grades.append(float(grade))

grades.sort()
grades = grades[2:]
grades = sum(grades)
result = grades /3

print("Average Grade {0:.2f}%$".format(result))
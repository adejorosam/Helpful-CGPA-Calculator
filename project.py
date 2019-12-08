print('Welcome to CGPA calculator. It allows you claculates your CGPA without stress.')
no_of_courses = int(input('How many number of courses would you be filling in?'))
total_unit = 0
result_atm = 0 #Result at the moment
for i in range(no_of_courses):
    courses = input('Enter your course: ')
    score = int(input('Enter your score: '))
    unit = int(input('Enter the unit of the course: '))
    total_unit += unit
    if score >= 70:
        result_atm += unit * 5
    elif score >= 60:
        result_atm += unit * 4
    elif score >= 50:
        result_atm += unit * 3
    elif score >= 45:
        result_atm += unit * 2
    elif score >= 40:
        result_atm += unit * 1
    elif score <= 40:
        result_atm += unit * 0
print(f'Your CGPA is {result_atm/total_unit}')




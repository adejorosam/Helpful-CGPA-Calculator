import mysql.connector

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
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database = "testdb")
    my_cursor = mydb.cursor()
    sql = 'INSERT INTO cgpacalc (courses,unit,score,total_unit) VALUES (%s,%s,%s)'
    value = (courses,unit,score)
    my_cursor.execute(sql,value)
    mydb.commit()
print(f'Your CGPA is {result_atm/total_unit}')






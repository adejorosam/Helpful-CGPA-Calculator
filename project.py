try:
    from random import randint
    import mysql.connector
except ImportError:
    print("Can't load modules for now!")


def checkAgain():
    ask = input('You wanna check for a friend or you still wanna check again?').lower()
    while True:
        if ask == 'yes':
            CGPACalc()
        if ask == 'no':
            print('Thanks for using this application.')
            exit()
        else:
            print('You entered a wrong input')
            ask = input('You wanna check for a friend or you still wanna check again?').lower()
   

def CGPACalc():
    print('Welcome to CGPA calculator. It allows you calculates your CGPA without stress.')
    username = input("I gotchu! What's the name?")
    random_int = str(randint(1,100000))
    peculiar_name = username + random_int

    try:
        no_of_courses = int(input('How many number of courses would you be filling in?'))
    except ValueError:
        print('Please enter a valid value not a string.')
    except NameError:
        print('Please enter a valid value not a string')
    
    total_unit = 0
    result_atm = 0 #Result at the moment

    try:
        for i in range(no_of_courses):

            courses = input('Enter your course: ')
            try:
                score = int(input('Enter your score: '))
                unit = int(input('Enter the unit of the course: '))
            except  ValueError:
                print('Please enter an integer: ')
        
            try:
                total_unit += unit
            except NameError:
                print('Check your inputs and try again.')
            
            try:
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
                elif score <= 39:
                    result_atm += unit * 0
            except NameError:
                print('Erorr!') 
            
            try:
                mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database = "testdb")
                my_cursor = mydb.cursor()
                sql = 'INSERT INTO cgpacalc (name,courses,unit,score) VALUES (%s,%s,%s,%s)'
                value = (peculiar_name,courses,unit,score)
                my_cursor.execute(sql,value)
                mydb.commit()
            except mysql.connector.errors.InterfaceError:
                print("It's not us. We will get it soretd out!")
    except NameError:
        print('Fix it!')

    try:
        print(f'Your CGPA is {result_atm/total_unit}')
        
    except ZeroDivisionError:
        print('Division by zero error')
    
    try:
        d = ('''SELECT courses,unit,score FROM cgpacalc WHERE name = %s''')
        my_cursor.execute(d,(peculiar_name,))
        my_result = my_cursor.fetchall()
        print(f'Hi {username}, your results are listed below.')
        for x in my_result:
            print(x) 
            
    except:
        print('Something went wrong!')

    checkAgain()   
       
CGPACalc()

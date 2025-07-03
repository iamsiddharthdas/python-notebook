import psycopg2

def create_table():
    try:
        cursor.execute("create table student_details(sid serial primary key, name text, email text unique, grade text)")
        connection.commit()
    except Exception as e:
        print(e)

def insertion_data(name, email, grade):
    try:
        cursor.execute("insert into student_details (name, email, grade) values(%s, %s, %s)", (name, email, grade))
        connection.commit()
    except Exception as e:
        print(e)

def get_all_data():
    try:
        cursor.execute("select * from student_details;")
        data = cursor.fetchall()
        for i in data:
            print(i[0], i[1], i[2], i[3])
    except Exception as e:
        print(e)

def find_User(email1):
    try:
        cursor.execute("select * from student_details where email=%s", (email1,))
        exist = cursor.fetchall()
        if len(exist) > 0:
            print("User Exist")
        else:
            print("No User Found")
    except Exception as e:
        print(e)

def update_email(sno):
    try:
        email1 = input("Please the updated email ")
        cursor.execute("update student_details set email=%s where sid=%s", (email1, sno))
        connection.commit()
    except Exception as e:
        print(e)

def delete_user_with_email(email1):
    try:
        cursor.execute("select * from student_details where email=%s", (email1,))
        exist = cursor.fetchall()
        if len(exist) == 0:
            print("No user Exist with this email")
            return
        else:
            cursor.execute("delete from student_details where email=%s", (email1,))
            connection.commit()
            print("Operation Succeeded")
    except Exception as e:
        print(e)

connection = psycopg2.connect(
    database='student',
    user='postgres',
    password='lokeshdevcoder',
    host='localhost'
)

cursor = connection.cursor()

delete_user_with_email('abhinash.999@mail.com')
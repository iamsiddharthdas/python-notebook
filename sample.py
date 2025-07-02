import psycopg2

connection = psycopg2.connect(database='siddharth' ,host='localhost', user= 'postgres', password='iavenjq')

cur = connection.cursor()

if cur:
    cur.execute('''
                create table std_details(sid serial primary key, name varchar (26), email varchar (100));
                ''')

connection.commit ()

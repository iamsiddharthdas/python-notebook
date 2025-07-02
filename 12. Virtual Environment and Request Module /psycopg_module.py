'''
psycopg2



Psycopg is a PostgreSQL adapter for the Python programming language.
It is a wrapper for the libpq, the official PostgreSQL client library.

( libpq is a set of library functions that allow client programs
to pass queries to the PostgreSQL backend server and 
to receive the results of these queries.)

- Installation
pip install psycopg2-binary
pip3 install psycopg2-binary ( if not working in mac )


psycopg vs psycopg-binary

- psycopg2-binary is a binary version of psycopg2 
that is faster and more secure than the standard psycopg2 library.

- The psycopg2-binary package is meant for beginners 
to start playing with Python and PostgreSQL without the need to meet the build requirements.
But, for production use, you should use the standard psycopg2 package.

'''

# SYNTAX

import psycopg2 

# Connect to your postgres DB
conn = psycopg2.connect("dbname=test user=postgres")

# Open a cursor to perform database operations
cur = conn.cursor()

# Execute a query
cur.execute("SELECT * FROM my_data")

# Retrieve query results
records = cur.fetchall()


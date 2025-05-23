# Function with args and kwargs:
'''
Args and kwargs allow us to accept an arbitrary number of positional and keyword arguments in a function.

def student_info(*args, **kwargs):
    print(args)
    print(kwargs)
    
Positional arguments e.g. Maths, Science, English
Keyword arguments e.g. name, age, class, section

example:
def student_info(*args, **kwargs):
    print(args)
    print(kwargs)
student_info('Maths','Art', name='Sid', age=20)

->prints->  ('Maths', 'Art') -> tuple containing positional arguments
            {'name': 'Sid', 'age': 20} -> dictionary containing keyword arguments

Single star (*) is used to unpack the positional arguments into a tuple.
Double star (**) is used to unpack the keyword arguments into a dictionary.

# example:
def student_info(*args, **kwargs):
    print(args)
    print(kwargs)

course = ['Maths', 'Art']
info = {'name': 'Sid', 'age': 20}

student_info(course, info) 

# instead of passing the values individually, it passed the complete list and complete dictionary as a positional argument.
# prints (['Maths', 'Art'], {'name': 'Sid', 'age': 20}) 


student_info(*course, **info)   

# passes the values individually, 
# prints -> ('Maths', 'Art') -> unpacked the tuple
            {'name': 'Sid', 'age': 20} -> unpacked the dictionary   


'''

# Leap year and days in month

# Number of days per month. First value placeholder for indexing purposes.
month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_leap(year):
    ''' Returns True for leap years, False for non-leap years. '''
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def days_in_month(year, month):
    ''' Returns number of days in that month in that year. '''
    
    
    # year 2017 (example)
    # month 2 (February)
    if month < 1 or month > 12:
        return 'Invalid month'
    if month == 2 and is_leap(year):
        return 29
    return month_days[month]

is_leap(2020) # prints True
days_in_month(2017, 2) # prints 28

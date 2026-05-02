#Week 13, Program 2 - Cities Database
#Caiden Heinrichs
#05/01/26

import sqlite3


def main():
    #Connect to the database
    connection = sqlite3.connect('cities.db')
    #Add the cursor
    cursor = connection.cursor()

    display_cities(cursor)

def display_cities(cursor):
    print('Contents of cities.db:')
    cursor.execute('SELECT * FROM Cities')
    results = cursor.fetchall()
    for row in results:
        print(f'{row[0]:<3}{row[1]:20}{row[2]:,.0f}')

if __name__ == '__main__':
    main()

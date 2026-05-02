#Week 13, Program 1 - Cities Database
#Caiden Heinrichs
#05/01/26

import sqlite3

def main():
    #Connect to the database
    connection = sqlite3.connect('cities.db')
    #Add the cursor
    cursor = connection.cursor()

    #Add the Cities table
    add_cities_table(cursor)
    # Add rows to the Cities table
    add_cities(cursor)
    #Commit the changes
    connection.commit()
    #Close the connection
    connection.close()

# The add_cities_table adds the Cities table to the database.
def add_cities_table(cursor):
    # If the table already exists, drop it.
    cursor.execute('DROP TABLE IF EXISTS Cities')

    # Create the table.
    cursor.execute('''CREATE TABLE Cities (CityID INTEGER PRIMARY KEY NOT NULL,
                                        CityName TEXT,
                                        Population REAL)''')

# The add_cities function adds 20 rows to the Cities table.
def add_cities(cursor):
    cities_pop = [(1,'Tokyo',38001000),
                  (2,'Delhi',25703168),
                  (3,'Shanghai',23740778),
                  (4,'Sao Paulo',21066245),
                  (5,'Mumbai',21042538),
                  (6,'Mexico City',20998543),
                  (7,'Beijing',20383994),
                  (8,'Osaka',20237645),
                  (9,'Cairo',18771769),
                  (10,'New York',18593220),
                  (11,'Dhaka',17598228),
                  (12,'Karachi',16617644),
                  (13,'Buenos Aires',15180176),
                  (14,'Kolkata',14864919),
                  (15,'Istanbul',14163989),
                  (16,'Chongqing',13331579),
                  (17,'Lagos',13122829),
                  (18,'Manila',12946263),
                  (19,'Rio de Janeiro',12902306),
                  (20,'Guangzhou',12458130)]
    
    for row in cities_pop:
        cursor.execute('''INSERT INTO Cities (CityID, CityName, Population)
                       VALUES (?, ?, ?)''', (row[0], row[1], row[2]))


if __name__ == '__main__':
    main()

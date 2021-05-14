import psycopg2 

connection = psycopg2.connect('dbname=example')

cursor = connection.cursor()

cursor.execute('''
    CREATE TABLE table3 (
        id INTEGER PRIMARY KEY,
        completed BOOLEAN NOT NULL DEFAULT False
    );
''')

cursor.execute('INSERT INTO table3 (id, completed) VALUES (1, true);')

connection.commit()

connection.close()
cursor.close()

# in bash: python3 demo.py
# psql example
# \dt
# // verify that table3 is there
# \d table 3
# select * from table3; 
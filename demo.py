import psycopg2 

connection = psycopg2.connect('dbname=example')

cursor = connection.cursor()

cursor.execute('DROP TABLE IF EXISTS table3;')

cursor.execute('''
    CREATE TABLE table3 (
        id INTEGER PRIMARY KEY,
        completed BOOLEAN NOT NULL DEFAULT False
    );
''')

cursor.execute('INSERT INTO table3 (id, completed) VALUES (1, true);')

cursor.execute('INSERT INTO table3 (id, completed) VALUES (%s, %s);', (2, True))

cursor.execute('INSERT INTO table3 (id, completed)' +
' VALUES (%(id)s, %(completed)s);', {
    'id': 3,
    'completed': False
})

SQL = 'INSERT INTO table3 (id, completed) VALUES (%(id)s, %(completed)s);'

data = {
    'id': 4,
    'completed': False
}
cursor.execute(SQL, data)

# (1):
cursor.execute('SELECT * from table3;')

result = cursor.fetchall()
print(result) # [(1, True), (2, True), (3, False), (4, False)]

connection.commit()

connection.close()
cursor.close()

# in bash: conda deactivate
# python3 demo.py
# psql example
# \dt
# // verify that table3 is there
# \d table 3
# select * from table3;

# We can use string interpolation to compose an SQL query using python strings, in two ways:
# 1. Using `%s`, passing in a tuple as a 2nd argument in `cursor.execute()`
# 2. Using named string parameters %(foo)s, passing in a dictionary instead
# in bash, run it etc: python3 demo.py
# psql example
# example=# select * from table3;

# We're doing a select * statement on the records we insterted (1)
# python3 demo.py
# the above returns as per # (1)
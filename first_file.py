import mysql.connector

HOST = "sql7.freesqldatabase.com"
USER = "sql7634893"
PASSWORD = "8RT5Q9GPpZ"

network_project_db = mysql.connector.connect(
    host=HOST,
    user=USER,
    password=PASSWORD
)

mycursor = network_project_db.cursor()

mycursor.execute("SHOW DATABASES")

for x in mycursor:
    print(x)

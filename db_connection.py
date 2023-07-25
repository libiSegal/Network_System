import mysql.connector

HOST = "sql7.freesqldatabase.com"
USER = "sql7634893"
PASSWORD = "8RT5Q9GPpZ"
DATABASE = "sql7634893"

network_project_db = mysql.connector.connect(
    host=HOST,
    user=USER,
    password=PASSWORD,
    database=DATABASE
)

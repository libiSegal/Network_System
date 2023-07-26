import mysql.connector
from mysql.connector import Error

HOST = "sql7.freesqldatabase.com"
USER = "sql7634893"
PASSWORD = "8RT5Q9GPpZ"
DATABASE = "sql7634893"


def create_server_connection(host_name, user_name, user_password, database):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=database
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection


def execute_query(connection, query):
    try:
        cursor = connection.cursor(buffered=True)
        cursor.execute(query)
        result = cursor.fetchall()
        connection.commit()
        print("Query successful")
        return result
    except Error as err:
        print(f"Error: '{err}'")


db_connection = create_server_connection(HOST, USER, PASSWORD, DATABASE)

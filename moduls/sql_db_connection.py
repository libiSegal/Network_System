import mysql.connector
from mysql.connector import Error

HOST = "sql7.freesqldatabase.com"
USER = "sql7636694"
PASSWORD = "9jmGbPjhLU"
DATABASE = "sql7636694"


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
        connection.commit()
        id = cursor.lastrowid
        return id
    except Error as err:
        print(f"Error: '{err}'")


def read_query(connection, query):
    cursor = connection.cursor(buffered=True)
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as err:
        print(f"Error: '{err}'")


db_connection = create_server_connection(HOST, USER, PASSWORD, DATABASE)

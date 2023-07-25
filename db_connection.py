import mysql.connector
from mysql.connector import Error


HOST = "sql7.freesqldatabase.com"
USER = "sql7634893"
PASSWORD = "8RT5Q9GPpZ"


def create_server_connection(host_name, user_name, user_password):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection


db_connection = create_server_connection(HOST, USER, PASSWORD)

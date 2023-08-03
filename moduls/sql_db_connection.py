import mysql.connector
from mysql.connector import Error
from log_file import logger

HOST = "sql7.freesqldatabase.com"
USER = "sql7636694"
PASSWORD = "9jmGbPjhLU"
DATABASE = "sql7636694"


@logger
def create_server_connection(host_name, user_name, user_password, database):
    """
    Connect to sql server database
    :param host_name: the host name of the sql server
    :param user_name:username of sql server
    :param user_password: the password on sql server
    :param database:the database name
    :return:
    """
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


@logger
def execute_query(connection, query):
    """
    This function execute queries in db
    :param connection: the connection to the db
    :param query: the query ti execute
    :return:the new id
    """
    try:
        cursor = connection.cursor(buffered=True)
        cursor.execute(query)
        connection.commit()
        id = cursor.lastrowid
        return id
    except Error as err:
        print(f"Error: '{err}'")


@logger
def read_query(connection, query):
    """
    This function run read function on sql
    :param connection: the connection to sql
    :param query:the query to run
    :return: the result of the query
    """
    cursor = connection.cursor(buffered=True)
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as err:
        print(f"Error: '{err}'")


db_connection = create_server_connection(HOST, USER, PASSWORD, DATABASE)

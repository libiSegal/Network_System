import mysql.connector
from mysql.connector import Error
import first_file

connection = first_file.db_connection


def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query successful")
    except Error as err:
        print(f"Error: '{err}'")


create_technicians_table = """
CREATE TABLE Technicians (
    Id INT PRIMARY KEY,
    Username VARCHAR(255),
    Password VARCHAR(255)
);
"""

create_clients_table ="""
CREATE TABLE Clients (
    Id INT PRIMARY KEY,
    Name VARCHAR(255)
);
"""

create_user_client_connection_table = """
CREATE TABLE User_Client_Connection (
    Id INT PRIMARY KEY,
    TechnicianId INT FOREIGN KEY REFERENCES Technician(Id),
    ClientId INT FOREIGN KEY REFERENCES Clients(Id)
);
"""

create_network_table = """
CREATE TABLE Network (
    Id INT PRIMARY KEY,
    ClientId INT FOREIGN KEY REFERENCES Clients(Id),
    Date DATE,
    PremiseLocationName VARCHAR(255)
);
"""

create_device_table = """
CREATE TABLE Device (
    Id INT PRIMARY KEY,
    MACAddress VARCHAR(255),
    NetworkId INT FOREIGN KEY REFERENCES Network(Id)
);
"""

create_communication_table = """
CREATE TABLE Communication (
    Id INT PRIMARY KEY,
    SourceId INT FOREIGN KEY REFERENCES Device(Id),
    DestinationId INT FOREIGN KEY REFERENCES Device(Id),
    NetworkId INT FOREIGN KEY REFERENCES Network(Id)
);
"""


execute_query(connection, create_technicians_table)
execute_query(connection, create_clients_table)
execute_query(connection, create_user_client_connection_table)
execute_query(connection, create_network_table)
execute_query(connection, create_device_table)
execute_query(connection, create_communication_table)
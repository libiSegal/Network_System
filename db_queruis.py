import mysql.connector
from mysql.connector import Error
import first_file

connection = first_file.db_connection


def execute_query(connection, query):
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        print("Query successful")
    except Error as err:
        print(f"Error: '{err}'")


def read_query(connection, query):
    cursor = connection.cursor()
    # result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as err:
        print(f"Error: '{err}'")


create_technicians_table = """
CREATE TABLE Technicians (
    Id INT AUTO_INCREMENT PRIMARY KEY,
    Username VARCHAR(255),
    Password VARCHAR(255)
);
"""

create_clients_table = """
CREATE TABLE Clients (
    Id INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(255)
);
"""


create_technician_client = """
CREATE TABLE Technician_Client (
    Id INT AUTO_INCREMENT PRIMARY KEY,
    TechnicianId INT,
    ClientId INT,
    FOREIGN KEY (TechnicianId) REFERENCES Technicians(Id),
    FOREIGN KEY (ClientId) REFERENCES Clients(Id)
);
"""

create_network_table = """
CREATE TABLE Network (
    Id INT AUTO_INCREMENT PRIMARY KEY,
    ClientId INT,
    Date DATE,
    PremiseLocationName VARCHAR(255),
    FOREIGN KEY (ClientId) REFERENCES Clients(Id)
);
"""

create_device_table = """
CREATE TABLE Device (
    Id INT AUTO_INCREMENT PRIMARY KEY,
    MACAddress VARCHAR(255),
    NetworkId INT,
    FOREIGN KEY (NetworkId) REFERENCES Network(Id)
);
"""

create_communication_table = """
CREATE TABLE Communication (
    Id INT AUTO_INCREMENT PRIMARY KEY,
    SourceId INT,
    DestinationId INT,
    NetworkId INT,
    FOREIGN KEY (SourceId) REFERENCES Device(Id),
    FOREIGN KEY (DestinationId) REFERENCES Device(Id),
    FOREIGN KEY (NetworkId) REFERENCES Network(Id)
);
"""

pop_technicians = """
INSERT INTO Technicians (Username, Password) VALUES 
    ('Eli_Marom', 'abc123');"""

q1 = """
SELECT *
FROM Technicians;
"""
d1 ="""
DROP TABLE Technicians
"""


# results = read_query(connection, q1)
# for result in results:
#   print(result)

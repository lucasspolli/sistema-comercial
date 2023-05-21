import sqlite3

connection = sqlite3.connect("../Database/database.db")
cursor = connection.cursor()

def createClientsTable():
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id          INTEGER AUTOINCREMENT PRIMARY KEY,
            username    VARCHAR(30) NOT NULL UNIQUE,
            email       VARCHAR(50) NOT NULL UNIQUE,
            password    VARCHAR(30),
            cart        VARCHAR(60) NOT NULL
        )''')

def createRegistredProductsTable():
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id          INTEGER AUTOINCREMENT PRIMARY KEY,
            name        VARCHAR(50) NOT NULL UNIQUE,
            price       REAL NOT NULL,
            quantify    INTEGER NOT NULL
        )''')
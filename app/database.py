import logging
import os

import mysql.connector
from mysql.connector import Error

logger = logging.getLogger(__name__)
class Database:
    _instance = None
    _connection = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._connection = cls._create_connection()
        return cls._instance

    @staticmethod
    def _create_connection():
        try:
            connection = mysql.connector.connect(
                host=os.getenv("MYSQL_HOST"),
                user=os.getenv("MYSQL_USER"),
                password=os.getenv("MYSQL_PASSWORD"),
                database=os.getenv("MYSQL_DB")
            )
            if connection.is_connected():
                logger.info("Connection to MySQL database was successful")
                return connection
        except Error as e:
            # implementar logging por error de conexión
            error = f"Error connecting to MySQL database: {e}"
            logger.exception(error)
            return None

    @staticmethod
    def get_connection():
        if Database._connection is None or not Database._connection.is_connected():
            Database._connection = Database._create_connection()
        return Database._connection

    @staticmethod
    def close_connection():
        if Database._connection and Database._connection.is_connected():
            Database._connection.close()
            logger.info("The connection is closed")

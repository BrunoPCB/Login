import mysql.connector
from mysql.connector import connection, errorcode

class ConnectDatabase:
    def __init__(self):
        self.__lines = None
        self.__connection = None
        self.__config = {}

    @property
    def config(self):
        return self.__config

    @property
    def connection(self):
        return self.__connection

    def get_config(self):
        # Search for config data, to open the database
        self.__lines = None
        with open('config.con') as conf:
            self.__lines = conf.readlines()

        for line in self.__lines:
            key_value = line.split(':')
            key = key_value[0].replace("'","")
            value = key_value[1].replace("'","")

            value = value.replace('\n', '')

            if value in ['True', 'False']:
                value = bool(value)

            self.__config[key] = value

    def connect(self):
        try:
            self.get_config()
            self.__connection = connection.MySQLConnection(**self.__config)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print('Error with username or password.')
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print('Database does not exists.')
            else:
                print(f'Error: {err.msg}')
        return False


    def close_connection(self):
        self.__connection.close()
from Connection import ConnectDatabase

from Utils import DB_USER


class User:
    def __init__(self):
        self.__username = ''
        self.__password = ''

    # --------- Getter/Setters --------- #

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, username):
        self.__username = username

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password):
        self.__password = password

    # ------------ Methods ------------- #

    def login_verification(self):
        # here goes the verification in the database, if
        # there is an account
        pass

    def encrypt_password(self):
        # here we will encrypt our password, to make it safer
        pass

    # ------------ DB Access ------------- #

    def add_data(self):
        query = (f"INSERT INTO {DB_USER} (user_name, pass_word) "
                 f"VALUES (%s, %s)")
        values = (self.__username, self.__password)

        myconnection = ConnectDatabase()
        try:
            myconnection.connect()
            cursor = myconnection.connection.cursor()

            cursor.execute(query, values)

            myconnection.connection.commit()
        finally:
            myconnection.close_connection()

    def select_data(self):
        query = f"SELECT user_name, pass_word FROM {DB_USER}"
        data = []

        myconnection = ConnectDatabase()
        try:
            myconnection.connect()
            cursor = myconnection.connection.cursor()

            cursor.execute(query)

            for us, ps in cursor:
                data.append([us, ps])

            return data

        finally:
            myconnection.close_connection()
        pass

    def update_data(self):
        # Here goes data update
        pass

    def delete_data(self):
        # Here goes the delete of data
        pass

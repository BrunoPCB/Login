from Connection import ConnectDatabase

from Utils import DB_USER


class User:
    def __init__(self):
        # self.__id = 0
        self.__username = ''
        self.__password = ''

    # --------- Getter/Setters --------- #
    # @property
    # def id(self):
    #     return self.__id
    #
    # @id.setter
    # def id(self, code):
    #     self.__id = code

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
        search_data = True

        select_return = self.select_data(search_data)

        return len(select_return) > 0


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
        except myconnection.connection.IntegrityError:
            print("Failed to insert values")
        finally:
            myconnection.close_connection()

    def select_data(self, where_clause=False):
        query = f"SELECT id, user_name, pass_word FROM {DB_USER} "
        if where_clause:
            query += f"WHERE user_name = \'{self.__username}\' and pass_word = \'{self.__password}\'"
        data = []

        myconnection = ConnectDatabase()
        try:
            myconnection.connect()
            cursor = myconnection.connection.cursor()

            cursor.execute(query)

            for code, us, ps in cursor:
                data.append([code, us, ps])

            return data

        finally:
            myconnection.close_connection()

    def update_data(self, code):
        query = (f"UPDATE {DB_USER} "
                 f"SET user_name = '{self.__username}', pass_word = '{self.__password}' "
                 f"WHERE id = {code}")

        myconnection = ConnectDatabase()
        try:
            myconnection.connect()
            cursor = myconnection.connection.cursor()

            cursor.execute(query)

            myconnection.connection.commit()
        finally:
            myconnection.close_connection()

    def delete_data(self, code, code_end=0):
        if code_end != 0:
            query = (f"DELETE FROM {DB_USER} "
                     f"WHERE id BETWEEN {code} AND {code_end}")
            #values = (code, code_end)
        else:
            query = (f"DELETE FROM {DB_USER} "
                     f"WHERE id = {code}")
            #values = code

        myconnection = ConnectDatabase()
        try:
            myconnection.connect()
            cursor = myconnection.connection.cursor()

            cursor.execute(query)

            myconnection.connection.commit()
        finally:
            myconnection.close_connection()
        pass

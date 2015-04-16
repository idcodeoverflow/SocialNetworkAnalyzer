from mysql.connector import errorcode
import mysql.connector

__author__ = 'David'


class DBConnection:
    def __init__(self):
        try:
            self.password = 'remex2013'
            self.user = 'root'
            self.host = 'localhost'
            self.database = 'fb_dataset'
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print('Something is wrong with your user name or password.')
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print('Database does not exist.')
            else:
                print(err)


    def closeConnection(self):
        try:
            self.cnx.close()
        except mysql.connector.Error:
            print('Something went wrong at connection closing.')


    def openConnection(self):
        self.cnx = mysql.connector.connect(user=self.user, password=self.password,
                                           host=self.host,
                                           database=self.database)

        return self.cnx


import mysql

from DBLayout.DBConnection import DBConnection
from EntitiesLayout import FacebookUser


__author__ = 'David'



class FacebookUserDB:

    def __init__(self):
        print('Create object to access table user in DB.')

    def insertUser(self, user: FacebookUser):
        try:
            db = DBConnection()
            cnx = db.openConnection()
            cursor = cnx.cursor()
            addFBUserQuery = 'INSERT INTO user(idUser, facebookUserID, firstName, gender, lastName, link, locale, name, username)' \
                             'VALUES (NULL, %s, %s, %s, %s, %s, %s, %s, %s);'
            dataUser = (user.facebookUserId, user.firstName, user.gender, user.lastName, user.link, user.locale, user.name, user.userName)

            cursor.execute(addFBUserQuery, dataUser)
            cnx.commit()
            cursor.close()
            db.closeConnection()

        except mysql.connector.Error:
            print('Error writing a Facebook User in the DB.')


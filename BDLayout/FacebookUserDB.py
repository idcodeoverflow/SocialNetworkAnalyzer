import mysql

from BDLayout.DBConnection import DBConnection
from EntitiesLayout import FacebookUser


__author__ = 'David'

from __future__ import print_function
from datetime import date, datetime, timedelta


class FacebookUserDB:

    def insertUser(self, user: FacebookUser):
        try:
            cnx = DBConnection()
            cursor = cnx.cursor()
            addFBUserQuery = 'INSERT INTO user(idUser, facebookUserID, firstName, gender, lastName, link, locale, name, username)' \
                             'VALUES (NULL, %s, %s, %s, %s, %s, %s, %s, %s);'
            dataUser = (user.facebookUserId, user.firstName, user.gender, user.lastName, user.link, user.locale, user.name, user.userName)

            cursor.execute(addFBUserQuery, dataUser)
            cnx.commit()
            cursor.close()
            cnx.closeConnection()

        except mysql.connector.Error:
            print('Error writing a Facebook User in the DB.')


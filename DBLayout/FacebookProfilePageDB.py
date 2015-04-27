import mysql
from DBLayout.FacebookUserDB import FacebookUserDB

from EntitiesLayout.FacebookProfilePage import FacebookProfilePage
from DBLayout.DBConnection import DBConnection
from EntitiesLayout.FacebookUser import FacebookUser


__author__ = 'David'

class FacebookProfilePageDB:

    profilesPages = []

    def __init__(self):
        self.db = DBConnection()
        self.profilesPages.clear()

    def insertProfilePage(self, page: FacebookProfilePage):
        try:
            cnx = self.db.openConnection()
            cursor = cnx.cursor()
            addFBUserQuery = 'INSERT INTO profilePage(idprofilePage, profilePage, facebookUserID, visitedOn)' \
                             ' VALUES (NULL, %s, %s, NOW());'
            dataUser = (page.profilePage, page.facebookUserId)

            cursor.execute(addFBUserQuery, dataUser)
            cnx.commit()
            cursor.close()
            self.db.closeConnection()

        except mysql.connector.Error as err:
            print(err)
            print('Error writing a Facebook User Profile in the DB.')
        except AttributeError as err:
            print('Register can\'t be stored.')

    def readProfilesPagesFromUser(self, user: FacebookUser):
        print('Getting User Profile Pages.')

        try:
            cnx = self.db.openConnection()
            cursor = cnx.cursor()
            readFBUserQuery = 'SELECT idProfilePage, profilePage, facebookUserID, visitedOn FROM profilePage WHERE facebookUserID = %s'

            dataUser = (user.facebookUserId,)

            cursor.execute(readFBUserQuery, dataUser)

            for (idProfilePage, profilePage, facebookUserID, visitedOn) in cursor:
                self.profilesPages.append(FacebookProfilePage(user, profilePage))
            cursor.close()
            self.db.closeConnection()

        except mysql.connector.Error as ex:
            print(ex)
            print('Error reading a Facebook Profile in the DB.')
        return self.profilesPages

    def readProfilesPages(self):
        print('Getting Profiles Pages.')

        try:
            cnx = self.db.openConnection()
            cursor = cnx.cursor()
            userAccess = FacebookUserDB()
            readFBProfilesQuery = 'SELECT idProfilePage, profilePage, facebookUserID, visitedOn FROM profilePage'

            cursor.execute(readFBProfilesQuery)

            for (idProfilePage, profilePage, facebookUserID, visitedOn) in cursor:
                self.profilesPages.append(FacebookProfilePage(userAccess.readUser(facebookUserID), profilePage))

            cursor.close()
            self.db.closeConnection()

        except mysql.connector.Error as ex:
            print(ex)
            print('Error reading a Facebook Profile in the DB.')
        return self.profilesPages
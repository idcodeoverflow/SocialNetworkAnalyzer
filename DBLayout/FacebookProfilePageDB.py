import mysql
from EntitiesLayout.FacebookProfilePage import FacebookProfilePage
from DBLayout.DBConnection import DBConnection


__author__ = 'David'

class FacebookProfilePageDB:

    def insertProfilePage(self, page: FacebookProfilePage):
        try:
            db = DBConnection()
            cnx = db.openConnection()
            cursor = cnx.cursor()
            addFBUserQuery = 'INSERT INTO profilePage(idprofilePage, profilePage, facebookUserID, visitedOn)' \
                             'VALUES (NULL, %s, %s, NOW());'
            dataUser = (page.profilePage, page.facebookUserId)

            cursor.execute(addFBUserQuery, dataUser)
            cnx.commit()
            cursor.close()
            db.closeConnection()

        except mysql.connector.Error as err:
            print(err)
            print('Error writing a Facebook User Profile in the DB.')
        except AttributeError as err:
            print('Register can\'t be stored.')
import mysql

from DBLayout.DBConnection import DBConnection
from EntitiesLayout.FacebookUser import FacebookUser


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

        except mysql.connector.Error as err:
            print(err)
            print('Error writing a Facebook User in the DB.')
        except AttributeError as err:
            print('Register can\'t be stored.')

    def readUser(self, id: int):
        user = FacebookUser({})
        mp = {}
        try:
            db = DBConnection()
            cnx = db.openConnection()
            cursor = cnx.cursor()
            readFBUserQuery = ("SELECT idUser, facebookUserID, firstName, gender, lastName, link, locale, name, username "
                               "FROM user WHERE facebookUserID = %s;")

            dataUser = (id,)

            cursor.execute(readFBUserQuery, dataUser)

            for (idUser, facebookUserID, firstName, gender, lastName, link, locale, name, username) in cursor:
                mp['id'] = facebookUserID
                mp['first_name'] = firstName
                mp['gender'] = gender
                mp['last_name'] = lastName
                mp['link'] = link
                mp['locale'] = locale
                mp['name'] = name
                mp['username'] = username
                user = (FacebookUser(mp))

            cursor.close()
            db.closeConnection()

        except mysql.connector.Error as ex:
            print(ex)
            print('Error reading a Facebook User in the DB.')
        return user

    def readUsers(self):
        users = []
        mp = {}
        try:
            db = DBConnection()
            cnx = db.openConnection()
            cursor = cnx.cursor()
            readFBUserQuery = 'SELECT idUser, facebookUserID, firstName, gender, lastName, link, locale, name, username ' \
                              'FROM user;'

            cursor.execute(readFBUserQuery)

            for (idUser, facebookUserID, firstName, gender, lastName, link, locale, name, username) in cursor:
                mp['id'] = facebookUserID
                mp['first_name'] = firstName
                mp['gender'] = gender
                mp['last_name'] = lastName
                mp['link'] = link
                mp['locale'] = locale
                mp['name'] = name
                mp['username'] = username
                users.append(FacebookUser(mp))

            cursor.close()
            db.closeConnection()

        except mysql.connector.Error as ex:
            print(ex.fp.read())
            print('Error reading a Facebook User in the DB.')
        return users
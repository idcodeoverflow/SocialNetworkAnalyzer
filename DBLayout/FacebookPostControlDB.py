from DBLayout.DBConnection import DBConnection, mysql
from EntitiesLayout.FacebookPostControl import FacebookPostControl

__author__ = 'David'


class FacebookPostControlDB:
    def __init__(self):
        self.db = DBConnection()
        print('Create object to access table user in DB.')

    def insertPostControl(self, post: FacebookPostControl):
        try:
            cnx = self.db.openConnection()
            cursor = cnx.cursor()
            addFBPostControlQuery = 'INSERT INTO postControl(idpostControl, fbid, facebookUserID, visited)' \
                                    'VALUES (NULL, %s, %s, %s);'
            data = (post.fbid, post.facebookUser.facebookUserId, post.visited)

            cursor.execute(addFBPostControlQuery, data)
            cnx.commit()
            cursor.close()
            self.db.closeConnection()

        except mysql.connector.Error as err:
            print(err)
            print('Error writing a Facebook Post Control in the DB.')
        except AttributeError as err:
            print('Register can\'t be stored.')

    def readPostControl(self, id: int):
        postControl = FacebookPostControl({})
        try:
            cnx = self.db.openConnection()
            cursor = cnx.cursor()
            readFBPostControlQuery = ("SELECT idpostControl, fbid, facebookUserID, visited "
                                      "FROM postControl WHERE fbid = %s;")

            data = (id,)

            cursor.execute(readFBPostControlQuery, data)

            for (idpostControl, fbid, facebookUserID, visited) in cursor:
                postControl = (FacebookPostControl(idpostControl, fbid, facebookUserID, visited))

            cursor.close()
            self.db.closeConnection()

        except mysql.connector.Error as ex:
            print(ex)
            print('Error reading a Facebook Post Control in the DB.')
        return postControl

    def readNotVisitedPostsControl(self):
        postsControl = []
        try:
            cnx = self.db.openConnection()
            cursor = cnx.cursor()
            readFBPostControlQuery = ("SELECT idpostControl, fbid, facebookUserID, visited "
                                      "FROM postControl WHERE visited = %s")

            data = (False,)

            cursor.execute(readFBPostControlQuery, data)

            for (idpostControl, fbid, facebookUserID, visited) in cursor:
                postsControl.append(FacebookPostControl(idpostControl, fbid, facebookUserID, visited))

            cursor.close()
            self.db.closeConnection()

        except mysql.connector.Error as ex:
            print(ex)
            print('Error reading not Visited Facebook Posts Control in the DB.')
        return postsControl

    def readPostsControl(self):
        postsControl = []
        try:
            cnx = self.db.openConnection()
            cursor = cnx.cursor()
            readFBPostControlQuery = ("SELECT idpostControl, fbid, facebookUserID, visited "
                                      "FROM postControl")

            cursor.execute(readFBPostControlQuery)

            for (idpostControl, fbid, facebookUserID, visited) in cursor:
                postsControl.append(FacebookPostControl(idpostControl, fbid, facebookUserID, visited))

            cursor.close()
            self.db.closeConnection()

        except mysql.connector.Error as ex:
            print(ex)
            print('Error reading Facebook Posts Control in the DB.')
        return postsControl
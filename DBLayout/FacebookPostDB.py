from DBLayout.DBConnection import DBConnection, mysql
from EntitiesLayout.FacebookPost import FacebookPost

__author__ = 'David'

class FacebookPostDB:

    def __init__(self):
        self.db = DBConnection()
    
    def insertPost(self, post: FacebookPost):
        try:
            cnx = self.db.openConnection()
            cursor = cnx.cursor()
            addFBPostQuery = 'INSERT INTO post(idPost, facebookPostId, createdTime, message, facebookUserId, likesCount)' \
                             'VALUES (NULL, %s, %s, %s, %s, %s);'
            dataPost = (post.facebookPostId, post.createdTime, post.text, post.facebookUserID, post.likeCount)


            print('INSERT INTO post(idPost, facebookPostId, createdTime, message, facebookUserId, likesCount)' \
                             'VALUES (NULL,' + str(post.facebookPostId) + ',' + str(post.createdTime)
                  + ',' + str(post.text) + ',' + str(post.facebookUserID) + ',' + str(post.likeCount))

            cursor.execute(addFBPostQuery, dataPost)
            cnx.commit()
            cursor.close()
            self.db.closeConnection()

        except mysql.connector.Error as err:
            print(err)
            print('Error writing a Facebook post in the DB.')
        except AttributeError as err:
            print(err)
            print('post register can\'t be stored.')

    def readPost(self, fbid: int):
        try:
            mp = {}
            cnx = self.db.openConnection()
            cursor = cnx.cursor()
            readFBPostQuery = ('SELECT idPost, facebookPostId, createdTime, message, facebookUserId, likesCount FROM '
                                  'post WHERE facebookPostId = %s;')

            dataPost = (fbid,)

            cursor.execute(readFBPostQuery, dataPost)

            for (idPost, facebookPostId, createdTime, message, facebookUserId, likesCount) in cursor:
                mp['targetfbid'] = facebookPostId
                mp['createdTime'] = createdTime
                mp['text'] = message
                mp['userId'] = facebookUserId
                mp['likecount'] = likesCount
                post = FacebookPost(mp)

            cursor.close()
            self.db.closeConnection()

        except mysql.connector.Error as ex:
            print(ex)
            print('Error reading a Facebook post in the DB.')
        return post

    def readPosts(self):
        posts = []
        mp = {}
        try:
            cnx = self.db.openConnection()
            cursor = cnx.cursor()

            readFBPostsQuery = ('SELECT idPost, facebookPostId, createdTime, message, facebookUserId, likesCount FROM post;')


            cursor.execute(readFBPostsQuery)

            for (idPost, facebookPostId, createdTime, message, facebookUserId, likesCount) in cursor:
                mp['targetfbid'] = facebookPostId
                mp['createdTime'] = createdTime
                mp['text'] = message
                mp['userId'] = facebookUserId
                mp['likecount'] = likesCount
                post = FacebookPost(mp)
                posts.append(post)

            cursor.close()
            self.db.closeConnection()

        except mysql.connector.Error as ex:
            print(ex.fp.read())
            print('Error reading Facebook posts in the DB.')
        return posts
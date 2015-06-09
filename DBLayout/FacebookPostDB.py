from DBLayout.DBConnection import DBConnection, mysql
from EntitiesLayout.FacebookPost import FacebookPost

__author__ = 'David'

class FacebookPostDB:

    def __init__(self):
        self.db = DBConnection()
    
    def insertPost(self, post: FacebookPost):
        try:
            if post.text == '':
                print('Post text is empty, this post will be ignored.')
                return False
            cnx = self.db.openConnection()
            cursor = cnx.cursor()
            addFBPostQuery = 'INSERT INTO post(idPost, facebookPostId, createdTime, message, facebookUserId, likesCount)' \
                             'VALUES (NULL, %s, %s, %s, %s, %s);'
            dataPost = (post.facebookPostId, post.createdTime, post.text, post.facebookUserID, post.likeCount)

            cursor.execute(addFBPostQuery, dataPost)
            cnx.commit()
            cursor.close()
            self.db.closeConnection()

        except mysql.connector.Error as err:
            print('Error writing a Facebook post in the DB. ' + str(err))
            return False
        except AttributeError as err:
            print('post register can\'t be stored. ' + str(err))
            return False
        return True

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

                post = FacebookPost(facebookPostId, createdTime, message, facebookUserId, likesCount)

            cursor.close()
            self.db.closeConnection()

        except mysql.connector.Error as ex:
            print('Error reading a Facebook post in the DB.' + str(ex))
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

                post = FacebookPost(facebookPostId, createdTime, message, facebookUserId, likesCount)
                posts.append(post)

            cursor.close()
            self.db.closeConnection()

        except mysql.connector.Error as ex:
            print('Error reading Facebook posts in the DB.' + str(ex.fp.read()))
        return posts
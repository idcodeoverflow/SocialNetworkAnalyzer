from mysql.connector import Timestamp

__author__ = 'David'


class FacebookPost:

    facebookPostId = 0
    createdTime = Timestamp()
    text = ''
    facebookUserID = 0
    likeCount = 0


    def __init__(self, mapa: {}):
        try:
            self.facebookPostId = mapa['targetfbid']
            self.createdTime = mapa['createdTime']
            self.text = mapa['text']
            self.facebookUserID = mapa['userId']
            self.likeCount = mapa['likecount']
        except KeyError:
            print('A key is missing, post register will be discarded.')

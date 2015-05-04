from mysql.connector import Timestamp

__author__ = 'David'


class FacebookPost:

    facebookPostId = 0
    createdTime = Timestamp()
    text = ''
    facebookUserID = 0
    likeCount = 0
    shareCount = 0
    commentCount = 0

    def __init__(self, mapa, userId: int, text: str):
        try:
            self.facebookPostId = mapa['targetfbid']
            self.createdTime = mapa['']
            self.text = text
            self.facebookUserID = userId
            self.likeCount = mapa['likecount']
            self.shareCount = mapa['sharecount']
            self.commentCount = mapa['commentcount']
        except KeyError:
            print('A key is missing, register will be discarded.')

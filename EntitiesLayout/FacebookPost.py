from mysql.connector import Timestamp
import datetime

__author__ = 'David'


class FacebookPost:

    facebookPostId = 0
    createdTime = datetime.datetime.now()
    text = ''
    facebookUserID = 0
    likeCount = 0


    def __init__(self, facebookPostId: int = 0, createdTime: Timestamp = datetime.datetime.now(),
                 text: str = '', facebookUserID: int = 0, likeCount: int = 0):
        self.facebookPostId = facebookPostId
        self.createdTime = createdTime
        self.text = text
        self.facebookUserID = facebookUserID
        self.likeCount = likeCount

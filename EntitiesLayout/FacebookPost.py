import datetime

__author__ = 'David'


class FacebookPost:
    def __init__(self):
        self.facebookPostID = 0
        self.createdTime = ""
        self.message = ""
        self.facebookUserID = 0
        self.likesCount = 0

    def __init__(self, facebookPostID: int, createdTime: datetime, message: str, facebookUserID: int, likesCount: int):
        self.facebookPostID = facebookPostID
        self.createdTime = createdTime
        self.message = message
        self.facebookUserID = facebookUserID
        self.likesCount = likesCount

    def __init__(self, mapa):
        self.facebookPostID = mapa['']
        self.createdTime = mapa['']
        self.message = mapa['']
        self.facebookUserID = mapa['']
        self.likesCount = mapa['']
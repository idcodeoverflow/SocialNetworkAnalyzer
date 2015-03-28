
__author__ = 'David'


class FacebookPost:
    def __init__(self):
        self.facebookPostID = 0
        self.createdTime = ""
        self.text = ""
        self.facebookUserID = 0
        self.likeCount = 0
        self.shareCount = 0
        self.commentCount = 0

    def __init__(self, mapa, userId: int, text: str):
        try:
            self.facebookPostID = mapa['targetfbid']
            self.createdTime = mapa['']
            self.text = text
            self.facebookUserID = userId
            self.likeCount = mapa['likecount']
            self.shareCount = mapa['sharecount']
            self.commentCount = mapa['commentcount']
        except KeyError:
            print('A key is missing, register will be discarded.')

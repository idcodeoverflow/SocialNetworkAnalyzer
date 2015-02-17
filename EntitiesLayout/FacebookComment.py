__author__ = 'David'


class FacebookComment:
    def __init__(self):
        self.facebookCommentID = 0
        self.message = ""
        self.likesCount = 0
        self.facebookPostID = 0

    def __init__(self, facebookCommentID: int, message: str, likesCount: int, facebookPostID: int):
        self.facebookCommentID = facebookCommentID
        self.message = message
        self.likesCount = likesCount
        self.facebookPostID = facebookPostID

    def __init__(self, mapa):
        self.facebookCommentID = mapa['']
        self.message = mapa['']
        self.likesCount = mapa['']
        self.facebookPostID = mapa['']
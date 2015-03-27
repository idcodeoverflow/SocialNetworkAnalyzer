

__author__ = 'David'


class FacebookComment:

    facebookCommentID = 0
    fbId = 0
    legacyId = 0
    author = 0
    time = 0
    text = ""
    likesCount = 0
    facebookPostID = 0

    def __init__(self, mapa, postId: int):
        try:
            self.facebookCommentID = mapa['id']
            self.fbId = mapa['fbid']
            self.legacyId = mapa['legacyid']
            self.text = (mapa['body'])['text']
            self.time = (mapa['timestamp'])['time']
            self.likesCount = mapa['likecount']
            self.facebookPostID = postId
        except KeyError:
            print('A key is missing, register will be discarded')

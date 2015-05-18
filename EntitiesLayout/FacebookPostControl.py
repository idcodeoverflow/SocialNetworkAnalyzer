__author__ = 'David'

from EntitiesLayout.FacebookUser import FacebookUser

class FacebookPostControl:

    idPostControl = 0
    fbid = 0
    facebookUser = FacebookUser.ini(0, '', '', '', '', '', '', '')
    visited = False

    def __init__(self, id: int = 0, fbid: int = 0, facebookUser: FacebookUser = None, visited: bool = False):
        self.idPostControl = id
        self.fbid = fbid
        self.facebookUser = facebookUser
        self.visited = visited


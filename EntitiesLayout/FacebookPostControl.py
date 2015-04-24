__author__ = 'David'

from EntitiesLayout.FacebookUser import FacebookUser

class FacebookPostControl:

    idPostControl = 0
    fbid = 0
    facebookUser = FacebookUser(0, '', '', '', '', '', '', '')
    visited = False

    def __init__(self, id: int, fbid: int, facebookUser: FacebookUser, visited: bool):
        self.idPostControl = id
        self.fbid = fbid
        self.facebookUser = facebookUser
        self.visited = visited


from EntitiesLayout.FacebookUser import FacebookUser

__author__ = 'David'

class FacebookProfilePage:
    facebookUserId = 0
    profilePage = ''

    def __init__(self, user: FacebookUser, page: str):
        self.facebookUserId = user.facebookUserId
        self.profilePage = page


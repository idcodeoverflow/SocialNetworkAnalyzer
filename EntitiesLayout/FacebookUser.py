__author__ = 'David'


class FacebookUser:
    def __init__(self):
        self.facebookUserId = 0
        self.firstName = ""
        self.gender = ""
        self.lastName = ""
        self.link = ""
        self.locale = ""
        self.name = ""
        self.userName = ""

    def __init__(self, facebookuserid: int, firstname: str, gender: str, lastname: str, link: str, locale: str,
                 name: str, username: str):
        self.facebookUserId = facebookuserid
        self.firstName = firstname
        self.gender = gender
        self.lastName = lastname
        self.link = link
        self.locale = locale
        self.name = name
        self.userName = username

    def __init__(self, mp):
        self.facebookUserId = mp['id']
        self.firstName = mp['first_name']
        self.gender = mp['gender']
        self.lastName = mp['last_name']
        self.link = mp['link']
        self.locale = mp['locale']
        self.name = mp['name']
        self.userName = mp['username']



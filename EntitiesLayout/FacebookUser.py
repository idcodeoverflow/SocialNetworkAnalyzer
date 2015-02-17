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

    def __init__(self, map):
        self.facebookUserId = map['ID']
        self.firstName = map['first_name']
        self.gender = map['gender']
        self.lastName = map['last_name']
        self.link = map['link']
        self.locale = map['locale']
        self.name = map['name']
        self.userName = map['username']



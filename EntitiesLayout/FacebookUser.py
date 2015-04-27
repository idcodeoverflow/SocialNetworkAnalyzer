__author__ = 'David'


class FacebookUser:

    facebookUserId = 0
    userName = ''
    name = ''

    @classmethod
    def ini(self, facebookuserid: int, firstname: str, gender: str, lastname: str, link: str, locale: str,
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
        try:
            self.facebookUserId = mp['id']
            self.firstName = mp['first_name']
            self.gender = mp['gender']
            self.lastName = mp['last_name']
            self.link = mp['link']
            self.locale = mp['locale']
            self.name = mp['name']
            self.userName = mp['username']

        except KeyError:
            print('This User register won\'t be stored.' + str(mp))

    
    def __repr__(self):
        return '(' + str(
            self.facebookUserId) + ', ' + self.firstName + ', ' + self.gender + ', ' + self.lastName + ', ' + \
               self.link + ', ' + self.locale + ', ' + self.name + ', ' + self.userName + ')'


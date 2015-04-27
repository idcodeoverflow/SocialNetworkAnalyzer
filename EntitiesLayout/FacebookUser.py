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
            if len(mp) < 1:
                raise KeyError('The dictionary containing the user data is empty.')
            print('usuario -> ' + str(mp))
            self.facebookUserId = mp['id']
            self.firstName = mp['first_name']
            self.gender = mp['gender']
            self.lastName = mp['last_name']
            self.link = mp['link']
            self.locale = mp['locale']
            self.name = mp['name']
            self.userName = mp['username']

        except KeyError:
            print('This register won\'t be stored.')

    
    def __repr__(self):
        return '(' + str(
            self.facebookUserId) + ', ' + self.firstName + ', ' + self.gender + ', ' + self.lastName + ', ' + \
               self.link + ', ' + self.locale + ', ' + self.name + ', ' + self.userName + ')'


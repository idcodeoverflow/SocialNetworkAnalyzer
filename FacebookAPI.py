from DBLayout.FacebookUserDB import FacebookUserDB
from EntitiesLayout.FacebookUser import FacebookUser
import json
import urllib.request
import urllib.error

__author__ = 'David'


class FacebookAPI:
    def __init__(self, nUsers: int, token: str, printable: bool):
        self.url = 'https://graph.facebook.com/'
        self.token = token

        self._START_NUMBER_ = 11

        self.usersNumber = nUsers
        self.existsUser = False
        self.limit = self.usersNumber + self._START_NUMBER_
        self.printable = printable

    def getUsers(self):
        currentUserId = self._START_NUMBER_
        result = []
        control = 0
        while control < self.usersNumber:

            self.existsUser = False

            try:
                packetData = urllib.request.urlopen(self.url + str(currentUserId), data=None, timeout=500, cafile=None,
                                                    capath=None,
                                                    cadefault=False)
            except urllib.error.HTTPError:
                self.existsUser = True
                self.limit += 1

            jsonString = packetData.read().decode('utf-8')

            if not self.existsUser:

                data = json.loads(jsonString)

                try:
                    data['link']
                except KeyError:
                    print("User ID: " + str(currentUserId) + " link is not available, will be discarded.")
                    currentUserId += 1
                    continue

                if self.printable:
                    print('--*--*--*--*--*--*--*--*--*--*--*--*-- USER ' + str(
                        currentUserId) + ' --*--*--*--*--*--*--*--*--*--*--*--*--')

                    for y in data.keys():
                        print('%s: %s' % (y, data[y]))

                control += 1

                result.append(data)

            else:
                if self.printable:
                    print('User ID: %s not found' % currentUserId)

            packetData.close()

            currentUserId += 1

        return result


fb = FacebookAPI(8997, "", True)
users = fb.getUsers()
userAccess = FacebookUserDB()
for data in users:
    user = FacebookUser(data)
    userAccess.insertUser(user)
    print(data)

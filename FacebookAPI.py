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

        self._START_NUMBER_ = 4
        self.currentUserId = 0

        self.usersNumber = nUsers
        self.existsUser = False
        self.limit = self.usersNumber + self._START_NUMBER_
        self.printable = printable

    def getUsers(self):
        self.currentUserId = self._START_NUMBER_
        result = []
        control = 0


        while control < self.usersNumber:

            self.existsUser = False

            try:
                packetData = urllib.request.urlopen(self.url + str(self.currentUserId), data=None, timeout=500, cafile=None,
                                                    capath=None,
                                                    cadefault=False)
            except urllib.error.HTTPError as e:
                self.existsUser = True
                self.limit += 1
                print(e.fp.read())

            jsonString = packetData.read().decode('utf-8')

            if not self.existsUser:

                data = json.loads(jsonString)

                try:
                    data['link']
                except KeyError:
                    print("User ID: " + str(self.currentUserId) + " link is not available, will be discarded.")
                    self.currentUserId += 1
                    continue

                if self.printable:
                    print('--*--*--*--*--*--*--*--*--*--*--*--*-- USER ' + str(
                        self.currentUserId) + ' --*--*--*--*--*--*--*--*--*--*--*--*--')

                    for y in data.keys():
                        print('%s: %s' % (y, data[y]))

                control += 1

                result.append(data)

            else:
                if self.printable:
                    print('User ID: %s not found' % self.currentUserId)

            packetData.close()

            self.currentUserId += 1

            print(str(control / self.usersNumber) + '% completed. ' + str(control) + ' of ' + str(self.usersNumber))

        return result

    def getPosts(self):
        self.currentUserId = self._START_NUMBER_
        result = []
        control = 0


        while control < self.usersNumber:

            self.existsUser = False

            try:
                packetData = urllib.request.urlopen(self.url + str(self.currentUserId), data=None, timeout=500, cafile=None,
                                                    capath=None,
                                                    cadefault=False)
            except urllib.error.HTTPError as e:
                self.existsUser = True
                self.limit += 1
                print(e.fp.read())

            jsonString = packetData.read().decode('utf-8')

            if not self.existsUser:

                data = json.loads(jsonString)

                try:
                    data['link']
                except KeyError:
                    print("User ID: " + str(self.currentUserId) + " link is not available, will be discarded.")
                    self.currentUserId += 1
                    continue

                if self.printable:
                    print('--*--*--*--*--*--*--*--*--*--*--*--*-- USER ' + str(
                        self.currentUserId) + ' --*--*--*--*--*--*--*--*--*--*--*--*--')

                    for y in data.keys():
                        print('%s: %s' % (y, data[y]))

                control += 1

                result.append(data)

            else:
                if self.printable:
                    print('User ID: %s not found' % self.currentUserId)

            packetData.close()

            self.currentUserId += 1

            print(str(control / self.usersNumber) + '% completed. ' + str(control) + ' of ' + str(self.usersNumber))

        return result

# fb = FacebookAPI(0, "", True)
#
# for i in range(0,450,1):
#
#     user = fb.currentUserId
#     fb = FacebookAPI(20, "", True)
#     fb.currentUserId = user
#     users = fb.getUsers()
#     userAccess = FacebookUserDB()
#     for data in users:
#         user = FacebookUser(data)
#         userAccess.insertUser(user)
#         print(data)
userAccess = FacebookUserDB()
for i in userAccess.readUsers():
    print(i)


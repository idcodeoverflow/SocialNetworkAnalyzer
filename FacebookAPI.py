import json
import urllib.request
import urllib.error

from DBLayout.FacebookUserDB import FacebookUserDB
from EntitiesLayout.FacebookUser import *


__author__ = 'David'


class FacebookAPI:
    def __init__(self, nUsers: int, token: str, printable: bool):
        self.url = 'https://graph.facebook.com/'
        self.fbURL = 'https://www.facebook.com/'
        self.token = token
        self.defTimeout = 500
        self._START_NUMBER_ = 2205
        self.currentUserId = self._START_NUMBER_
        self.usersNumber = nUsers
        self.existsUser = False
        self.limit = self.usersNumber + self._START_NUMBER_
        self.printable = printable
        self.existsProfile = False

    def getUsers(self):
        result = []
        control = 0

        while control < self.usersNumber:

            self.existsUser = False

            try:
                packetData = urllib.request.urlopen(self.url + str(self.currentUserId), data=None, timeout=self.defTimeout, cafile=None,
                                                    capath=None,
                                                    cadefault=False)
                jsonString = packetData.read().decode('utf-8')
                packetData.close()
            except urllib.error.HTTPError as e:
                self.existsUser = True
                self.limit += 1
                print(e.fp.read())

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



            self.currentUserId += 1

            print(str(100.0 * control / self.usersNumber) + '% completed. ' + str(control) + ' of ' + str(self.usersNumber))

        return result

    def getPosts(self):

        users = []
        userAccess = FacebookUserDB()
        result = []
        try:
            users = userAccess.readUsers()
        except Exception as e:
            print(e)


        for i in users:

            self.currentUserId = i.facebookUserId
            self.existsPost = False

            try:
                packetData = urllib.request.urlopen(self.url + str(self.currentUserId) + '/statuses', data=None, timeout=self.defTimeout, cafile=None,
                                                    capath=None,
                                                    cadefault=False)
            except urllib.error.HTTPError as e:
                self.existsPost = True
                self.limit += 1
                print(e.fp.read())

            jsonString = packetData.read().decode('utf-8')

            if not self.existsPost:

                data = json.loads(jsonString)

                if self.printable:
                    print('--*--*--*--*--*--*--*--*--*--*--*--*-- POST from: ' + str(
                        self.currentUserId) + ' --*--*--*--*--*--*--*--*--*--*--*--*--')

                    for y in data.keys():
                        print('%s: %s' % (y, data[y]))


                result.append(data)

            else:
                if self.printable:
                    print('Post from User ID: %s not found' % self.currentUserId)

            packetData.close()

            self.currentUserId += 1

        return result

    def getProfilePage(self, fbUser: FacebookUser):

        try:
            packetData = urllib.request.urlopen(self.fbURL + '/' + fbUser.userName, data=None,
                                                timeout=self.defTimeout, cafile=None,
                                                capath=None,
                                                cadefault=False)
        except urllib.error.HTTPError as e:
            self.existsProfile = True
            self.limit += 1
            print(e.fp.read())

        profilePage = packetData.read().decode('utf-8')

        if not self.existsProfile:

           if self.printable:
                print('--*--*--*--*--*--*--*--*--*--*--*--*-- Profile Page of: ' + str(
                    self.currentUserId) + ' ' + fbUser.name + ' --*--*--*--*--*--*--*--*--*--*--*--*--')
                print(profilePage)

        else:
            if self.printable:
                print('Profile Page of User ID: %s not found' % self.currentUserId)

        packetData.close()

        return profilePage

fb = FacebookAPI(5, "", True)
userAccess = FacebookUserDB()
# for i in range(0,450,1):
#     users = fb.getUsers()
#     for u in users:
#         userAccess.insertUser(FacebookUser(u))

u = userAccess.readUser(4)

fb.getProfilePage(u)



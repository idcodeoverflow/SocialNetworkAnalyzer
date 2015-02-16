import json
import urllib.request
import urllib.error

__author__ = 'David'


class FacebookAPI:

    def __init__(self, nUsers: int, token: str, printable: bool):
        self.url = 'https://graph.facebook.com/'
        self.token = token

        self._START_NUMBER_ = 4

        self.usersNumber = nUsers
        self.usersNumber += self._START_NUMBER_
        self.existsUser = False
        self.limit = self.usersNumber + self._START_NUMBER_
        self.printable = printable



    def getUsers(self):
        currentUserId = self._START_NUMBER_
        result = {}
        while currentUserId < self.limit:

            self.existsUser = False

            try:
                packetData = urllib.request.urlopen(self.url + str(currentUserId), data=None, timeout=500, cafile=None, capath=None,
                                                    cadefault=False)
            except urllib.error.HTTPError:
                self.existsUser = True
                self.limit += 1

            jsonString = packetData.read().decode('utf-8')

            if not self.existsUser:

                data = json.loads(jsonString)
                if self.printable:
                    print('--*--*--*--*--*--*--*--*--*--*--*--*-- USER ' + str(currentUserId) + ' --*--*--*--*--*--*--*--*--*--*--*--*--')

                    for y in data.keys():
                        print('%s: %s' % (y, data[y]))

                for y in data.keys():
                     result[y] = data[y]

            else:
                if self.printable:
                    print('ID: %s not found' % currentUserId)

            packetData.close()
            currentUserId += 1
        return result

fb = FacebookAPI(4, "", True)
fb.getUsers()


import json
import urllib.request
import urllib.error

__author__ = 'David'

url = 'https://graph.facebook.com/'

usersNumber = int(input('How many users are we gonna search???: '))
usersNumber += 4
isFalse = False

for x in range(4, usersNumber):

    isFalse = False

    try:
        packetData = urllib.request.urlopen(url + str(x), data=None, timeout=500, cafile=None, capath=None, cadefault=False)
    except urllib.error.HTTPError:
        isFalse = True
        usersNumber += 1

    jsonString = packetData.read().decode('utf-8')

    if not isFalse:

        data = json.loads(jsonString)

        print('--*--*--*--*--*--*--*--*--*--*--*--*-- USUARIO ' + str(x) + '--*--*--*--*--*--*--*--*--*--*--*--*--')

        for y in data.keys():
            print('%s: %s' % (y, data[y]))

    else:

        print('ID: %s not found' % x)

    print('n')

    packetData.close()

input('Press any key to exit...')
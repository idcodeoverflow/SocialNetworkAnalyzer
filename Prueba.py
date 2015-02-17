import json
import urllib.request
import urllib.error

__author__ = 'David'

url = 'https://www.facebook.com/zuck'

_START_NUMBER_ = 4
usersNumber = int(input('How many users are we gonna search???: '))
usersNumber += _START_NUMBER_
isFalse = False

x = _START_NUMBER_
limit = usersNumber + _START_NUMBER_

while x < limit:

    isFalse = False

    try:
        packetData = urllib.request.urlopen(url, data=None, timeout=500, cafile=None, capath=None,
                                            cadefault=False)
    except urllib.error.HTTPError:
        isFalse = True
        limit += 1

    jsonString = packetData.read().decode('utf-8')

    if not isFalse:

        data = json.loads(jsonString)

        print('--*--*--*--*--*--*--*--*--*--*--*--*-- USUARIO ' + str(x) + ' --*--*--*--*--*--*--*--*--*--*--*--*--')

        for y in data.keys():
            print('%s: %s' % (y, data[y]))

    else:

        print('ID: %s not found' % x)

    packetData.close()
    x += 1

input('Press any key to exit...')

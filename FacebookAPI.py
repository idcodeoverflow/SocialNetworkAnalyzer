import datetime
import json
import urllib.request
import urllib.response
import urllib.parse
import urllib.error
import http.cookiejar
from mysql.connector import Timestamp
from DBLayout.FacebookCommentDB import FacebookCommentDB
from DBLayout.FacebookProfilePageDB import FacebookProfilePageDB
from DBLayout.FacebookUserDB import FacebookUserDB
from EntitiesLayout.FacebookPostControl import FacebookPostControl

from EntitiesLayout.FacebookUser import *
from DBLayout.FacebookPostControlDB import FacebookPostControlDB
from DBLayout.FacebookPostDB import FacebookPostDB
from EntitiesLayout.FacebookPost import FacebookPost
from PreprocessingLayout.html.HTMLTreatment import HTMLTreatment


__author__ = 'David'


class FacebookAPI:
    cj = http.cookiejar.MozillaCookieJar()
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
    headers = [('Referer', 'http://login.facebook.com/login.php'),
               ('Content-Type', 'application/x-www-form-urlencoded'), ('User-Agent',
                                                                       'Mozilla/8.0 (Windows; U; Windows '
                                                                       'NT 5.1; en-US; rv:1.9.1.7)Gecko'
                                                                       '/20091221 Firefox/3.5.7 (.NET CLR'
                                                                       ' 3.5.30729)')]


    def __init__(self, nUsers: int, token: str, printable: bool):
        self.url = 'https://graph.facebook.com/'
        self.fbURL = 'https://www.facebook.com/'
        self.token = token
        self.defTimeout = 500
        self._START_NUMBER_ = 6744
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
                packetData = urllib.request.urlopen(self.url + str(self.currentUserId), data=None,
                                                    timeout=self.defTimeout, cafile=None,
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

            print(str(100.0 * control / self.usersNumber) + '% completed. ' + str(control) + ' of ' + str(
                self.usersNumber))

        return result

    def getProfilePage(self, fbUser: FacebookUser):
        profilePage = ''
        try:
            packetData = self.opener.open(fbUser.link)
            profilePage = packetData.read().decode('utf-8')
            packetData.close()
        except urllib.error.HTTPError as e:
            self.existsProfile = True
            self.limit += 1
            print(e.fp.read())

        if not self.existsProfile:

            if self.printable:
                print('--*--*--*--*--*--*--*--*--*--*--*--*-- Profile Page of: ' + str(
                    fbUser.facebookUserId) + ' ' + fbUser.name + ' --*--*--*--*--*--*--*--*--*--*--*--*--')
                print(profilePage)

        else:
            if self.printable:
                print('Profile Page of User ID: %s not found' % (str(fbUser.facebookUserId) + ' ' + fbUser.name))

        self.existsProfile = False
        return profilePage

    def login(self, user: str, password: str):
        cj = self.cj
        opener = self.opener
        opener.addheaders = self.headers
        url = 'https://login.facebook.com/login.php?login_attempt=1'
        data = 'locale=en_US&non_com_login=&email=' + user + '&pass=' + password + '&lsd=20TOl'

        auth = urllib.parse.urlencode({'email': user, 'pass': password}).encode('utf-8')
        usock = self.opener.open('http://www.facebook.com')
        usock = self.opener.open(url, data=auth)
        html = usock.read().decode('utf-8')
        if "Logout" in html:
            print("*-*-*-*-*-*-*-*-*-*-*-* Successfully logged in!!! *-*-*-*-*-*-*-*-*-*-*-*")
            self.auth = auth
        else:
            print
            "failed login"
        print(html)

    def getLikesPage(self, user: FacebookUser, postId: str):
        self.existsPostCount = False
        profilePage = ''
        try:
            link = self.fbURL + '/browse/likes?id=' + postId + '&actorid=' + str(user.facebookUserId)
            packetData = self.opener.open(link)
            profilePage = packetData.read().decode('utf-8')
            packetData.close()
            if('No se han encontrado resultados.' in profilePage):
                return ''
        except urllib.error.HTTPError as e:
            self.existsPostCount = True
            self.limit += 1
            print(e.fp.read())

        if not self.existsPostCount:
            tempo = 0

        else:
            if self.printable:
                print("Like's count Page not found" )

        return profilePage

    def getPostPage(self, user: FacebookUser, postId: int):
        self.existsPostCount = False
        profilePage = ''
        try:
            link = user.link + '/posts/' + str(postId)
            packetData = self.opener.open(link)
            profilePage = packetData.read().decode('utf-8')
            packetData.close()
            if('Esta página no está disponible' in profilePage):
                return ''
        except urllib.error.HTTPError as e:
            self.existsPostCount = True
            self.limit += 1
            print(e.fp.read())

        if not self.existsPostCount:
            tempo = 0

        else:
            try:
                if self.printable:
                    print('Post\'s Page % not found' % (link))
            except ValueError as err:
                return profilePage

        return profilePage

    def getPendantPosts(self):
        try:
            ufpcAccess = FacebookProfilePageDB()
            fpcAccess = FacebookPostControlDB()
            postAccess = FacebookPostDB()
            usersAccess = FacebookUserDB()
            users = usersAccess.readUsers()

            for user in users:
                print('Getting posts from user: ' + str(user.facebookUserId))
                profiles = ufpcAccess.readProfilesPagesFromUser(user)


                for profile in profiles:
                    htmlTreatment = HTMLTreatment(profile.profilePage)
                    fbids = htmlTreatment.getFBIds()

                    for fbid in fbids:
                        if fbid.isdigit():
                            control = fpcAccess.readPostControl(int(fbid))
                        else:
                            control = FacebookPostControl()
                        if control.fbid == 0:
                            postPage = self.getPostPage(user, fbid)
                            postTreatment = HTMLTreatment(postPage)
                            if postPage != '':
                                likes = postTreatment.countLikes()
                                facebookPostId = fbid
                                createdTime = datetime.datetime.now()
                                text = ''
                                facebookUserID = user.facebookUserId
                                paragraphs = postTreatment.extractParagraphs()

                                for paragraph in paragraphs:
                                    text += paragraph

                                textTreatment = HTMLTreatment(text)

                                textTreatment.removeHTMLLabels()
                                textTreatment.removeLinks()
                                textTreatment.removerURLs()
                                textTreatment.replaceHexCharacters()
                                text = textTreatment.html

                                post = FacebookPost(facebookPostId, createdTime, text, facebookUserID, likes)
                                completed = postAccess.insertPost(post)
                                fpcAccess.insertPostControl(FacebookPostControl(0, fbid, user, True))
                                if completed:
                                    print('A post from user ' + str(facebookUserID) + ' was stored fbid: ' + str(fbid) + '\n' + text)
        except AttributeError as err:
            print('Attribute error at get pendant posts ' + str(err))
        except ValueError as err:
            print('Value error at get pendant posts ' + str(err))
        except Exception as err:
            print('An error has occurred while getting pendant posts ' + str(err))


    def getPendantComments(self):
        try:
            accessProfilePage = FacebookProfilePageDB()
            accessComment = FacebookCommentDB()
            accessUser = FacebookUserDB()
            users = accessUser.readUsers()
            comments = []

            for user in users:
                print('user ' + str(user.facebookUserId))#delete
                if(user.facebookUserId < 5739):#delete
                    continue#delete
                profilesPages = accessProfilePage.readProfilesPagesFromUser(user)

                for profilePage in profilesPages:
                    htmlTreament = HTMLTreatment(profilePage.profilePage)
                    fbids = htmlTreament.getFBIds()
                    for fbid in fbids:
                        print(fbid)
                        text = self.getPostPage(user,fbid)
                        tr = HTMLTreatment(text)
                        print('*************************************************')
                        tr.getFacebookComments()
                        comments = tr.commentsJSONToDictionary(fbid)
                        for comment in comments:
                            success = accessComment.insertComment(comment, fbid)
                            if success:
                                print('A comment from user ' + str(user.facebookUserId) + ' was stored fbid: ' + str(fbid))

        except AttributeError as err:
            print('Attribute error at get pendant comments ' + str(err))
        except ValueError as err:
            print('Value error at get pendant comments ' + str(err))
        except Exception as err:
            print('An error has occurred while getting pendant comments ' + str(err))








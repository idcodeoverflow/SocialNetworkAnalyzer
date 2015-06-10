import datetime
import json
import string
import urllib.request
import urllib.response
import urllib.parse
import urllib.error
import http.cookiejar

from DBLayout.FacebookCommentDB import FacebookCommentDB
from DBLayout.FacebookProfilePageDB import FacebookProfilePageDB
from DBLayout.FacebookUserDB import FacebookUserDB
from EntitiesLayout.FacebookPostControl import FacebookPostControl
from EntitiesLayout.FacebookUser import *
from DBLayout.FacebookPostControlDB import FacebookPostControlDB
from DBLayout.FacebookPostDB import FacebookPostDB
from EntitiesLayout.FacebookPost import FacebookPost
from PreprocessingLayout.html.HTMLTreatment import HTMLTreatment
from PreprocessingLayout.language.LanguageProcessor import LanguageProcessor
from PreprocessingLayout.language.PorterStemmer import PorterStemmer


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
                if(user.facebookUserId < 7221):#delete
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


    def analyzePostsNComments(self):
        resultsFile = open('socialNetworkAnalyzerResult.txt', 'w')
        resultsFile.write('post\'s_user\tpost\'s_likes\tpost\'s_positive_words\tpost\'s_negative_words\tpost\'s_totalwords'
                          '\tpost\'s_classification\tpositive_comments_count'
                          '\tnegative_comments_count\ttotal_comments_count')
        resultsFile.write('\n')
        postDB = FacebookPostDB()

        commentDB = FacebookCommentDB()

        posts = postDB.readPosts()
        ps = PorterStemmer()

        currentPost = 0

        for post in posts:
            postText = post.text

            #put all chars to lower case
            postText = postText.lower()

            languageProcessor = LanguageProcessor(postText)
            languageProcessor.removeSymbols()
            postTokens = languageProcessor.getTokens()

            #exclude unwanted tokens which contains no letters
            postTokens = [ tok for tok in postTokens if tok.__len__() > 1 and all(c in string.ascii_letters for c in tok) ]

            #exclude empty lists
            if postTokens.__len__() > 0:
                #clear prefixes, plurals and things like that
                cleanPostTokens = [ps.stem(tok, 0, tok.__len__() - 1) for tok in postTokens]

                postPositiveWordsCount = 0
                postNegativeWordsCount = 0
                postNeutralWordsCount = 0

                commPositiveWordsCount = 0
                commNegativeWordsCount = 0
                commNeutralWordsCount = 0

                negativeComments = 0
                positiveComments = 0
                neutralComments = 0


                for word in cleanPostTokens:
                    indexKind = LanguageProcessor.isNegativeOrPositive(word)
                    if indexKind == 1:
                        postNegativeWordsCount += 1
                    elif indexKind == 2:
                        postPositiveWordsCount += 1
                    else:
                        postNeutralWordsCount += 1



            #analyze comments from the current post
            comments = commentDB.readComment(post.facebookPostId)
            for comment in comments:

                commPositiveWordsCount = 0
                commNegativeWordsCount = 0
                commNeutralWordsCount = 0

                commText = comment.body.text
                #put all chars to lower case
                commText = commText.lower()

                languageProcessor = LanguageProcessor(commText)
                languageProcessor.removeSymbols()
                commTokens = languageProcessor.getTokens()

                #exclude unwanted tokens which contains no letters
                commTokens = [ tok for tok in commTokens if tok.__len__() > 1 and all(c in string.ascii_letters for c in tok) ]

                #exclude empty lists
                if commTokens.__len__() > 0:
                    #clear prefixes, plurals and things like that
                    cleanCommTokens = [ps.stem(tok, 0, tok.__len__() - 1) for tok in commTokens]

                    for commWord in cleanCommTokens:
                        indexKind = LanguageProcessor.isNegativeOrPositive(commWord)
                        if indexKind == 1:
                            commNegativeWordsCount += 1
                        elif indexKind == 2:
                            commPositiveWordsCount += 1
                        else:
                            commNeutralWordsCount += 1

                    if commNegativeWordsCount > commPositiveWordsCount:
                        negativeComments += 1 * max(comment.likeCount, 1)
                    elif commNegativeWordsCount < commPositiveWordsCount:
                        positiveComments += 1 * max(comment.likeCount, 1)
                    else:
                        neutralComments += 1 * max(comment.likeCount, 1)

            totalPostWords =  postNegativeWordsCount + postPositiveWordsCount + postNeutralWordsCount

            postClassification = 'NEUTRAL'
            if postNegativeWordsCount > postPositiveWordsCount:
                postClassification = 'NEGATIVE'
            elif postNegativeWordsCount < postPositiveWordsCount:
                postClassification = 'POSITIVE'

            resultsFile.write(str(post.facebookUserID) + '\t' + str(post.likeCount) + '\t' + str(postPositiveWordsCount)
                              + '\t' + str(postNegativeWordsCount) + '\t' + str(totalPostWords) +
                              '\t' + postClassification + '\t' + str(positiveComments) + '\t' + str(negativeComments) +
                              '\t' + str(neutralComments))
            resultsFile.write('\n')

            currentPost += 1
            print(str(currentPost / posts.__len__() * 100.0) + ' COMPLETED...')





        resultsFile.close()
        return 0






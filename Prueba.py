from DBLayout.FacebookProfilePageDB import FacebookProfilePageDB
from DBLayout.FacebookUserDB import FacebookUserDB
from EntitiesLayout.FacebookProfilePage import FacebookProfilePage
from FacebookAPI import FacebookAPI
from PreprocessingLayout.html.HTMLTreatment import HTMLTreatment

accessUser = FacebookUserDB()
accessProfile = FacebookProfilePageDB()
#
#
fb = FacebookAPI(5, "", True)
# # userAccess = FacebookUserDB()
# # for i in range(0, 450, 1):
# #     users = fb.getUsers()
# #     for u in users:
# #         userAccess.insertUser(FacebookUser(u))
#
u = accessUser.readUsers()
profilePageAccess = FacebookProfilePageDB()
mail = 'respaldos.remex2013@gmail.com'#input('Type your email:')
password = 'remex2013'#input('Type your password:')
fb.login(mail, password)
#for i in u:
#    if i.facebookUserId > 1468:
#        print(i)
#        profilePageAccess.insertProfilePage(FacebookProfilePage(i, fb.getProfilePage(i)))

accessProfilePage = FacebookProfilePageDB()
profilePages = accessProfilePage.readProfilesPages()
user = FacebookUserDB().readUser(4)
profilePage = accessProfilePage.readProfilesPagesFromUser(user)[0]
#for profilePage in profilePages:
#    print(profilePage.profilePage)
    #htmlTreament = HTMLTreatment(profilePage)
    #fbids = htmlTreament.getFBIds()
    #for fbid in fbids:
        #print(fbid)
#print(profilePage.profilePage)
htmlTreament = HTMLTreatment(profilePage.profilePage)
fbids = htmlTreament.getFBIds()
print('8888888888888888888888888888888888888888888888888888888888888888888888888888888')

for fbid in fbids:
    print(fbid)
    text = fb.getPostPage(user,fbid)
    tr = HTMLTreatment(text)
    print('*************************************************')
    tr.getFacebookComments()
    tr.commentsJSONToDictionary()


#print(htmlTreament.html)


#fb.getPendantPosts()





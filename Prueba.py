from DBLayout.FacebookProfilePageDB import FacebookProfilePageDB
from DBLayout.FacebookUserDB import FacebookUserDB
from EntitiesLayout.FacebookProfilePage import FacebookProfilePage
from FacebookAPI import FacebookAPI
from PreprocessingLayout.html.HTMLTreatment import HTMLTreatment

# accessUser = FacebookUserDB()
# accessProfile = FacebookProfilePageDB()
#
#
fb = FacebookAPI(5, "", True)
# # userAccess = FacebookUserDB()
# # for i in range(0, 450, 1):
# #     users = fb.getUsers()
# #     for u in users:
# #         userAccess.insertUser(FacebookUser(u))
#
# u = accessUser.readUsers()
# profilePageAccess = FacebookProfilePageDB()
mail = 'respaldos.remex2013@gmail.com'#input('Type your email:')
password = 'remex2013'#input('Type your password:')
fb.login(mail, password)
# for i in u:
#     if i.facebookUserId > 6942:
#         print(i)
#         profilePageAccess.insertProfilePage(FacebookProfilePage(i, fb.getProfilePage(i)))

accessProfilePage = FacebookProfilePageDB()
#profilePages = accessProfilePage.readProfilesPages()
user = FacebookUserDB().readUser(4)
profilePage = accessProfilePage.readProfilesPagesFromUser(user)[0]
#for profilePage in profilePages:
#    print(profilePage.profilePage)
#    htmlTreament = HTMLTreatment(profilePage)
    #fbids = htmlTreament.getFBIds()
    #for fbid in fbids:
    #    print(fbid)
#print(profilePage.profilePage)
htmlTreament = HTMLTreatment(profilePage.profilePage)
fbids = htmlTreament.getFBIds()
print(fbids)
for fbid in fbids:
    print(fbid)
    text = fb.getPostPage(user,fbid)
    tr = HTMLTreatment(text)
    print(text)
    print('--------------------->Likes count: ' + str(tr.countLikes()))

#print(htmlTreament.html)
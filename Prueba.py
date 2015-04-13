from DBLayout.FacebookProfilePageDB import FacebookProfilePageDB
from DBLayout.FacebookUserDB import FacebookUserDB
from EntitiesLayout.FacebookProfilePage import FacebookProfilePage
from FacebookAPI import FacebookAPI
from PreprocessingLayout.html.HTMLTreatment import HTMLTreatment

# accessUser = FacebookUserDB()
# accessProfile = FacebookProfilePageDB()
#
#
# fb = FacebookAPI(5, "", True)
# # userAccess = FacebookUserDB()
# # for i in range(0, 450, 1):
# #     users = fb.getUsers()
# #     for u in users:
# #         userAccess.insertUser(FacebookUser(u))
#
# u = accessUser.readUsers()
# profilePageAccess = FacebookProfilePageDB()
# mail = input('Type your email:')
# password = input('Type your password:')
# fb.login(mail, password)
# for i in u:
#     if i.facebookUserId > 6942:
#         print(i)
#         profilePageAccess.insertProfilePage(FacebookProfilePage(i, fb.getProfilePage(i)))

accessProfilePage = FacebookProfilePageDB()
profilePages = accessProfilePage.readProfilesPages()


#for profilePage in profilePages:
#    htmlTreament = HTMLTreatment(profilePage)
#    fbids = htmlTreament.getFBIds()
#    for fbid in fbids:
#        print(fbid)
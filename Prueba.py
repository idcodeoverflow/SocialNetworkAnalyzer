from DBLayout.FacebookProfilePageDB import FacebookProfilePageDB
from DBLayout.FacebookUserDB import FacebookUserDB
from EntitiesLayout.FacebookProfilePage import FacebookProfilePage
from FacebookAPI import FacebookAPI
from PreprocessingLayout.HTMLTreatment import HTMLTreatment

accessUser = FacebookUserDB()
accessProfile = FacebookProfilePageDB()

user = accessUser.readUser(4)
profile = accessProfile.readProfilesPagesFromUser(user)


h = HTMLTreatment(profile[0].profilePage)
h.replaceHexCharacters()
#h.removeLinks()
#for i in h.extractParagraphs():
#    print(h.removeHTMLLabelsFromText(i))
for i in h.extractComments():
    print(i)

# fb = FacebookAPI(5, "", True)
# userAccess = FacebookUserDB()
# for i in range(0, 450, 1):
#     users = fb.getUsers()
#     for u in users:
#         userAccess.insertUser(FacebookUser(u))

# u = userAccess.readUsers()
# profilePageAccess = FacebookProfilePageDB()
# mail = input('Type your email:')
# password = input('Type your password:')
# fb.login2(mail, password)
# for i in u:
#     print(i)
#     profilePageAccess.insertProfilePage(FacebookProfilePage(i, fb.getProfilePage(i)))
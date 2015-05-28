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

fb.getPendantComments()





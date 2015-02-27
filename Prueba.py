from DBLayout.FacebookProfilePageDB import FacebookProfilePageDB
from DBLayout.FacebookUserDB import FacebookUserDB
from PreprocessingLayout.HTMLTreatment import HTMLTreatment

accessUser = FacebookUserDB()
accessProfile = FacebookProfilePageDB()

user = accessUser.readUser(4)
profile = accessProfile.readProfilesPagesFromUser(user)


h = HTMLTreatment(profile[0].profilePage)
h.replaceHexCharacters()
for i in h.extractParagraphs():
    print(i)
for i in h.extractComments():
    print(i)
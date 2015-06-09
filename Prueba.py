from DBLayout.FacebookCommentDB import FacebookCommentDB
from DBLayout.FacebookPostDB import FacebookPostDB
from EntitiesLayout.FacebookPost import FacebookPost
from FacebookAPI import FacebookAPI


api = FacebookAPI(5, ' ', True)

api.analyzePostsNComments()
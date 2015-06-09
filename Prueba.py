from DBLayout.FacebookCommentDB import FacebookCommentDB
from DBLayout.FacebookPostDB import FacebookPostDB
from EntitiesLayout.FacebookPost import FacebookPost




postsDB = FacebookPostDB()
commentsDB = FacebookCommentDB()
comments = commentsDB.readComments()


print(commentsDB.readComment(10102044342642751).body.text)
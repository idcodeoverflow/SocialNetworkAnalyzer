from DBLayout.FacebookPostDB import FacebookPostDB
from EntitiesLayout.FacebookPost import FacebookPost




postsDB = FacebookPostDB()
posts = postsDB.readPosts()

print(postsDB.readPost(10102017646077881).text)

from DBLayout.DBConnection import DBConnection, mysql
from EntitiesLayout.FacebookComment import FacebookComment
from EntitiesLayout.FacebookUser import FacebookUser

__author__ = 'David'


class FacebookCommentDB:


    def __init__(self):
        self.db = DBConnection()

    def insertComment(self, comment: FacebookComment):
        try:
            cnx = self.db.openConnection()
            cursor = cnx.cursor()
            addFBCommentQuery = 'INSERT INTO comment(idComment, id, fbid, legacyid, text, author, ftidentifier, isFeatured, likeCount, hasViewerLiked, ' \
                             'canRemove, canReport, canEdit, source, viewerCanLike, canComment, isAuthorWeakReference, isTranslatable, ' \
                             'timestamp_time, timestamp_text, timestamp_verbose, spamReplyCount, interestingReplyOffset, interestingReplyId, ' \
                             'recentReplyTimestamp_time, recentReplyTimestamp_text, recentReplyTimestamp_verbose)' \
                             'VALUES (NULL, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);'
            dataUser = (comment.idComment, comment.id, comment.fbid, comment.legacyid, comment.text, comment.author, comment.ftidentifier, comment.isFeatured,
                        comment.likeCount, comment.hasViewerLiked, comment.canRemove, comment.canReport, comment.canEdit, comment.source, comment.viewerCanLike,
                        comment.canComment, comment.isAuthorWeakReference, comment.isTranslatable, comment.timestamp_time, comment.timestamp_text, comment.timestamp_verbose,
                        comment.spamReplyCount, comment.interestingReplyOffset, comment.interestingReplyId, comment.recentReplyTimestamp_time, comment.recentReplyTimestamp_text,
                        comment.recentReplyTimestamp_verbose)

            cursor.execute(addFBCommentQuery, dataUser)
            cnx.commit()
            cursor.close()
            self.db.closeConnection()

        except mysql.connector.Error as err:
            print(err)
            print('Error writing a Facebook comment in the DB.')
        except AttributeError as err:
            print('Comment register can\'t be stored.')

    def readComment(self, fbid: int):
        try:
            cnx = self.db.openConnection()
            cursor = cnx.cursor()
            readFBCommentQuery = ('SELECT idComment, id, fbid, legacyid, text, author, ftidentifier, isFeatured, likeCount, hasViewerLiked, ' \
                             'canRemove, canReport, canEdit, source, viewerCanLike, canComment, isAuthorWeakReference, isTranslatable, ' \
                             'timestamp_time, timestamp_text, timestamp_verbose, spamReplyCount, interestingReplyOffset, interestingReplyId, ' \
                             'recentReplyTimestamp_time, recentReplyTimestamp_text, recentReplyTimestamp_verbose FROM comment WHERE fbid = %s;')

            dataUser = (fbid,)

            cursor.execute(readFBCommentQuery, dataUser)

            for (idComment, id, fbid, legacyid, text, author, ftidentifier, isFeatured, likeCount, hasViewerLiked, canRemove, canReport, canEdit, source,
            viewerCanLike, canComment, isAuthorWeakReference, isTranslatable, timestamp_time, timestamp_text, timestamp_verbose, spamReplyCount,
            interestingReplyOffset, interestingReplyId, recentReplyTimestamp_time, recentReplyTimestamp_text, recentReplyTimestamp_verbose) in cursor:
                comment = FacebookComment(idComment, id, fbid, legacyid, text, ftidentifier, isFeatured, likeCount, hasViewerLiked, canRemove, canReport,
                                          canEdit, source, viewerCanLike, canComment, isAuthorWeakReference, isTranslatable, timestamp_time,
                                          timestamp_text, timestamp_verbose, spamReplyCount, interestingReplyOffset, interestingReplyId,
                                          recentReplyTimestamp_time, recentReplyTimestamp_text, recentReplyTimestamp_verbose)

            cursor.close()
            self.db.closeConnection()

        except mysql.connector.Error as ex:
            print(ex)
            print('Error reading a Facebook Comment in the DB.')
        return comment

    def readComments(self):
        comments = []
        try:
            cnx = self.db.openConnection()
            cursor = cnx.cursor()

            readFBCommentsQuery = ('SELECT idComment, id, fbid, legacyid, text, author, ftidentifier, isFeatured, likeCount, hasViewerLiked, ' \
                             'canRemove, canReport, canEdit, source, viewerCanLike, canComment, isAuthorWeakReference, isTranslatable, ' \
                             'timestamp_time, timestamp_text, timestamp_verbose, spamReplyCount, interestingReplyOffset, interestingReplyId, ' \
                             'recentReplyTimestamp_time, recentReplyTimestamp_text, recentReplyTimestamp_verbose FROM comment;')


            cursor.execute(readFBCommentsQuery)

            for (idComment, id, fbid, legacyid, text, author, ftidentifier, isFeatured, likeCount, hasViewerLiked, canRemove, canReport, canEdit, source,
            viewerCanLike, canComment, isAuthorWeakReference, isTranslatable, timestamp_time, timestamp_text, timestamp_verbose, spamReplyCount,
            interestingReplyOffset, interestingReplyId, recentReplyTimestamp_time, recentReplyTimestamp_text, recentReplyTimestamp_verbose) in cursor:
                comment = FacebookComment(idComment, id, fbid, legacyid, text, ftidentifier, isFeatured, likeCount, hasViewerLiked, canRemove, canReport,
                                          canEdit, source, viewerCanLike, canComment, isAuthorWeakReference, isTranslatable, timestamp_time,
                                          timestamp_text, timestamp_verbose, spamReplyCount, interestingReplyOffset, interestingReplyId,
                                          recentReplyTimestamp_time, recentReplyTimestamp_text, recentReplyTimestamp_verbose)
                comments.append(comment)

            cursor.close()
            self.db.closeConnection()

        except mysql.connector.Error as ex:
            print(ex.fp.read())
            print('Error reading Facebook comments in the DB.')
        return comments
from DBLayout.DBConnection import DBConnection, mysql
from EntitiesLayout.FacebookComment import FacebookComment
from EntitiesLayout.FacebookUser import FacebookUser

__author__ = 'David'


class FacebookCommentDB:


    def __init__(self):
        self.db = DBConnection()

    def insertComment(self, comment: FacebookComment, postFbId):
        try:
            cnx = self.db.openConnection()
            cursor = cnx.cursor()
            addFBCommentQuery = 'INSERT INTO comment(idComment, id, fbid, postFbId, legacyid, text, author, ftidentifier, isFeatured, likeCount, hasViewerLiked, ' \
                             'canRemove, canReport, canEdit, source, viewerCanLike, canComment, isAuthorWeakReference, isTranslatable, ' \
                             'timestamp_time, timestamp_text, timestamp_verbose, spamReplyCount, interestingReplyOffset, interestingReplyId, ' \
                             'recentReplyTimestamp_time, recentReplyTimestamp_text, recentReplyTimestamp_verbose)' \
                             'VALUES (NULL, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);'
            dataUser = (comment.id, comment.fbid, postFbId, comment.legacyId, comment.body.text, comment.author, comment.ftIdentifier, comment.isFeatured,
                        comment.likeCount, comment.hasViewerLiked, comment.canRemove, comment.canReport, comment.canEdit, comment.source, comment.viewerCanLike,
                        comment.canComment, comment.isAuthorWeakReference, comment.isTranslatable, comment.timestamp.time,
                        comment.timestamp.text, comment.timestamp.verbose, comment.spamReplyCount, comment.interestingReplyOffset,
                        comment.interestingReplyId, comment.recentReplyTimestamp.time, comment.recentReplyTimestamp.text,
                        comment.recentReplyTimestamp.verbose)

            cursor.execute(addFBCommentQuery, dataUser)
            cnx.commit()
            cursor.close()
            self.db.closeConnection()

        except mysql.connector.Error as err:
            print('Error writing a Facebook comment in the DB. ' + str(err))
            return False
        except AttributeError as err:
            print('Comment register can\'t be stored. ' + str(err))
            return False
        return True

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
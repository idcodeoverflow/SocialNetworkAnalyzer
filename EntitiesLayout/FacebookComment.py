import json

__author__ = 'David'


class FacebookComment:

    def __init__(self, facebookCommentId: int = 0, id: int = 0, fbid: int = 0, legacyId : int = 0, body : CommentBody = CommentBody('', [], []),
                 author: int = 0, ftIdentifier: int = 0, isFeatured: bool = False, likeCount: int = 0, hasViewerLiked: bool = False,
                 canRemove: bool = False, canReport: bool = False, canEdit: bool = False, source: str = '', viewerCanLike: bool = False,
                 canComment: bool = False, isAuthorWeakReference: bool = False, isTranslatable: bool = False,
                 timestamp: Timestamp = Timestamp(0,'',''), interestingReplyOffset: int = 0, interestingReplyId: int = 0,
                 recentReplyTimestamp: Timestamp = Timestamp(0,'',''), spamReplyCount: int = 0):
        self.facebookCommentId = facebookCommentId
        self.id = id
        self.fbid = fbid
        self.legacyId = legacyId
        self.body = body
        self.author = author
        self.ftIdentifier = ftIdentifier
        self.isFeatured = isFeatured
        self.likeCount = likeCount
        self.hasViewerLiked = hasViewerLiked
        self.canRemove = canRemove
        self.canReport = canReport
        self.canEdit = canEdit
        self.source = source
        self.viewerCanLike = viewerCanLike
        self.canComment = canComment
        self.isAuthorWeakReference = isAuthorWeakReference
        self.isTranslatable = isTranslatable
        self.timestamp = timestamp
        self.interestingReplyOffset = interestingReplyOffset
        self.interestingReplyId = interestingReplyId
        self.recentReplyTimestamp = recentReplyTimestamp
        self.spamReplyCount = spamReplyCount

    def __init__(self, mp: {}):
        time = 0
        text = ''
        verbose = ''
        comment = FacebookComment()
        comment.id = mp['id']
        comment.fbid = mp['fbid']
        comment.legacyId = mp['legacyid']
        comment.body = mp['body']
        comment.author = mp['author']
        comment.ftIdentifier = mp['ftentidentifier']
        comment.isFeatured = mp['isfeatured']
        comment.likeCount = mp['likecount']
        comment.hasViewerLiked = mp['hasviewerliked']
        comment.canRemove = mp['canremove']
        comment.canReport = mp['canreport']
        comment.canEdit = mp['canedit']
        comment.source = mp['source']
        comment.viewerCanLike = mp['viewercanlike']
        comment.canComment = mp['cancomment']
        comment.isAuthorWeakReference = mp['isauthorweakreference']
        comment.isTranslatable = mp['istranslatable']
        time = mp['timestamp']
        timestampData = json.loads(time)
        if 'time' in timestampData.keys():
            time = timestampData['time']
        if 'text' in timestampData.keys():
            text = timestampData['text']
        if 'verbose' in timestampData.keys():
            verbose = timestampData['verbose']
        comment.timestamp = Timestamp(time, text, verbose)
        comment.interestingReplyOffset = mp['']
        comment.interestingReplyId = mp['']
        comment.recentReplyTimestamp = mp['']
        comment.spamReplyCount = mp['']



class CommentBody:

    text = ''
    ranges = []
    aggregatedRanges = []

    def __init__(self, text: str, ranges: [], agregatedRanges: []):
        self.text = text
        self.ranges = ranges
        self.aggregatedRanges = agregatedRanges

    @classmethod
    def init(self, map):
        return CommentBody()

class Timestamp:

    time = 0
    text = ''
    verbose = ''

    def __init__(self, time: int, text: str, verbose: str):
        self.time = time
        self.text = text
        self.verbose = verbose



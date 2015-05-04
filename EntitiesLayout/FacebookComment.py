

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



class CommentBody:

    text = ''
    ranges = []
    aggregatedRanges = []

    def __init__(self, text: str, ranges: [], agregatedRanges: []):
        self.text = text
        self.ranges = ranges
        self.aggregatedRanges = agregatedRanges

class Timestamp:

    time = 0
    text = ''
    verbose = ''

    def __init__(self, time: int, text: str, verbose: str):
        self.time = time
        self.text = text
        self.verbose = verbose



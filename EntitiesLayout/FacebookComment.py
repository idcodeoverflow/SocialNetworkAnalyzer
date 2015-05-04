

__author__ = 'David'


class FacebookComment:

    def __init__(self):
        self.facebookCommentId = 0
        self.id = 0
        self.fbid = 0
        self.legacyId = 0
        self.body = CommentBody('', [], [])
        self.author = 0
        self.ftIdentifier = 0
        self.isFeatured = False
        self.likeCount = 0
        self.hasViewerLiked = False
        self.canRemove = False
        self.canReport = False
        self.canEdit = False
        self.source = ""
        self.viewerCanLike = False
        self.canCommnet = False
        self.isAuthorWeakReference = False
        self.isTranslatable = False
        self.timestamp = Timestamp(0, '', '')
        self.interestingReplyOffset = 0
        self.interestingReplyId = 0
        self.recentReplyTimestamp = Timestamp(0, '', '')
        self.spamReplyCount = Timestamp(0, '', '')



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



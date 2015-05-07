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
        ttext = ''
        ranges = []
        aggregatedRanges = []
        comment = FacebookComment()
        try:
            if 'id' in mp.keys():
                comment.id = mp['id']
            if 'fbid' in mp.keys():
                comment.fbid = mp['fbid']
            if 'legacyid' in mp.keys():
                comment.legacyId = mp['legacyid']

            if 'body' in mp.keys():
                bodyData = json.loads(mp['body'])
                if 'text' in bodyData.keys():
                    ttext = bodyData['text']
                if 'ranges' in bodyData.keys():
                    ranges = bodyData['ranges']
                if 'aggregatedranges' in bodyData.keys():
                    aggregatedRanges = bodyData['aggregatedranges']
                comment.body = CommentBody(ttext, ranges, aggregatedRanges)

            if 'author' in mp.keys():
                comment.author = mp['author']
            if 'ftentidentifier' in mp.keys():
                comment.ftIdentifier = mp['ftentidentifier']
            if 'isfeatured' in mp.keys():
                comment.isFeatured = mp['isfeatured']
            if 'likecount' in mp.keys():
                comment.likeCount = mp['likecount']
            if 'hasviewerliked' in mp.keys():
                comment.hasViewerLiked = mp['hasviewerliked']
            if 'canremove' in mp.keys():
                comment.canRemove = mp['canremove']
            if 'canreport' in mp.keys():
                comment.canReport = mp['canreport']
            if 'canedit' in mp.keys():
                comment.canEdit = mp['canedit']
            if 'source' in mp.keys():
                comment.source = mp['source']
            if 'viewercanlike' in mp.keys():
                comment.viewerCanLike = mp['viewercanlike']
            if 'cancomment' in mp.keys():
                comment.canComment = mp['cancomment']
            if 'isauthorweakreference' in mp.keys():
                comment.isAuthorWeakReference = mp['isauthorweakreference']
            if 'istranslatable' in mp.keys():
                comment.isTranslatable = mp['istranslatable']

            if 'timestamp' in mp.keys():
                timestampData = json.loads(mp['timestamp'])
                if 'time' in timestampData.keys():
                    time = timestampData['time']
                if 'text' in timestampData.keys():
                    text = timestampData['text']
                if 'verbose' in timestampData.keys():
                    verbose = timestampData['verbose']
                comment.timestamp = Timestamp(time, text, verbose)

            if 'interestingreplyoffset' in mp.keys():
                comment.interestingReplyOffset = mp['interestingreplyoffset']
            if 'interestingreplyid' in mp.keys():
                comment.interestingReplyId = mp['interestingreplyid']

            if 'recentreplytimestamp' in mp.keys():
                timestampData = json.loads(mp['recentreplytimestamp'])
                if 'time' in timestampData.keys():
                    time = timestampData['time']
                if 'text' in timestampData.keys():
                    text = timestampData['text']
                if 'verbose' in timestampData.keys():
                    verbose = timestampData['verbose']
                comment.recentReplyTimestamp = Timestamp(time, text, verbose)

            if 'spamreplycount' in mp.keys():
                comment.spamReplyCount = mp['spamreplycount']

        except KeyError:
            print('One attribute is missing in comment.')
        return comment


class CommentBody:

    text = ''
    ranges = []
    aggregatedRanges = []

    def __init__(self, text: str, ranges: [], aggregatedRanges: []):
        self.text = text
        self.ranges = ranges
        self.aggregatedRanges = aggregatedRanges

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



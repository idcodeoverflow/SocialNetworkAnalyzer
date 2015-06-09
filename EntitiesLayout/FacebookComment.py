import json

__author__ = 'David'


class FacebookComment:

    def __init__(self, mp: dict = {}, postFbId: int = 0):
        time = 0
        text = ''
        verbose = ''
        ttext = ''
        ranges = []
        aggregatedRanges = []
        self.postFbId = postFbId
        try:
            if 'id' in mp.keys():
                self.id = mp['id']
            else:
                self.id = None

            if 'fbid' in mp.keys():
                self.fbid = mp['fbid']
            else:
                self.fbid = None

            if 'legacyid' in mp.keys():
                self.legacyId = mp['legacyid']
            else:
                self.legacyId = None

            ttext = ''
            ranges = []
            aggregatedRanges = []

            if 'body' in mp.keys():
                if 'text' in mp['body'].keys():
                    ttext = mp['body']['text']
                else:
                    ttext = None
                if 'ranges' in mp['body'].keys():
                    ranges = mp['body']['ranges']
                if 'aggregatedranges' in mp['body'].keys():
                    aggregatedRanges = mp['body']['aggregatedranges']
                self.body = CommentBody(ttext, ranges, aggregatedRanges)
            else:
                self.body = CommentBody(None, None, None)

            if 'author' in mp.keys():
                self.author = mp['author']
            else:
                self.author = None

            if 'ftentidentifier' in mp.keys():
                self.ftIdentifier = mp['ftentidentifier']
            else:
                self.ftIdentifier = None

            if 'isfeatured' in mp.keys():
                self.isFeatured = mp['isfeatured']
            else:
                self.isFeatured = None

            if 'likecount' in mp.keys():
                self.likeCount = mp['likecount']
            else:
                self.likeCount = None

            if 'hasviewerliked' in mp.keys():
                self.hasViewerLiked = mp['hasviewerliked']
            else:
                self.hasViewerLiked = None

            if 'canremove' in mp.keys():
                self.canRemove = mp['canremove']
            else:
                self.canRemove = None

            if 'canreport' in mp.keys():
                self.canReport = mp['canreport']
            else:
                self.canReport = None

            if 'canedit' in mp.keys():
                self.canEdit = mp['canedit']
            else:
                self.canEdit = None

            if 'source' in mp.keys():
                self.source = mp['source']
            else:
                self.source = None

            if 'viewercanlike' in mp.keys():
                self.viewerCanLike = mp['viewercanlike']
            else:
                self.viewerCanLike = None

            if 'cancomment' in mp.keys():
                self.canComment = mp['cancomment']
            else:
                self.canComment = None

            if 'isauthorweakreference' in mp.keys():
                self.isAuthorWeakReference = mp['isauthorweakreference']
            else:
                self.isAuthorWeakReference = None

            if 'istranslatable' in mp.keys():
                self.isTranslatable = mp['istranslatable']
            else:
                self.isTranslatable = None

            time = 0
            text = ''
            verbose = ''
            if 'timestamp' in mp.keys():

                if 'time' in mp['timestamp'].keys():
                    time = mp['timestamp']['time']
                if 'text' in mp['timestamp'].keys():
                    text = mp['timestamp']['text']
                if 'verbose' in mp['timestamp'].keys():
                    verbose = mp['timestamp']['verbose']
                self.timestamp = Timestamp(time, text, verbose)
            else:
                self.timestamp = Timestamp(None, None, None)

            if 'interestingreplyoffset' in mp.keys():
                self.interestingReplyOffset = mp['interestingreplyoffset']
            else:
                self.interestingReplyOffset = None
            if 'interestingreplyid' in mp.keys():
                self.interestingReplyId = mp['interestingreplyid']
            else:
                self.interestingReplyId = None

            if 'recentreplytimestamp' in mp.keys():
                if 'time' in mp['recentreplytimestamp'].keys():
                    time = mp['recentreplytimestamp']['time']
                if 'text' in mp['recentreplytimestamp'].keys():
                    text = mp['recentreplytimestamp']['text']
                if 'verbose' in mp['recentreplytimestamp'].keys():
                    verbose = mp['recentreplytimestamp']['verbose']
                self.recentReplyTimestamp = Timestamp(time, text, verbose)
            else:
                self.recentReplyTimestamp = Timestamp(None, None, None)

            if 'spamreplycount' in mp.keys():
                self.spamReplyCount = mp['spamreplycount']
            else:
                self.spamReplyCount = None

        except KeyError:
            print('One attribute is missing in comment.')


    def initialize(self, id, fbid, postFbId, legacyid, text, ftidentifier, isFeatured, likeCount, hasViewerLiked, canRemove, canReport,
                                          canEdit, source, viewerCanLike, canComment, isAuthorWeakReference, isTranslatable, timestamp_time,
                                          timestamp_text, timestamp_verbose, spamReplyCount, interestingReplyOffset, interestingReplyId,
                                          recentReplyTimestamp_time, recentReplyTimestamp_text, recentReplyTimestamp_verbose):
        self.postFbId = postFbId
        self.id = id
        self.fbid = fbid
        self.legacyId = legacyid
        self.body = CommentBody(text, None, None)
        self.ftIdentifier = ftidentifier
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
        self.timestamp = Timestamp(timestamp_time, timestamp_text, timestamp_verbose)
        self.spamReplyCount = spamReplyCount
        self.interestingReplyOffset = interestingReplyOffset
        self.interestingReplyId = interestingReplyId
        self.recentReplyTimestamp = Timestamp(recentReplyTimestamp_time, recentReplyTimestamp_text, recentReplyTimestamp_verbose)






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



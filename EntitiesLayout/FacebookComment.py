import json

__author__ = 'David'


class FacebookComment:



    def __init__(self, mp: dict = {}):
        time = 0
        text = ''
        verbose = ''
        ttext = ''
        ranges = []
        aggregatedRanges = []
        try:
            if 'id' in mp.keys():
                self.id = mp['id']
            if 'fbid' in mp.keys():
                self.fbid = mp['fbid']
            if 'legacyid' in mp.keys():
                self.legacyId = mp['legacyid']

            ttext = ''
            ranges = []
            aggregatedRanges = []

            if 'body' in mp.keys():
                if 'text' in mp['body'].keys():
                    ttext = mp['body']['text']
                if 'ranges' in mp['body'].keys():
                    ranges = mp['body']['ranges']
                if 'aggregatedranges' in mp['body'].keys():
                    aggregatedRanges = mp['body']['aggregatedranges']
                self.body = CommentBody(ttext, ranges, aggregatedRanges)

            if 'author' in mp.keys():
                self.author = mp['author']
            if 'ftentidentifier' in mp.keys():
                self.ftIdentifier = mp['ftentidentifier']
            if 'isfeatured' in mp.keys():
                self.isFeatured = mp['isfeatured']
            if 'likecount' in mp.keys():
                self.likeCount = mp['likecount']
            if 'hasviewerliked' in mp.keys():
                self.hasViewerLiked = mp['hasviewerliked']
            if 'canremove' in mp.keys():
                self.canRemove = mp['canremove']
            if 'canreport' in mp.keys():
                self.canReport = mp['canreport']
            if 'canedit' in mp.keys():
                self.canEdit = mp['canedit']
            if 'source' in mp.keys():
                self.source = mp['source']
            if 'viewercanlike' in mp.keys():
                self.viewerCanLike = mp['viewercanlike']
            if 'cancomment' in mp.keys():
                self.canComment = mp['cancomment']
            if 'isauthorweakreference' in mp.keys():
                self.isAuthorWeakReference = mp['isauthorweakreference']
            if 'istranslatable' in mp.keys():
                self.isTranslatable = mp['istranslatable']

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

            if 'interestingreplyoffset' in mp.keys():
                self.interestingReplyOffset = mp['interestingreplyoffset']
            if 'interestingreplyid' in mp.keys():
                self.interestingReplyId = mp['interestingreplyid']

            if 'recentreplytimestamp' in mp.keys():
                if 'time' in mp['recentreplytimestamp'].keys():
                    time = mp['recentreplytimestamp']['time']
                if 'text' in mp['recentreplytimestamp'].keys():
                    text = mp['recentreplytimestamp']['text']
                if 'verbose' in mp['recentreplytimestamp'].keys():
                    verbose = mp['recentreplytimestamp']['verbose']
                self.recentReplyTimestamp = Timestamp(time, text, verbose)

            if 'spamreplycount' in mp.keys():
                self.spamReplyCount = mp['spamreplycount']

        except KeyError:
            print('One attribute is missing in comment.')



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



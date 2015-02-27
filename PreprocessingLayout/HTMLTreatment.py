__author__ = 'David'


class HTMLTreatment:
    html = ''
    comments = []
    paragraphs = []

    def __init__(self, html: str):
        self.html = html

    def getIniEnd(self, lIni: str, lEnd: str, ini: int=0, end: int=0):
        if ini != 0 or end != 0:
            ini = self.html.find(lIni, ini + lEnd.__len__(), self.html.__len__())
            end = self.html.find(lEnd, ini, self.html.__len__())
        else:
            ini = self.html.find(lIni)
            end = self.html.find(lEnd, ini, self.html.__len__())
        return ini, end

    def extractComments(self):
        ini, end = self.getIniEnd('<--', '-->')
        self.comments = []
        while ini > -1:
            self.comments.append(self.html[ini + 3: end])
            ini, end = self.getIniEnd('<--', '-->', end, self.html.__len__())
        return self.comments

    def extractParagraphs(self):
        ini, end = self.getIniEnd('<p>', '</p>')
        self.paragraphs = []
        while ini > -1:
            self.paragraphs.append(self.html[ini + 3: end])
            ini, end = self.getIniEnd('<p>', '</p>', end, self.html.__len__())
        return self.paragraphs


h = HTMLTreatment(1, '')
for i in h.extractParagraphs():
    print(i)
for i in h.extractComments():
    print(i)
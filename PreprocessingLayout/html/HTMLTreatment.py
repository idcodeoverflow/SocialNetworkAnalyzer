from PreprocessingLayout.html import HexCharacterMapping

__author__ = 'David'


class HTMLTreatment:
    html = ''
    comments = []
    paragraphs = []

    def __init__(self, html: str):
        self.html = html

    def replaceHexCharacters(self):
        chars = HexCharacterMapping()
        for char in chars.characters.keys():
            self.html = self.html.replace(char, chars.characters[char])

    def removeLinks(self):
        iniLen = self.html.__len__()
        ini, end = self.getIniEnd('href', '>')

        while self.html[ini] != '<' and ini > 0:
            ini -= 1

        tempHTML = self.html[:ini - 1]
        tempHTML += self.html[end + 1:]


        while ini > -1 and end > -1:

            self.html = tempHTML
            ini, end = self.getIniEnd('href', '>')

            while self.html[ini] != '<' and ini > 0:
                ini -= 1
            if ini <= -1 and end <= -1:
                continue
            tempHTML = self.html[:ini - 1] + ' '
            tempHTML += self.html[end + 1:]

        if iniLen > self.html.__len__():
            self.html = tempHTML


    def getIniEnd(self, lIni: str, lEnd: str, ini: int=0, end: int=0):
        if ini != 0 or end != 0:
            ini = self.html.find(lIni, ini + lEnd.__len__(), self.html.__len__())
            end = self.html.find(lEnd, ini, self.html.__len__())
        else:
            ini = self.html.find(lIni)
            end = self.html.find(lEnd, ini, self.html.__len__())
        return ini, end

    def getIniEndFromText(self, text: str, lIni: str, lEnd: str, ini: int=0, end: int=0):
        if ini != 0 or end != 0:
            ini = text.find(lIni, ini + lEnd.__len__(), text.__len__())
            end = text.find(lEnd, ini, text.__len__())
        else:
            ini = text.find(lIni)
            end = text.find(lEnd, ini, text.__len__())
        return ini, end

    def extractComments(self):
        ini, end = self.getIniEnd('<!--', '-->')
        self.comments = []
        while ini > -1:
            self.comments.append(self.html[ini + 4: end])
            ini, end = self.getIniEnd('<!--', '-->', end, self.html.__len__())
        return self.comments

    def extractParagraphs(self):
        ini, end = self.getIniEnd('<p>', '</p>')
        self.paragraphs = []
        while ini > -1:
            self.paragraphs.append(self.html[ini + 3: end])
            ini, end = self.getIniEnd('<p>', '</p>', end, self.html.__len__())
        return self.paragraphs

    def removeHTMLLabelsFromText(self, text: str):
        ini, end = self.getIniEndFromText(text,'<', '>')
        while ini > -1 and end > -1:
            text = text[:ini - 1] + ' ' + text[end + 1:]
            ini, end = self.getIniEndFromText(text,'<', '>')

        return text


import json
from PreprocessingLayout.html.HexCharacterMapping import HexCharacterMapping

__author__ = 'David'


class HTMLTreatment:
    html = ''
    comments = []
    paragraphs = []

    def __init__(self, htmlText: str):
        self.html = htmlText

    def replaceHexCharacters(self):
        chars = HexCharacterMapping()
        for char in chars.characters.keys():
            self.html = self.html.replace(char, chars.characters[char])

    def removerURLs(self):
        ini, end = self.getIniEnd('http', ' ')

        while ini > -1:
            tempHTML = self.html[:ini - 1] + ' '
            if end < self.html.__len__() and end > -1:
                tempHTML += self.html[end + 1:]
            self.html = tempHTML
            ini, end = self.getIniEnd('http', ' ')

    def removeHTMLLabels(self):
        ini, end = self.getIniEnd('<', '>')
        while ini > -1 and end > -1 and end < self.html.__len__():
            tempHTML = self.html[:ini - 1] + ' '
            if end + 1 < self.html.__len__():
                print(self.html)
                tempHTML += self.html[end + 1:]

            self.html = tempHTML
            ini, end = self.getIniEnd('<', '>')

    def removeLinks(self):
        iniLen = self.html.__len__()
        ini, end = self.getIniEnd('href', '>')

        while ini > 0 and self.html[ini] != '<':
            ini -= 1

        tempHTML = self.html[:ini - 1] + ' '
        tempHTML += self.html[end + 1:]

        while ini > -1 and end > -1:

            self.html = tempHTML
            ini, end = self.getIniEnd('href', '>')

            while self.html[ini] != '<' and ini > 0:
                ini -= 1
            if ini <= -1 and end <= -1:
                continue

            if ini != 0:
                tempHTML = self.html[:ini - 1] + ' '
            else:
                tempHTML = self.html[:ini] + ' '

            if end < self.html.__len__():
                tempHTML += ' ' + self.html[end + 1:]


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

    @classmethod
    def getIniEndFromText(self, text: str, lIni: str, lEnd: str, ini: int=0, end: int=0):
        if ini != 0 or end != 0:
            ini = text.find(lIni, ini + lEnd.__len__(), text.__len__())
            end = text.find(lEnd, ini, text.__len__())
        else:
            ini = text.find(lIni)
            end = text.find(lEnd, ini, text.__len__())
        return ini, end

    def extractHTMLComments(self):
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

    @classmethod
    def removeHTMLLabelsFromText(self, text: str):
        ini, end = self.getIniEndFromText(text,'<', '>')
        while ini > -1 and end > -1 and end < text.__len__():
            if ini - 1 < 0 or end - 1 < 0:
                break
            text = text[:ini - 1] + ' ' + text[end + 1:]
            ini, end = self.getIniEndFromText(text,'<', '>')

        return text

    def countLikes(self):
        try:
            sentence = 'likecountreduced'
            hexChar = '\\u00a0'
            ini = self.html.find(sentence) + 19
            end = ini
            if ini == -1:
                return 0
            while end < self.html.__len__() and self.html[end] != '"':
                end += 1
            number = self.html[ini : end]
            number = number.replace(hexChar,'')
            likesCount = int(number)
        except ValueError:
            return 0
        return likesCount

    def getFacebookComments(self):
        comms = {}
        strs = []
        data = {}
        text = ''
        self.replaceHexCharacters()
        ini, end = self.getIniEnd('{\"content\":{\"stream_pagelet\"', ');}, "onPageletArrive stream_pagelet")()')
        if ini > -1:
            text = self.html[ini : end]
            ini, end = self.getIniEndFromText(text, '"comments"', ']')
            text = text[ini : ]
            #print(text)
            count = 1
            index = 12
            #get comments JSON string
            while index < text.__len__() and count != 0:
                if text[index] == '[' :
                    count += 1
                elif text[index] == ']':
                    count -= 1
                index += 1

            if count != 0: #if there isn't a valid string return an empty dictionary
                return {}
            text = '{' + text[ : index] + '}'


            index = 14

            while index < text.__len__():
                ini = index
                count = 1
                while index < text.__len__() and count != 0:
                    if text[index] == '{':
                        count += 1
                        if count == 1:
                            ini = index
                    elif text[index] == '}':
                        count -= 1
                    index += 1
                #print(text[ini - 1 : index])
                strs.append(text[ini - 1 : index])
                index += 2

            data = json.loads(text)
            self.comments = strs

            #temp show results
            #for key in data.keys():
            #    print(key + ' : ' + str(data[key]))
        return comms

    def getFBIds(self):
        lis = {}
        self.replaceHexCharacters()
        ini, end = self.getIniEnd('fbid=', '&')
        ini -= 1
        self.paragraphs = []
        while ini > -1:
            lis[self.html[ini + 6: end]] = '1'
            ini, end = self.getIniEnd('?fbid=', '&', end, self.html.__len__())
        return lis.keys()

    def commentsJSONToDictionary(self):
        commentsObjects = []
        if self.comments.__len__() < 1:
            print("No comments to extract.")
            return {}
        dic = json.loads(self.comments[0])
        print('--------------------->' + str(dic))
        return dic



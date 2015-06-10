from PreprocessingLayout.language.RestrictedSymbolsMapping import RestrictedSymbolsMapping

__author__ = 'David'


class LanguageProcessor:

    text = ''

    def __init__(self, text: str):
        self.text = text


    def getTokens(self):
        return self.text.split(' ')

    def removeSymbols(self):
        symbols = RestrictedSymbolsMapping().symbols
        for key in symbols.keys():
            self.text = self.text.replace(key, symbols[key])

    @classmethod
    def isNegative(cls, word):
        negative = Positive()


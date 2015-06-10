from _operator import pos
from PreprocessingLayout.language.NegativeDictionary import NegativeDictionary
from PreprocessingLayout.language.PositiveDictionary import PositiveDictionary
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
    def isNegativeOrPositive(cls, word):
        negative = NegativeDictionary()
        positive = PositiveDictionary()
        if negative.isNegative(word):
            return 1
        if positive.isPositive(word):
            return 2
        return 0


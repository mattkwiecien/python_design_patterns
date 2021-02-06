from decorator.translators.translator import Translator
from decorator.translators.translators import *


def AddGermanTranslation(self):
    return GermanTranslator(self)


def AddPersianTranslation(self):
    return PersianTranslator(self)


def AddZuluTranslation(self):
    return ZuluTranslator(self)


def AddChineseTranslation(self):
    return ChineseTranslator(self)


def AddFrenchTranslation(self):
    return FrenchTranslator(self)


def AddLatinTranslation(self):
    return LatinTranslator(self)


Translator.AddGermanTranslation = AddGermanTranslation
Translator.AddFrenchTranslation = AddFrenchTranslation
Translator.AddChineseTranslation = AddChineseTranslation
Translator.AddLatinTranslation = AddLatinTranslation
Translator.AddZuluTranslation = AddZuluTranslation
Translator.AddPersianTranslation = AddPersianTranslation

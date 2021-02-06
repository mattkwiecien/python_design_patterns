from decorator.translators.translator import TranslatorBase


class GermanTranslator(TranslatorBase):

    def Translate(self, input):
        self._translator.Translate(input)
        print("The German translation is: " +
              self._google_trans.translate(input, lang_tgt='de'))


class FrenchTranslator(TranslatorBase):

    def Translate(self, input):
        self._translator.Translate(input)
        print("The French translation is: " +
              self._google_trans.translate(input, lang_tgt='fr'))


class ChineseTranslator(TranslatorBase):

    def Translate(self, input):
        self._translator.Translate(input)
        print("The Chinese translation is: " +
              self._google_trans.translate(input, lang_tgt='zh-TW'))


class PersianTranslator(TranslatorBase):

    def Translate(self, input):
        self._translator.Translate(input)
        print("The Persian translation is: " +
              self._google_trans.translate(input, lang_tgt='fa'))


class ZuluTranslator(TranslatorBase):

    def Translate(self, input):
        self._translator.Translate(input)
        print("The Zulu translation is: " +
              self._google_trans.translate(input, lang_tgt='zu'))


class LatinTranslator(TranslatorBase):

    def Translate(self, input):
        self._translator.Translate(input)
        print("The Latin translation is: " +
              self._google_trans.translate(input, lang_tgt='la'))

from google_trans_new import google_translator


class Translator():
    def Translate(self, input):
        pass


class TranslatorBase(Translator):
    _translator: Translator = None

    def __init__(self, translator: Translator):
        self._translator = translator
        self._google_trans = google_translator()

    @property
    def translator(self):
        return self._translator

    def Translate(self, input):
        self._translator.Translate(input)

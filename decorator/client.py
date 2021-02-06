from decorator.translators import *


def consumer(translator: Translator):
    translator.Translate("Hello World")


if __name__ == "__main__":
    # Decorate base translator using ad hoc extension methods.
    translator = Translator()
    translator = translator.AddGermanTranslation()
    translator = translator.AddFrenchTranslation()
    translator = translator.AddChineseTranslation()
    translator = translator.AddLatinTranslation()
    translator = translator.AddZuluTranslation()
    translator = translator.AddPersianTranslation()
    consumer(translator)

    # Typical decorator pattern below

    # translator = Translator()
    # translator = GermanTranslator(translator)
    # translator = FrenchTranslator(translator)
    # translator = ChineseTranslator(translator)
    # translator = LatinTranslator(translator)
    # translator = ZuluTranslator(translator)
    # translator = PersianTranslator(translator)
    # consumer(translator)

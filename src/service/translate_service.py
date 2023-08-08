from deep_translator import GoogleTranslator


class TranslateService:
    def __init__(self, source='auto', target='de'):
        self.source = source
        self.target = target
        self.translator = GoogleTranslator(source=source, target=target)

    def translate(self, to_translate):
        return self.translator.translate(to_translate)

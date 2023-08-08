class CountryTranslator:
    def __init__(self, translator):
        self.translator = translator

    def translate(self, to_translate):
        return self.translator.translate(to_translate)

    def translate_dict(self, countries):
        _countries = dict()
        for country_code, country_name in countries.items():
            _countries[country_code] = self.translator.translate(country_name)
        return _countries


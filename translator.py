from utils import singleton
import googletrans

@singleton
class Translator(object):
    def __init__(self):
        super().__init__()
        self._translator = googletrans.Translator()

    def translate(self, article, dest='en'):
        return self._translator.translate(article, dest=dest).text
        
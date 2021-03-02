from utils import singleton
from summa import summarizer
from translator import Translator

@singleton
class Summarizer(object):
    def __init__(self):
        super().__init__()
        self._translator = Translator()
    
    def summarize(self, article, ratio=0.2, dest='zh-cn'):
        x = summarizer.summarize(article, ratio=ratio)
        x = self._translator.translate(x, dest=dest)
        return x
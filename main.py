import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

class Mood():
  def __init__(self, sentence):
    self.mood = ""
    self.sia = SentimentIntensityAnalyzer()
    self.sentence = sentence
    self.score = {}
    self.compound = 0
  def mood(self):
    self.score = self.sia.polarity_scores(self.sentence)
    self.compound = self.scores['compound']
    if self.compound == 0:
      return "neu"
    elif self.compound <= -0.05:
      return "neg"
    elif self.compound >= 0.05:
      return "pos"

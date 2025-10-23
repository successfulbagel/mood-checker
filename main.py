#pip3 install nltk
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
#pip3 install colorama
import colorama

colorama.init()

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
      self.mood = "Neutral"
      return "neu", self.compound
    elif self.compound <= -0.05:
      self.mood = "Negative"
      return "neg", self.compund
    elif self.compound >= 0.05:
      self.mood = "Positive"
      return "pos", self.compund
  def display_mood(self):
    #print(f

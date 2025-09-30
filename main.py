import nltk
from nltk import SentimentIntensityAnalyzer

class Mood():
  def __init__(self, sentence):
    self.mood = ""
    self.sia = SentimentIntensityAnalyzer()
    self.sentence = sentence

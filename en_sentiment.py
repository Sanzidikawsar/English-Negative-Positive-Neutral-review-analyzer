#English Negative-Positive-Neutral review analysis with nltk textblob
import sys
from textblob import TextBlob

print("***Review Analyzer***")

def analyzer(text):
    text = TextBlob(text)
    sentiment = text.sentiment.polarity

    if (sentiment > 0):
        print("\nPositive Review!\n")

    elif (sentiment < 0):
        print("\nNegative Review!\n")

    else:
        print("\nIt\'s Neutral!\n")

def interface():
    print('''
    1. Analyze Review
    2. Exit''')

while(1):
    interface();
    inp = int(input("Enter Choice: "))

    if (inp == 1):
        text = input("Enter Your Review: ")
        analyzer(text)

    elif (inp == 2):
        sys.exit()

    else:
        print("Invalid Input!")



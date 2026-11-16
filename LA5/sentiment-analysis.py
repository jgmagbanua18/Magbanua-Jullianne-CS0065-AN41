from textblob import TextBlob

positive = 0
neutral = 0
negative = 0

for i in range(10):
    sentence = input(f"Enter sentence {i+1}: ")

    s = TextBlob(sentence)
    p = s.sentiment.polarity

    if p < 0:
        print("Negative")
        negative += 1
    elif p == 0:
        print("Neutral")
        neutral += 1
    else:
        print("Positive")
        positive += 1

print("\nSUMMARY")
print("Positive:", positive)
print("Neutral:", neutral)
print("Negative:", negative)
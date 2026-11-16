def number_happy(sentence):
    happy_words = [
        "happy", "joy", "love", "great", "good",
        "excellent", "wonderful", "excited", "amazing", "smile"
    ]

    count = 0
    words = sentence.lower().split()

    for word in words:
        if word.strip(".,!?") in happy_words:
            count += 1

    return count


def number_sad(sentence):
    sad_words = [
        "sad", "bad", "hate", "angry", "upset",
        "terrible", "awful", "depressed", "cry", "lonely"
    ]

    count = 0
    words = sentence.lower().split()

    for word in words:
        if word.strip(".,!?") in sad_words:
            count += 1

    return count


sentence = input("Enter a sentence: ")

happy = number_happy(sentence)
sad = number_sad(sentence)

print("Happy words:", happy)
print("Sad words:", sad)

if happy > sad:
    print("Tone: Positive")
elif sad > happy:
    print("Tone: Negative")
else:
    print("Tone: Neutral")
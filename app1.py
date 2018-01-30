import json

data = json.load(open("data/data.json"))


def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    else:
        return "The word doesn't exist. Please double check it"


word_input = input("Enter word: ")

print(translate(word_input))

import json
from difflib import get_close_matches

data = json.load(open("data/data.json"))


def format_definitions(word, found_definitions):
    """
    Returns formatted string from list
    :param word: String
    :param found_definitions: List
    :return formatted_definition: String
    """
    if type(found_definitions) != list:
        return "Error: function requires only lists"

    formatted_definition = "%s: " % word

    for definition in found_definitions:
        formatted_definition += definition + '\n'
    return formatted_definition


def translate(word):
    """
    Returns the definition of the word entered
    :param word: string
    :return list if word is found or a String of not found:
    """
    word = word.lower()
    if word in data:
        return format_definitions(word, data[word])
    elif word.title() in data:
        return format_definitions(word.title(), data[word.title()])
    elif word.upper() in data:
        return format_definitions(word.upper(), data[word.upper()])
    else:
        # find close matches
        word_matches = get_close_matches(word, data.keys(), cutoff=0.6)
        if len(word_matches) > 0:
            answer = input("Did you mean %s instead? Enter y for yes or any other key for no: " % word_matches[0])
            answer = answer.lower()
            if answer == 'y':
                return format_definitions(word_matches[0], data[word_matches[0]])
        return "The word doesn't exist. Please double check it."


# Input word from console
if __name__ == "__main__":
    word_input = input("Enter word: ")
    print(translate(word_input))

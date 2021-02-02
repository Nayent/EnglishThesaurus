import json
from difflib import get_close_matches

data = json.load(open("data.json"))


def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif w.title() in data:
        return data[w.title()]
    elif w.upper() in data:
        return data[w.upper()]
    elif len(get_close_matches(w, data.keys(), n=1)) > 0:
        bestMatch = get_close_matches(w, data.keys(), n=1)
        choice = input(f"Did you mean {bestMatch[0]}? (Y/N)  ")
        if choice == 'Y' or choice == 'y':
            return data[bestMatch[0]]
        elif choice == "N" or choice == "n":
            return "The word doesn't exist. Please double check it."
        else:
            return "We didn't understand your entry."
    else:
        return "The word doesn't exist. Please double check it."


word = input('Enter word: ')

output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)

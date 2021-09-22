import re
from english_words import english_words_set
from pyinputplus import inputMenu, inputStr
from getch import pause

wordlist = english_words_set
key_letters = ['', '', 'abc', 'def', 'ghi',
            'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']


# --------------------------------------------------
def num_to_words(num: str) -> list:
    digits = [int(s) for s in num]
    regex = "^" + ''.join(["[" + key_letters[x] + "]" for x in digits]) + "$"
    words = list(set([w for w in wordlist if re.search(regex, w)]))
    return words


# --------------------------------------------------
def letter_to_num(letter: str) -> str:
    num = str([i for i in range(2,10) if letter in key_letters[i]][0])
    return num


# --------------------------------------------------
def word_to_num(word: str) -> str:
    digits = [letter_to_num(l) for l in word]
    num = ''.join(digits)
    return num


# --------------------------------------------------
def get_textonyms():
    user_input = inputStr('Enter a word: ', blockRegexes = [r'\d'])
    num = word_to_num(user_input)
    textonyms = [w for w in num_to_words(num) if w != user_input]
    if len(textonyms) == 0:
        print(f'"{user_input}" has 0 textonyms.')
    else:
        print(f'"{user_input}" has {len(textonyms)} textonym(s): {", ".join(textonyms)}')


# --------------------------------------------------
def keys_to_words() -> list:
    user_input = inputStr('Enter some numbers between 2 and 9 (e.g. 378): ', blockRegexes = ['[^23456789]'])
    keys = sorted(set(list(user_input)))
    regex = "^[" + ''.join(key_letters[int(x)] for x in keys) + "]*$"
    words = list(set([w for w in wordlist if re.search(regex, w)]))
    words.sort(key = len)
    print(f'There are {len(words)} words that can be typed using only the keys {", ".join(keys)}. The longest is \'{words[len(words) - 1]}\'.')


# --------------------------------------------------
def main():
    user_options = [
        'Get textonyms of a word',
        'Find out how many words can be typed using a certain group of keys',
        'Something else'
    ]
    user_choice = inputMenu(
        user_options,
        prompt = "What do you want to do?\n",
        numbered=True
    )
    if user_choice == user_options[0]:
        get_textonyms()
    elif user_choice == user_options[1]:
        keys_to_words()
    else:
        print("I can't do anything else.")
    pause("Press any key to exit")


# --------------------------------------------------
if __name__ == '__main__':
    main()




def count_words(book):
    num_words = len(book.split())
    return f"Found {num_words} total words"


def count_characters(book):
    charact_dict = {}
    for letter in book:
        if  charact_dict.get(letter.lower()) is None:
            charact_dict[letter.lower()] = 1
        else:
            charact_dict[letter.lower()]+=1

    return charact_dict

def sort_on(items):
    # print(items["num"])
    return items["num"]


def format_book(char_dict):
    char_list = []
    for char in char_dict:
        char_list.append({"char": char, "num": char_dict[char]})

    char_list.sort(reverse=True, key=sort_on)
    return char_list
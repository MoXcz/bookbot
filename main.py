from stats import get_character_count, get_words_count
import sys


def main():
    if len(sys.argv) < 1:
        print("Usage: python3 main.py <path_to_book>")
    path = sys.argv[1]
    text = open_file(path)
    print_report(text)


def print_report(text):
    char_count = get_words_count(text)
    print(f"{char_count} words found in the document")
    characters = sort_dict(get_character_count(text))
    for char in characters:
        character = char["character"]
        if not character.isalpha():
            continue
        count = char["count"]
        print(f"{character}: {count}")
    print("--------- End ----------")


def sort_on(dict):
    return dict["count"]


def sort_dict(dict):
    characters_list = []
    for character in dict:
        characters_list.append({"character": character, "count": dict[character]})
    characters_list.sort(reverse=True, key=sort_on)
    return characters_list


def open_file(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents


main()

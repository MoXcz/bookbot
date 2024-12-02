def main():
    path = "books/frankenstein.txt"
    text = open_file(path)
    print_report(text)


def print_report(text):
    char_count = get_words_count(text)
    print(f"There are {char_count} words inside the text")
    characters = sort_dict(get_character_count(text))
    for char in characters:
        character = char["character"]
        if not character.isalpha():
            continue
        count = char["count"]
        print(f"{character} was found {count} times")
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


def get_words_count(text):
    list_of_words = text.split()
    return len(list_of_words)


def get_character_count(text):
    character_count = {}
    for character in text:
        character = character.lower()
        if character not in character_count:
            character_count[character] = 1
        else:
            character_count[character] += 1
    return character_count


main()

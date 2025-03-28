def get_character_count(text):
    character_count = {}
    for character in text:
        character = character.lower()
        if character not in character_count:
            character_count[character] = 1
        else:
            character_count[character] += 1
    return character_count


def get_words_count(text):
    list_of_words = text.split()
    return len(list_of_words)

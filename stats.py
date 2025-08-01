def get_number_of_words(text):
    return len(text.split())

def get_character_count(text):
    character_count = dict()
    for char in text.lower():
        if char in character_count:
            character_count[char] += 1
        else:
            character_count[char] = 1
    return character_count

def sort_on(items):
    return items["num"]

def sort_character_count(character_count_dict):
    character_count_list = []
    
    # Append dict to list
    for key in character_count_dict:
        dict_to_append = {"char": key, "num": character_count_dict[key]}
        character_count_list.append(dict_to_append)    
    
    # Sort
    character_count_list.sort(reverse=True, key=sort_on)

    return character_count_list
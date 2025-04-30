def number_of_words(text):
    words = text.split()
    return len(words)

def number_of_characters(text):
    characters = {}
    for char in text:
        char = char.lower()
        if char in characters:
            characters[char] += 1
        else:
            characters[char] = 1
    return characters

def chars_dictionary_to_list_sorted(dictionary):
    dict_list = []
    for char in dictionary:
        aux_dict = {"char": char, "num": dictionary[char]}
        dict_list.append(aux_dict)
        
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list 

def sort_on(dict):
    return dict["num"]
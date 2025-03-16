def get_num_words(bookstr):
    wordcount = bookstr.split()

    print(f"Found {len(wordcount)} total words")

def sort_on(dict_item):
    return dict_item["count"]

def get_num_chars(bookstr):
    lower_bookstr = bookstr.lower()
    characters = {}

    for character in range(0, len(lower_bookstr)):
        if lower_bookstr[character] in characters:
            characters[lower_bookstr[character]] += 1
        else:
            characters[lower_bookstr[character]] = 1
    char_list = []
    for key,value in characters.items():
        char_list.append({"char" : key, "count" : value})
    char_list.sort(reverse=True, key=sort_on)
    



    for item in char_list:
        print(f"{item['char']}: {item['count']}")
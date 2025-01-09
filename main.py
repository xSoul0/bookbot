def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    #print(text)
    word_count = get_word_count_alt(text)
    #print(f"{word_count} words found in the document!")
    char_count = get_character_count(text)
    #print(char_count)
    chars_sorted_list = character_count_to_sorted_list(char_count)
    
    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document!")
    print()
    
    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")
    
    print("--- End report ---")
    
def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def get_word_count(text):
    counter = 0
    for i in text.split():
            counter += 1
    return counter

#alternative solution to getting word count
def get_word_count_alt(text):
    words = text.split()
    return len(words)


#get character count from the entire text
def get_character_count(text):
    characters = {}
    for c in text:
        lowered = c.lower()
        if lowered in characters:
            characters[lowered] += 1
        else:
            characters[lowered] = 1
    return characters


#sorting the character count by number of repeated occurrences
def sort_on(dict):
    return dict["num"]

def character_count_to_sorted_list(char_count_dict):
    sorted_list = []
    for ch in char_count_dict:
        sorted_list.append({"char": ch, "num": char_count_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
    
# this if block prevents the main() function from running when the script is imported into another Python file
if __name__ == "__main__":
    main()
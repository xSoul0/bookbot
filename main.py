def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    #print(text)
    word_count = get_word_count_alt(text)
    print(f"{word_count} words found in the document!")
    
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



# this if block prevents the main() function from running when the script is imported into another Python file
if __name__ == "__main__":
    main()
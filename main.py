import sys
from stats import get_num_words, get_num_chars



def get_book_text(filepath):
    bookstring = filepath.read()
    return bookstring

def main():
    arguments = sys.argv
    if len(arguments) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    with open(arguments[1]) as f:
        bookstr = get_book_text(f)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {arguments[1]}...")
    print("----------- Word Count ----------")
    
    get_num_words(bookstr)

    print("----------- Character Count ----------")

    get_num_chars(bookstr)
    print("============= END ===============")

main()
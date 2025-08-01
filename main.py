from stats import get_number_of_words, get_character_count, sort_character_count
import sys

def get_book_text(filepath):
    contents = ""
    with open(filepath) as f:
        contents = f.read()
    return contents

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    frankenstein = get_book_text(book_path)
    num_words = get_number_of_words(frankenstein)
    num_chars = get_character_count(frankenstein)
    sorted_chars = sort_character_count(num_chars)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char_dict in sorted_chars:
        if not char_dict["char"].isalpha():
            continue
        print(f"{char_dict["char"]}: {char_dict["num"]}")
    print("============= END ===============")



main()
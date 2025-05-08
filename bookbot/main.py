import sys
from stats import number_of_words
from stats import number_of_characters
from stats import chars_dictionary_to_list_sorted

def get_book_text(path_to_file):
    file_content = ""
    with open(path_to_file) as f:
        file_content = f.read()
    return file_content

def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        path_to_file = sys.argv[1]
        words = number_of_words(get_book_text(path_to_file))
        characters = chars_dictionary_to_list_sorted(number_of_characters(get_book_text(path_to_file)))

        print("============ BOOKBOT ============")

        print("Analyzing book found at books/frankenstein.txt...")
        print("----------- Word Count ----------")
        print(f"Found {words} total words")

        print("---------- Character Count -------")
        for dict in characters:
            print(f"{dict["char"]}: {dict["num"]}")
            
        print("---------- END -------")

main()
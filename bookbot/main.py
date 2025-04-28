from stats import number_of_words

def get_book_text(path_to_file):
    file_content = ""
    with open(path_to_file) as f:
        file_content = f.read()
    return file_content

def main():
    print(f"{number_of_words(get_book_text("books/frankenstein.txt"))} words found in the document")

main()
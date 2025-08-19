from stats import get_num_words, count_characters, sort_characters
import sys

def get_book_text(filename):
    with open(filename, "r", encoding="utf-8") as f:
        text = f.read()
    return text

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file_path = sys.argv[1]
    string = get_book_text(file_path)
    characters = count_characters(string)
    sorted = sort_characters(characters)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}")
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(string)} total words")
    print("--------- Character Count -------")
    for item in sorted:
        if item['char'].isalpha():
            print(f"{item['char']}: {item['num']}")
if __name__ == "__main__":
    main()

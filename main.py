import sys
from stats import get_num_words, get_num_chars, sort_dict

def get_book_text(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def main():
    # check command line args
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    text = get_book_text(book_path)

    # word count
    num_words = get_num_words(text)

    # char counts
    num_chars = get_num_chars(text)
    sorted_dict = sort_dict(num_chars)

    # output
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(num_words)
    print("--------- Character Count -------")
    for item in sorted_dict:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

if __name__ == "__main__":
    main()

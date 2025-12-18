from stats import count_words, count_characters, format_book
import sys

def get_book_text(file_path):
    with open(file_path) as f:
        content = f.read()
    
    return content
    

def generate_report(book, url, items):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {url}...")
    print("----------- Word Count ----------")
    print(count_words(book))
    print("--------- Character Count -------")
    for item in items:
        if item["char"].isalpha():
            print(f"{item["char"]}: {item["num"]}")

    print("============= END ===============")


def main():
    if len(sys.argv) == 2:
        url = sys.argv[1]
        book = get_book_text(url)
        # print(book)
        #count_words(book)
        #print(count_characters(book))
        sorted_data = format_book(count_characters(book))
        generate_report(book, url, sorted_data)
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

main()
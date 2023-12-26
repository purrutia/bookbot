def main():
    book_name = "Frankenstein"
    book_path = "books/frankenstein.txt"
    make_report(book_path)


def count_words(book_content):
    book_words = book_content.split()
    return len(book_words)


def count_chars(book_content):
    book_content_lower = book_content.lower()
    char_count = {}
    for char in book_content_lower:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    return char_count


def get_book_content(book_path):
    with open(book_path) as f:
        return f.read()


def make_report(book_path):
    book_content = get_book_content(book_path)
    num_words = count_words(book_content)
    num_chars = count_chars(book_content)

    # Print report
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print("")

    chars = list(num_chars)
    chars.sort()
    for char in chars:
        if char.isalpha():
            print(f"The '{char}' character was found {num_chars[char]} times")
    print("--- End report ---")


main()

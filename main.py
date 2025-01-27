def main():

    book_path = "books/frankenstein.txt"
    text = read_book_text(book_path)

    print(f"Word count: {word_count(text)}")

    for each in count_characters(text):
        if each.isalpha():
            print(f"The '{each}' character was found {count_characters(text)[each]} times")

def read_book_text(path):
    with open(path) as f:
        return f.read()

def word_count(text):
    return len(text.split())

def count_characters(text):
    ch_count = {}
    for ch in text:
        ch_low = ch.lower()
        if ch_low not in ch_count:
            ch_count[ch_low] = 0
        ch_count[ch_low] += 1
    return ch_count

main()


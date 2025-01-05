import sys

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print(report(file_contents))

def word_count(text):
    return len(text.split())

def char_count(text):
    text = text.lower()

    char_dict = {}

    for char in text:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1

    return char_dict

def report(text):
    report_str = "--- Begin report of books/frankenstein.txt ---\n"

    words = word_count(text)
    report_str += f"{words} words found in the document\n\n"

    chars = char_count(text)

    letter_counts = {k: v for k, v in chars.items() if k.isalpha()}
    sorted_chars = sorted(letter_counts.items(), key=lambda x: x[1], reverse=True)

    for char, count in sorted_chars:
        report_str += f"The '{char}' character was found {count} times\n"

    report_str += "--- End report ---"
    return report_str

if __name__ == '__main__':
    sys.exit(main())

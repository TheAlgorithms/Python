# word_frequency_counter.py
# This program counts the frequency of each word in a paragraph of text.
# Author: jaimin45-art

def word_frequency(text: str):
    # Convert to lowercase and remove punctuation
    for ch in [',', '.', '?', '!', ';', ':']:
        text = text.replace(ch, '')
    words = text.lower().split()

    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1

    # Sort by frequency (descending) then alphabetically
    sorted_words = sorted(freq.items(), key=lambda x: (-x[1], x[0]))

    print("Word Frequency:\n")
    for word, count in sorted_words:
        print(f"{word} : {count}")

if __name__ == "__main__":
    print("Enter a paragraph of text:")
    paragraph = input()
    word_frequency(paragraph)

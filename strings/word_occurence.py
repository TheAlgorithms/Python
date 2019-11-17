# Created by sarathkaul on 17/11/19


from collections import defaultdict


def word_occurence(sentence: str) -> dict:
    occurence = defaultdict(int)

    sentence = sentence.split(" ")
    # Creating a dictionary containing count of each word
    for a_word in sentence:
        occurence[a_word] += 1
    return occurence


if __name__ == "__main__":
    count_dict = word_occurence("INPUT STRING")
    for word, count in count_dict.items():
        print(f"{word}: {count}")

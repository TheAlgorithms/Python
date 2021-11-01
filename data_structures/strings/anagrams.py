import collections
import os
import pprint
import time

start_time = time.time()
print("creating word list...")
path = os.path.split(os.path.realpath(__file__))
with open(path[0] + "/words.txt") as f:
    word_list = sorted(list({word.strip().lower() for word in f}))


def signature(word):
    return "".join(sorted(word))


word_bysig = collections.defaultdict(list)
for word in word_list:
    word_bysig[signature(word)].append(word)


def anagram(my_word):
    return word_bysig[signature(my_word)]


print("finding anagrams...")
all_anagrams = {word: anagram(word) for word in word_list if len(anagram(word)) > 1}

print("writing anagrams to file...")
with open("anagrams.txt", "w") as file:
    file.write("all_anagrams = ")
    file.write(pprint.pformat(all_anagrams))

total_time = round(time.time() - start_time, 2)
print(("Done [", total_time, "seconds ]"))

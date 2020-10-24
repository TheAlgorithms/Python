# Python program for insert and search
# operation in a Trie


class TrieNode:

    # Trie node class
    def __init__(self):
        self.children = [None]*26

        # isEndOfWord is True if node represent the end of the word
        self.isEndOfWord = False


class Trie:

    # Trie data structure class
    def __init__(self):
        self.root = self.getNode()

    def getNode(self):

        # Returns new trie node (initialized to NULLs)
        return TrieNode()

    def _charToIndex(self, ch):

        # private helper function
        # Converts key current character into index
        # use only 'a' through 'z' and lower case

        return ord(ch)-ord('a')

    def insert(self, key):

        # If not present, inserts key into trie
        # If the key is prefix of trie node,
        # just marks leaf node
        current = self.root
        for level in key:
            index = self._charToIndex(level)

            # if current character is not present
            if current.children[index] == None:
                current.children[index] = self.getNode()
            current = current.children[index]

        # mark last node as leaf
        current.isEndOfWord = True

    def search(self, key):

        # Search key in the trie
        # Returns true if key presents
        # in trie, else false
        current = self.root
        length = len(key)
        for level in range(length):
            index = self._charToIndex(key[level])
            if not current.children[index]:
                return False
            current = current.children[index]

        return current != None and current.isEndOfWord

    def display_content(self, root, s):
        if root == None:
            print(s)
            return
        if root.isEndOfWord:
            print(s)
        for i in range(26):
            if root.children[i]:
                self.display_content(root.children[i], s+chr(i+ord('a')))
    # T(n)=O(ALPHABET_SIZE * key_length * N) where N is number of keys in Trie
    # alphabet_size = 26 & key_length = average size

    def remove(self, string):
        ptr = self.root
        length = len(string)
        for idx in range(length):
            i = self._charToIndex(string[idx])
            if ptr.children[i] is not None:
                ptr = ptr.children[i]
            else:
                print("Keyword doesn't exist in trie")
        if ptr.isEndOfWord is not True:
            print("Keyword doesn't exist in trie")
        ptr.isEndOfWord = False
        return
    # T(n)= O(len(string)) and S(n)=O(1)


def main():

    # Input keys (use only 'a' through 'z' and lower case)
    keys = ["the", "a", "there", "anaswe", "any",
            "by", "their"]
    output = ["Not present in trie",
              "Present in trie"]

    # Trie object
    t = Trie()

    # Construct trie
    for key in keys:
        t.insert(key)

    # Search for different keys
    print("{} ---- {}".format("the", output[t.search("the")]))
    print("{} ---- {}".format("these", output[t.search("these")]))
    print("{} ---- {}".format("their", output[t.search("their")]))
    print("{} ---- {}".format("thaw", output[t.search("thaw")]))

    t.display_content(t.root, '')

    t.remove('bys')

    t.display_content(t.root, '')


if __name__ == '__main__':
    main()
# Insert and search costs O(key_length), however the memory requirements of Trie is O(ALPHABET_SIZE * key_length * N) where N is number of keys in Trie.
# alphabet_size=26
# key_length = average size

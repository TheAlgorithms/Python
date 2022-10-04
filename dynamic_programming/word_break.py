"""
Given a string s and a dictionary of strings wordDict,
return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Note: that the same word in the dictionary may be reused multiple times in the segmentation.

Examples

1. Input:- s= 'deepImpact' , wordDict = ['deep','Im','pact']
   Output:- True (Because deepImpact can be segregated into words mentioned in wordDict )
2. Input:- s= 'mangoinmango' , wordDict = ['mango','in','mango']
   Output:- True (Same word occurring twice )
3. Input:- s= 'deepfacts' , wordDict = ['deep','pact']
   Output:- False (Because pacts is not mentioned in wordDict )
"""


def wordBreak(s, word_dict):
    dict_set = set(word_dict)
    start = [0]
    # dp[0] is the equivalent of a base-case from the recursive solution and dp[-1] is the overall solution to the complete problem
    for i in range(len(s)):
        for j in start:
            if s[j : i + 1] in dict_set:
                start.append(i + 1)  # start of next word
                break  # - note [1]

    return start[-1] == len(s)


print(wordBreak("deepImpact", ["deep", "Im", "pact"]))
print(wordBreak("deepfacts", ["deep", "fact"]))
print(wordBreak("mangoinmango", ["mango", "in"]))

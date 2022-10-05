class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d= {} 
        for i in strs: 
            word = ''.join(sorted(i))
            if word not in d: 
                d[word]=[i]
            else: 
                d[word].extend([i])  
        return d.values()

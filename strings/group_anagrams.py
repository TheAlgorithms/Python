def signature(s: str) -> str:
  return ''.join(sorted(s))

def group_anagrams(words: List[str]) -> dict:
  anagrams = dict()
  for word in words:
    sign = signature(word)
    if sign not in anagrams:
      anagrams[sign] = []
    anagrams[sign].append(word)
  return anagrams

def remove_non_anagrams(anagrams: dict) -> dict:
  return {key: anagrams[key] for key in anagrams if len(anagrams[key]) > 1}

def isolate_anagrams(anagrams: dict) -> List[str]:
  return sorted([sorted(_) for _ in anagrams.values()])

data = ['could', 'cloud', 'areas', 'arena', 'artsy', 'grips', 'hello', 'parts', 'prigs', 'strap', 'traps']

print(isolate_anagrams(remove_non_anagrams(group_anagrams(data))))

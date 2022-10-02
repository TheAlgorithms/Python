from typing import List


def signature(word: str) -> str:
  """
  >>> signature("python")
  'hnopty'
  >>> signature("anagram")
  'aaagmnr'
  >>> signature("cloud")
  'cdlou'
  """
  return ''.join(sorted(word))

def group_anagrams(words: List[str]) -> dict:
  """
  >>> group_anagrams(['cloud', 'python', 'could'])
  {'cdlou': ['cloud', 'could'], 'hnopty': ['python']}
  >>> group_anagrams(['strap', 'traps', 'maps'])
  {'aprst': ['strap', 'traps'], 'amps': ['maps']}
  >>> group_anagrams(['astro', 'plastic', 'kite'])
  {'aorst': ['astro'], 'acilpst': ['plastic'], 'eikt': ['kite']}
  """
  anagrams = dict()
  for word in words:
    sign = signature(word)
    if sign not in anagrams:
      anagrams[sign] = []
    anagrams[sign].append(word)
  return anagrams

def remove_non_anagrams(anagrams: dict) -> dict:
  """
  >>> remove_non_anagrams({'cdlou': ['cloud', 'could'], 'hnopty': ['python']})
  {'cdlou': ['cloud', 'could']}
  >>> remove_non_anagrams({'aprst': ['strap', 'traps'], 'amps': ['maps']})
  {'aprst': ['strap', 'traps']}
  >>> remove_non_anagrams({'aorst': ['astro'], 'acilpst': ['plastic'], 'eikt': ['kite']})
  {}
  """
  return {key: anagrams[key] for key in anagrams if len(anagrams[key]) > 1}

def isolate_anagrams(anagrams: dict) -> List[str]:
  """
  >>> from grpAna import isolate_anagrams
  >>> isolate_anagrams({'cdlou': ['cloud', 'could']})
  [['cloud', 'could']]
  >>> isolate_anagrams({'aprst': ['strap', 'traps']})
  [['strap', 'traps']]
  >>> isolate_anagrams({})
  []
  """
  return sorted([sorted(_) for _ in anagrams.values()])


if __name__ == "__main__":
  data = ['could', 'cloud', 'areas', 'arena', 'artsy', 'grips', 'hello', 'parts', 'prigs', 'strap', 'traps']
  print(isolate_anagrams(remove_non_anagrams(group_anagrams(data))))

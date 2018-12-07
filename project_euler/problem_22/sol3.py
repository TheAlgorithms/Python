with open('p022_names.txt') as file:
	names = str(file.readlines()[0])
	names = names.replace('"', '').split(',')
names.sort()
answer = [ (index+1)*sum(map(lambda letter: ord(letter) -64, name)) for index, name in enumerate(names)  ]
assert answer == 871198282

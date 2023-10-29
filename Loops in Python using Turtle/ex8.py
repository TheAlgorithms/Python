story = '' # empty string
while 'the end' not in story:
    line = input('Enter a line: ')
    story += line + '\n'        # add line to story

print('Ye rahi kahani')
print(story)
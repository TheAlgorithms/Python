story = ''
while True:
    line = input('>>>')
    if not line:
        break
    story += line + '\n'

print('The new chapter of story')
print(story)
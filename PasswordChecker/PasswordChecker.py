import requests
import hashlib

string = input('Enter the password')
sha1pass = hashlib.sha1(string.encode('utf-8')).hexdigest().upper()
head, tail = sha1pass[:5],sha1pass[5:]

url = 'http://api.pwnedpasswords.com/range/' + head
res = requests.get(url)
hashes = (password.split(':') for password in res.text.splitlines())
for code, count in hashes:
    if code == tail:
        c = count
        break


print(f'This is used {count} times')
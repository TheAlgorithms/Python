import requests
import hashlib


def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'Error fetching: {res.status_code} check the API')
    return res


def get_password_leaks_count(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hash_to_check:
            return count
    return 0


def pwned_api_check(password):
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5_char, tail = sha1password[:5], sha1password[5:]
    response = request_api_data(first5_char)
    return get_password_leaks_count(response, tail)


def main(args):
    count = int(pwned_api_check(args))
    if count > 25:
        print(f'{args} was found {count} times.Your password is insecure.')
    else:
        print(f'{args} was found. Your password is secure...carry on!')


if __name__ == '__main__':
    while True:
        password = input('type "STOP" to exit\npassword: ')

        if password == 'STOP':
            break
        main(password)
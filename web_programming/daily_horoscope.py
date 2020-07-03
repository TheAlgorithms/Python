from bs4 import BeautifulSoup as bs
import requests

def horoscope():
    print('Your daily Horoscope. \n') 
    print('enter your Zodiac sign number:\n',
      '1. Aries\n','2. Taurus\n',
      '3. Gemini\n', '4. Cancer\n', 
      '5. Leo\n', '6. Virgo\n', 
      '7. Libra\n', '8. Scorpio\n', 
      '9. Sagittarius\n', '10. Capricorn\n', 
      '11. Aquarius\n', '12. Pisces\n') 
    
    z_sign = input('number> ')
    print('choose some day:\n', 'yesterday\n', 'today\n', 'tomorrow\n')
    day = input('enter the day> ')
    
    url = f'https://www.horoscope.com/us/horoscopes/general/horoscope-general-daily-{day}.aspx?sign={z_sign}'
    try: #exception handling for wrong day input
        soup = bs(requests.get(url).content, 'html.parser')
        s = soup.find('div', class_= 'main-horoscope')
        print('*' * 70)
        print(s.p.text) #horoscope text for chosen Zodiac sign
    except:
        print('it seems like you made a mistake in spelling the Day word. Please check your input and try again')

if __name__ == "__main__":
    horoscope()

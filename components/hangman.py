import requests # Для запроса на сайт
from bs4 import BeautifulSoup

url = 'https://ru.wikipedia.org/wiki/'
search = str(input())

url += search

HEADERS = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 OPR/68.0.3618.191'
    }

response = requests.get(url, headers = HEADERS)
soup = BeautifulSoup(response.content, features = 'html.parser')
text = soup.find('div', class_ = 'mw-parser-output').text

text = str(text)

text = text[0:10000]

text = text.lower()

text = text.replace('у́', 'у')
text = text.replace('а́', 'a')
text = text.replace('о́', 'o')
text = text.replace('и́', 'и')
text = text.replace('е́', 'е')

text = text.split()

i = 0 # определитель положения '—' в тесксте

while text[i] != '—':
    i += 1

check_word_1 = text[i - 1]
check_word_2 = text[i - 2]
check_word_3 = text[i - 3]

while t != text:
    if text[i - 1] == search or text[i - 2] == search or text[i - 3] == search: #самый простой случай

        print('прошло одну проверку')
        
        if check_word_1.find('(') != 0 or check_word_2.find('(') != 0 or check_word_3.find('(') != 0:

            text = ' '.join(text)
            print('прошло две проверки')

            if check_word_1.find(')') == True:
                text = text[i + 1:-1] #обрезание до '—'
    
                text = ' '.join(text)
                text = text[0:text.find('.') + 1] # обрезание до '.'

                t = text

                print(t)
                print(f'Это слово — {text}')
                print(check_word_1)
        
            else:
                text = text[i + 1:-1] #обрезание до '—'
        
        else:
            text = text[i + 1:-1] #обрезание до '—'
    
    else: 
        text = text[i + 1:-1] #обрезание до '—'

print(text)
import random
import json
import requests
from bs4 import BeautifulSoup


class Hangman:
    def __init__(self):
        self.word = self.__word_gen()
        self.word_lenght = len(self.word)
        self.template = "_" * self.word_lenght
        self.is_game = True
        self.life = 5
        self.attempts = 2

    @staticmethod
    def __word_gen():
        with open("assets/wordos.json") as js:
            data = json.load(js)
            random_word = random.choice(data['words'])

            return random_word

    @staticmethod
    def find(s, ch):
        return [i for i, ltr in enumerate(s) if ltr == ch]


    def chars_replace(self, char, indexs):
        temp = list(self.template)
        for i in indexs:
            temp[i] = char
        
        self.template = "".join(temp)


    def hangman_algorithm(self, char):
        if self.template != self.word:
            if self.is_game and self.life > 0:
                indexs = self.find(self.word, char)
                if len(indexs) != 0:
                    for _ in indexs:
                        self.chars_replace(char, indexs)

                    return f'Буква (Буквы) {char} есть в этом слове {self.template}'
                else:
                    self.life -= 1
                    return f'Буквы нет и у вас осталось {self.life} жизней. Вы можете испытать свою удачу /get_luck'

            return 'Вы допустили предельное количество ошибок, чтобы начать новую игру /game'
        
        else:
            return f'Вы угадали слово {self.word}'


    def tips(self):
        url = 'https://ru.wikipedia.org/wiki/'

        url += self.word

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
        text = text.replace('е́', 'е' )

        text = text.split()

        i = 0

        while text[i] != '—':
            i += 1

        if text[i - 1] == self.word or text[i - 2] == self.word or text[i - 3] == self.word:
            text = text[i + 1:-1]
            text = ' '.join(text)
            i = text.find('.')
            text = text[0:i]

        return text


class Minigame(Hangman):
    surprises = {
        0 : "Тебе повезло, мы добавили тебе еще одну жизнь", 
        1 : "Удача сыграла с тобой злую шутку и нам пришлось забрать у тебя еще одну жизнь",
        2 : "Ого, тебе очень повезло, ты можешь еще раз бросить кости :dame_die:",
        }

    def throw(self):
        luck_num = random.randint(0, 2)
        if self.attempts > 0:
            if luck_num == 0:
                self.life += 1
                self.attempts -= 1
                return self.surprises[luck_num]
            # elif luck_num == 1:
            #     self.recognize_letter()
            #     return self.surprises[luck_num]
            elif luck_num == 1:
                self.life -= 1
                self.attempts -= 1
                return self.surprises[luck_num]
            elif luck_num == 2:
                return self.surprises[luck_num]

    def foo(self):
        self.attempts -= 1




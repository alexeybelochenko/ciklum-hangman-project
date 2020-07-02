import random
import json



class Hangman:
    def __init__(self):
        self.word = self.__word_gen()
        self.word_lenght = len(self.word)
        self.template = "_" * self.word_lenght
        self.is_game = True
        self.life = 5

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
        if self.template != self.word
            if self.is_game and self.life > 0:
                indexs = self.find(self.word, char)
                if len(indexs) != 0:
                    for i in indexs:
                        self.chars_replace(char, indexs)

                    return f'Буква (Буквы) {char} есть в этом слове {self.template}'
                else:
                    self.life -= 1
                    return f'Буквы нет и у вас осталось {self.life} жизней'

            return 'Вы допустили предельное количество ошибок, чтобы начать новую игру /game'
        
        else:
            return f'Вы угадали слово {self.word}'
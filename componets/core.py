import random
import json



class Hangman:
    def __init__(self):
        self.word = self.__word_gen()
        self.word_lenght = len(word)
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

    @staticmethod
    def chars_replace(char, indexs):
        temp = list(self.template)
        for i in indexs:
            temp[i] = char
        
        string = "".join(temp)
        return string


    def hangman_algorithm(self, char):
        if self.is_game and self.life != 0 and self.template != self.word:
            indexs = find(default, str(char))
            if len(indexs) != 0:
                for i in indexs:
                    template = chars_replace(char, indexs)
            else:
                life -= 1
                return f'Буквы нет и у вас осталось {life} жизней'
        
        return 'Вы допустили предельное количество ошибок')
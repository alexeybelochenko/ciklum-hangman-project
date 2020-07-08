import random
import json

class Hangman:
    def __init__(self):
        self.word = self.__word_gen()
        self.word_lenght = len(self.word)
        self.template = "_" * self.word_lenght
        self.is_game = True
        self.attempts = 1
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
        if self.template != self.word:
            if self.is_game and self.life > 0:
                indexs = self.find(self.word, char)
                if len(indexs) != 0:
                    for i in indexs:
                        self.chars_replace(char, indexs)

                    return f'Буква (Буквы) {char} есть в этом слове {self.template}'
                else:
                    self.life -= 1
                    return f'Буквы нет и у вас осталось {self.life} жизней. Вы можете испытать свою удачу /get_luck_num'

            return 'Вы допустили предельное количество ошибок, чтобы начать новую игру /game'
        
        else:
            return f'Вы угадали слово {self.word}'



class Minigame(Hangman):
    def __init__(self, answer):
        self.surprises = {
            0 : "Тебе повезло, мы добавили тебе еще одну жизнь", 
            1 : "Тебе повезло и мы случайным образом отметили тебе букву", 
            2 : "Удача сыграла с тобой злую шутку и нам пришлось забрать у тебя еще одну жизнь",
            3 : "Ого, тебе очень повезло, ты можешь еще раз бросить кости :dame_die:",
            }

    def magic(self):
        luck_num = random.randint(0, 3)
        if self.attempts > 0:
            if luck_num == 0:
                self.life += 1
                self.attempts -= 1
                return self.surprises[luck_num]
            elif luck_num == 1:
                self.recognize_letter()
                return self.surprises[luck_num]
            elif luck_num == 2:
                self.life -= 1
                self.attempts -= 1
                return self.surprises[luck_num]
            elif luck_num == 3:
                return 

    def recognize_letter(self):
        pass
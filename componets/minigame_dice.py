import string
import random


class Minigame:
    def __init__(self, answer):
        self.status = answer
        self.attempts = 0
        self.surprises = {0 : "Тебе повезло, мы добавили тебе еще одну жизнь", 1 : "Тебе повезло и мы случайным образом отметили тебе букву", 2:"Удача сыграла с тобой злую шутку и нам пришлось забрать у тебя езе одну жизнь"}

while attempts != 2 :
    if self.status == 'д':
        luck = random.randint(0, 2)
        print(self.surprises[luck])
        # die1 = random.randint(1, 6)
        # die2 = random.randint(1, 6)
        # prise1 = random.randint(2, 12)
        # prise2 = random.randint(2, 12)
        # prise3 = random.randint(2, 12)
        question = input('Ты уверен ? [д/н]?\n' )
        attempts += 1
        print(die1, die2)
    else:
        print('Неверный ответ. Пожалуйста напечатай. "д" или "н".')
        attempts += 1
        question = input('Ты хочешь закончить ? [д/н]?\n' )        


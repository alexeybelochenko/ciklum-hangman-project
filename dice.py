import string
import random


attempts = 0
k = "Доп жизнь"
l = "Подсказка"
m = "Ещё попытка"

question = input('Привет, это мини-игра, кости. Бросаешь побеждаешь, тут можно выбить один из трёх призов. Хочешь бросить? [д/н]?\n')

while question != 'н' or attempts == 2:
    if question == 'д':
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        die3 = random.randint(2, 12)
        die4 = random.randint(2, 12)
        print(die1, die2)
        print(die3, die4)
        question = input('Ты хочешь ещё раз кости бросить? [д/н]?\n')
    else:
        print('Неверный ответ. Пожалуйста напечатай. "д" или "н".')
        question = input('Может опять ? [д/н]?\n')        
        print('Удачи!')

    if m == die3 and die1 and die2 == die3:
        attempts -=1
        print(f'Ты победил, ты вибил комбинацию {die3}, теперь продолжай кидать кубики.') 
    else:
        print('Ты не смог выбить комбинацию.')
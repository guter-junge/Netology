from random import choice

import telebot

token = '6249535829:AAH1y7pYsGb9-OZquPaaOWx2cL2MyBm-wBo'

bot = telebot.TeleBot(token)


RANDOM_TASKS = ['Написать Гвидо письмо', 'Выучить Python', 'Записаться на курс в Нетологию', 'Посмотреть 4 сезон Рик и Морти']

todos = dict()


HELP = '''
Список доступных команд:
* print  - напечать все задачи на заданную дату
* todo - добавить задачу
* random - добавить на сегодня случайную задачу
* help - Напечатать help
'''


def add_todo(date, description, category):
    date = date.lower()
    if todos.get(date) is not None:
        full_task = [description, category]
        todos[date].append(full_task)
    else:
        todos[date] = []
        full_task = [description, category]
        todos[date].append(full_task)


@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, HELP)


@bot.message_handler(commands=['random'])
def random(message):
    task = choice(RANDOM_TASKS)
    add_todo('сегодня', task)
    bot.send_message(message.chat.id, f'Задача {task} добавлена на сегодня')


@bot.message_handler(commands=['add'])
def add(message):
    _, date, tail = message.text.split(maxsplit=2)
    description, category = tail.split('@')
    description = ' '.join([description])
    add_todo(date, description, category)
    bot.send_message(message.chat.id, f'Задача {description}категории "@{category}" добавлена на дату {date}')


@bot.message_handler(commands=['show'])
def print_(message):
    date = message.text.split()[1].lower()
    if date in todos:
        tasks = ''
        for full_task in todos[date]:
            description = full_task[0]
            category = full_task[1]
            tasks += f'[ ] {description} @{category}\n'
    else:
        tasks = 'Такой даты нет'
    bot.send_message(message.chat.id, tasks)


bot.polling(none_stop=True)
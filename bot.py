import math, telebot, operations
from telebot import types, apihelper


def main():
    apihelper.proxy = {"https": "socks5h://127.0.0.1:9050",
                       "https": "socks5h://user42399:zeno9h@45.90.197.187:18943"}

    bot = telebot.TeleBot('')

    @bot.message_handler(commands=['start'])
    def start_message(message):
        bot.send_message(message.chat.id,
                         '/random - выведет вам целое или вещественное случайное число в заданном вами диапазоне\n'
                         '/calculator - примитивный калькулятор\n/help - помощь')
        markup = types.InlineKeyboardMarkup()
        inst = types.InlineKeyboardButton(text='мой', url='https://www.instagram.com/ketorg0z')
        markup.add(inst)
        bot.send_message(message.chat.id, 'Instagram', reply_markup=markup)
        markup = types.InlineKeyboardMarkup()
        inst = types.InlineKeyboardButton(text='мой', url='https://www.facebook.com/Ketorg0z')
        markup.add(inst)
        bot.send_message(message.chat.id, 'Facebook', reply_markup=markup)

    @bot.message_handler(commands=['random'])
    def send_text(message):
        keyboardrandom = types.InlineKeyboardMarkup()
        key_float = types.InlineKeyboardButton(text='Вещественное', callback_data='float')
        key_int = types.InlineKeyboardButton(text='Целое', callback_data='int')
        keyboardrandom.add(key_float)
        keyboardrandom.add(key_int)
        bot.send_message(message.from_user.id, 'Какое вам нужно число?', reply_markup=keyboardrandom)

    @bot.message_handler(commands=['calculator'])
    def calc(message):
        bot.send_message(message.chat.id, 'Введите число')
        bot.register_next_step_handler(message, get_num)

    def get_num(message):
        if "," in message.text:
            bot.send_message(message.chat.id, "Вещественные числа следует вводить с точкой.\nПопробуйте сначала.")
        else:
            global a
            a = float(message.text)
            keyboard = types.InlineKeyboardMarkup()
            key_plus = types.InlineKeyboardButton(text='+', callback_data='plus')
            key_minus = types.InlineKeyboardButton(text='-', callback_data='minus')
            key_divide = types.InlineKeyboardButton(text='/', callback_data='divide')
            key_multiply = types.InlineKeyboardButton(text='*', callback_data='multiply')
            key_sqrt = types.InlineKeyboardButton(text='sqrt', callback_data='sqrt')
            key_log = types.InlineKeyboardButton(text='log', callback_data='log')
            key_sin = types.InlineKeyboardButton(text='sin', callback_data='sin')
            key_cos = types.InlineKeyboardButton(text='cos', callback_data='cos')
            keyboard.row(key_plus, key_minus, key_multiply, key_divide)
            keyboard.row(key_sqrt, key_log, key_sin, key_cos)
            bot.send_message(message.from_user.id, text='Что будем с ним делать?', reply_markup=keyboard)

    @bot.callback_query_handler(func=lambda call: True)
    def callback_worker(call):
        global a
        if call.data == 'plus':
            bot.send_message(call.message.chat.id, 'С чем будем складывать?')
            bot.register_next_step_handler(call.message, plus)

        elif call.data == "minus":
            bot.send_message(call.message.chat.id, 'Что будем вычитать?')
            bot.register_next_step_handler(call.message, minus)

        elif call.data == 'divide':
            bot.send_message(call.message.chat.id, 'На что будем делить?')
            bot.register_next_step_handler(call.message, divide)

        elif call.data == 'multiply':
            bot.send_message(call.message.chat.id, 'На что будем умножать?')
            bot.register_next_step_handler(call.message, multiply)

        elif call.data == 'sqrt':
            bot.send_message(call.message.chat.id, 'Корень какой степени вы хотите извлечь?')
            bot.register_next_step_handler(call.message, sqrt)

        elif call.data == 'log':
            bot.send_message(call.message.chat.id, 'Какое основание будет у логарифма?')
            bot.register_next_step_handler(call.message, log)

        elif call.data == 'sin':
            a = math.radians(a)
            a = math.sin(a)
            bot.send_message(call.message.chat.id, str(a))

        elif call.data == 'cos':
            a = math.radians(a)
            a = math.cos(a)
            bot.send_message(call.message.chat.id, str(a))

        elif call.data == 'float':
            bot.send_message(call.message.chat.id,
                             'Введите нижний и верхний предел предел '
                             '(два вещественных числа (пример - 5.43), '
                             'через пробел)')
            bot.register_next_step_handler(call.message, get_lower_float)

        elif call.data == 'int':
            bot.send_message(call.message.chat.id, 'Введите нижний и верхний '
                                                   'предел предел (два целых числа, через пробел)')
            bot.register_next_step_handler(call.message, get_lower_int)
        else:
            help_tg(call.message)

    @bot.message_handler(commands=['help'])
    def help_tg(message):
        bot.send_message(message.chat.id,
                         '/random - выведет вам целое или вещественное '
                         'случайное число в заданном вами диапазоне\n'
                         '/calculator - примитивный калькулятор\n'
                         'Вещественные числа вводятся через точку.\n(Пример - 3.21)')

    def plus(message):
        bot.send_message(message.chat.id, operations.plus(a, message))

    def minus(message):
        bot.send_message(message.chat.id, operations.minus(a, message))

    def divide(message):
        bot.send_message(message.chat.id, operations.divide(a, message))

    def multiply(message):
        bot.send_message(message.chat.id, operations.multiply(a, message))

    def sqrt(message):
        bot.send_message(message.chat.id, operations.sqrt(a, message))

    def log(message):
        bot.send_message(message.chat.id, operations.log(a, message))

    def get_lower_float(message):
        if "," in message.text:
            bot.send_message(message.chat.id, "Вещественные числа следует вводить с точкой.\nПопробуйте сначала.")
        else:
            bot.send_message(message.chat.id, operations.get_lower_float(message))

    def get_lower_int(message):
        if "," in message.text:
            bot.send_message(message.chat.id, "Вещественные числа следует вводить с точкой.\nПопробуйте сначала.")
        else:
            bot.send_message(message.chat.id, operations.get_lower_int(message))

    bot.polling(none_stop=True)


if __name__ == '__main__':
    main()

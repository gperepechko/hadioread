import telebot
from keys import token
from telebot import types
from user import User
import pandas as pd

def main():
    global users
    users = dict()
    bot = telebot.TeleBot(token)

    # greeting message

    @bot.message_handler(commands=['start'])
    def start_message(message):
        bot.send_message(message.chat.id,"Hi! Guess whether my lyrics are written by Radiohead or a computer\n" +
        "Send me 'Begin' to start a new game. Send 'End' to stop.\n" +
        "If you want to play again, send me 'Begin' again.\n" +
        "Send me 'y' if you think the line was written by Radiohead, if not send 'n'. \n")
        
        global users
        users[message.chat.id] = User()
        print('User started the game')
        

    @bot.message_handler(content_types='text')
    def message_reply(message):
        global users
        try:
            user = users[message.chat.id]
        except KeyError:
            bot.send_message(message.chat.id,"To start the game send /start")
            print('User plays without /start') 
            return
        if message.text=="Begin" or message.text=="begin":
            users[message.chat.id] = User()
            user = users[message.chat.id]
            print(message.chat.id)
            user.load_dataset()
            bot.send_message(message.chat.id,"Game has started\n" + \
                            user.get_line())
            return
        
        if message.text=="y" or message.text=="Y":
            user = users[message.chat.id]
            user.add_answer(True)
            new_line = user.get_line()
            if new_line is None:
                bot.send_message(message.chat.id,"Game has finished\n" + \
                                "You guessed correctly in: " + str(user.get_score()) + '%')
                return
            bot.send_message(message.chat.id, user.get_line())
            return
        
        if message.text=="n" or message.text=="N":
            user = users[message.chat.id]
            user.add_answer(False)
            new_line = user.get_line()
            if new_line is None:
                bot.send_message(message.chat.id,"Game has finished\n" + \
                                "You guessed correctly in: " + str(user.get_score()) + '%')
                return
            bot.send_message(message.chat.id, user.get_line())
            return

        if message.text=="End" or message.text=="end":
            user = users[message.chat.id]
            bot.send_message(message.chat.id,"Game has stopped\n" + \
                                "You guessed correctly in: " + str(user.get_score()) + '%')
            return

        bot.send_message(message.chat.id,"I don't understand you. Send me 'y', 'n' or 'Begin' to start a new game. Send 'End' to stop.\n")

    bot.infinity_polling()

if __name__ == "__main__":
    main()

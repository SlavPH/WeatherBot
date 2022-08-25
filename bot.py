#!/usr/bin/env python3

# Libraries
import time
import json
import telebot
import requests

# Config
with open("config.py", "r") as file:
    config = file.read()
    exec(config)

# Define bot
bot = telebot.TeleBot(Token)

# Print running message
print("\033[1;32mBot in running now...\033[m\n\n")

# /start command
@bot.message_handler(commands=['start'])
def start_command(message):
    global Start
    user = message.from_user.first_name
    bot.send_chat_action(message.chat.id, "typing")
    bot.reply_to(message, Start.format(user))

# All messages
@bot.message_handler(func=lambda message: True)
def all_messages(message):

    city = message.text
    try:
        bot.send_chat_action(message.chat.id, "typing")
        msg1 = bot.reply_to(message, f"Getting information about {city}...")
        time.sleep(2)
        bot.edit_message_text(text=GetWeather(city), chat_id=message.chat.id, message_id=msg1.message_id)
                
    except Exception as e:
        print(e)
        bot.edit_message_text(text="Error: Could not get result!", chat_id=message.chat.id, message_id=msg1.message_id) 

bot.infinity_polling()
#SlavPH

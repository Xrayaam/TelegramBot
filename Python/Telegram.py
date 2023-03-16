import telebot
import yfinance as yf
import time
import random
from datetime import datetime as dt
TOKEN = '6055768297:AAGjwLnQLdyCieG1npFYStvDlnh3-3pS1mM'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_hello(message):
    chat_id = message.chat.id
    username = message.from_user.username
    bot.reply_to(message, f"👋 سلام @{username}! \n چطور میتونم کمکتون کنم؟")

@bot.message_handler(commands=['time'])
def getting_message_time(message):
    chat_id = message.chat.id
    b = 24 - dt.now().hour
    username = message.from_user.username
    bot.send_message(chat_id, text="⏰ " + dt.now().strftime('%I:%M %p \n') + f"---------------------------- \n{str(b)} ساعت مانده به 12 شب  ")

currency_ticker = "USDIRR=X"
@bot.message_handler(commands=['currency'])
def getting_message_time(message):
    chat_id = message.chat.id
    username = message.from_user.username
    data = yf.download(currency_ticker, period='1d')
    usd_price = data['Close'][-1]
    bot.send_message(chat_id, text=f"💰 قیمت دلار امروز : {usd_price:.0f} تومان")
    time.sleep(5)

@bot.message_handler(commands=['vpn'])
def getting_message_time(message):
    chat_id = message.chat.id
    username = message.from_user.username
    V2ray_code = ("vmess://eyJhZGQiOiJqb2luLWJlZGUudm1lc3NvcmcuZnVuIiwiYWlkIjoiMCIsImhvc3QiOiIiLCJpZCI6ImUxZTI2NGI2LWQ5YjUtNGE4Zi1mNDkwLTg2YjU4ZjU3YzQyMiIsIm5ldCI6IndzIiwicGF0aCI6Ii8iLCJwb3J0IjoiODAiLCJwcyI6IkB2MnJheW5nX29yZyIsInNjeSI6ImF1dG8iLCJzbmkiOiIiLCJ0bHMiOiIiLCJ0eXBlIjoiIiwidiI6IjIifQ==" , "vmess://eyJhZGQiOiIyMC4yMDUuMjE0LjY1IiwiYWlkIjoiMCIsImhvc3QiOiIiLCJpZCI6ImI4ZWMxNDAxLWU1YzEtNDI5OS1iMzE1LTk2OTRjY2EwYzJmOCIsIm5ldCI6IndzIiwicGF0aCI6Ii8iLCJwb3J0IjoiMzU4NDgiLCJwcyI6InYycmF5bmdfb3JnIiwic2N5IjoiYXV0byIsInNuaSI6IiIsInRscyI6IiIsInR5cGUiOiIiLCJ2IjoiMiJ9")
    bot.send_message(chat_id, '<code>' + str(random.choice(V2ray_code)) + '</code>', parse_mode='HTML')


bot.polling()



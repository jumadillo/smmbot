import telebot
import requests
import os

TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Assalomu alaykum! SMM xizmatlarimizga xush kelibsiz.")

bot.polling()

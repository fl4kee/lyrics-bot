import requests
import lxml.html
from lxml import etree
import telebot

TOKEN = '1792942070:AAHGl1s8KuVcwlmINi8EpvzxQdcgkHnrVwE'

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['help','start'])
def help_(message: telebot.types.Message):
    text = 'Привет! Это бот для поиска песен на английском.\n\
Формат ввода \'Группа - Песня\''
    bot.reply_to(message, text)

@bot.message_handler(content_types=['text'])
def show_lyrics(message: telebot.types.Message):
    try:
        artist, song = message.text.replace(' ','').lower().split('-')

        r = requests.get(f'https://www.azlyrics.com/lyrics/{artist}/{song}.html')
        if r.status_code == 200:
            html = r.content
            tree = lxml.html.document_fromstring(html)
            lyrics = tree.xpath('/html/body/div[2]/div/div[2]/div[5]/text()')

            text_1 = ''
            text_2 = ''
            for i in range(0, len(lyrics)//2):
                text_1 += lyrics[i].strip() + '\n'
            for i in range(len(lyrics)//2, len(lyrics)):
                text_2 += lyrics[i].strip() + '\n'

            bot.send_message(message.chat.id, text_1)

            bot.send_message(message.chat.id, text_2)


        else:
            bot.reply_to(message, 'Ничего не нашел. Возможно ты написал с ошибкой')
    except Exception as e:
        bot.reply_to(message, e)

bot.polling()


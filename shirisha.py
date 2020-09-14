!pip3 install adafruit.io
from Adafruit_IO import RequestError, Client, Feed
from Adafruit_IO import Data
username = "inmovidu"                   #change the username
code = "aio_qTPB77YrONiKtDxkYRq3BP4vdnh6"   #change the key
aio = Client(username,code)

!pip install python-telegram-bot
from telegram.ext import Updater,CommandHandler
import requests
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()
    url = contents['url']
    return url

def on(bot,update):
    url = get_url()
    chat_id = update.message.chat_id
    txt = 'light is turning on'
    pic = 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/5d/Green_sphere.svg/1024px-Green_sphere.svg.png'
    bot.send_message(chat_id,txt)
    bot.send_photo(chat_id,pic)
    value = Data(value=1)
    value_send = aio.create_data('lit',value)

def off(bot,update):
    url = get_url()
    chat_id = update.message.chat_id
    txt = 'light is turning off'
    pic = 'https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcTuueKIndqjMG0rlzPZrO0UUFP6ts8b_CrUIQ&usqp=CAU'
    bot.send_message(chat_id,txt)
    bot.send_photo(chat_id,pic)
    value = Data(value=0)
    value_send = aio.create_data('shirisha-a',value)

u = Updater('1373757776:AAEljYmvyeZ7Vstv6p4TquxEudB1qFV63os')  #change the token
dp = u.dispatcher
dp.add_handler(CommandHandler('on',on))
dp.add_handler(CommandHandler('off',off))
u.start_polling()
u.idle()


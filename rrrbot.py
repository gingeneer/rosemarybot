# -*- encoding: utf-8 -*-

import sys
import time
import pprint
import telepot
import urllib
from lxml import html
import json

def handle(msg):
	content_type, chat_type, chat_id = telepot.glance2(msg)
	
	chat_id = msg['chat']['id']
	command = msg['text']

	if '@' in command:
		command, botname = command.split('@')
	
	command = command.replace("/", "")
        
        if command == "start":
            bot.sendMessage(chat_id, "Send /rrr to see if the RRR summerbar is currently open.\nAlso don't slap pandas 🐼")

        if command.lower() == 'rrr':
            url = "https://afternoondelight.de/rrr/status"
            page = urllib.urlopen(url).read()
            data = json.loads(page)
            #print(data["status"])
            if data["status"] == "closed":
                bot.sendMessage(chat_id, "RRR is closed")
            elif data["status"] == "open":
                bot.sendMessage(chat_id, "RRR is open")
            else:
	        bot.sendMessage(chat_id, "something's wrong...")


TOKEN = ''

bot = telepot.Bot(TOKEN)
bot.notifyOnMessage(handle)
print 'running...'

# Keep the program running.
while 1:
    time.sleep(10)

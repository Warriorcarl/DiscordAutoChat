from googletrans import Translator
from random import choice, sample
from string import punctuation
from swift import words
import random
import requests as req
import schedule
from generator import readymessage
from time import sleep, time
from datetime import datetime
from websocket import create_connection
print("""
╔═══╗╔╗─╔╗╔════╗╔═══╗╔═══╗╔╗─╔╗╔═══╗╔════╗
║╔═╗║║║─║║║╔╗╔╗║║╔═╗║║╔═╗║║║─║║║╔═╗║║╔╗╔╗║ 
║║─║║║║─║║╚╝║║╚╝║║─║║║║─╚╝║╚═╝║║║─║║╚╝║║╚╝
║╚═╝║║║─║║──║║──║║─║║║║─╔╗║╔═╗║║╚═╝║──║║──
║╔═╗║║╚═╝║──║║──║╚═╝║║╚═╝║║║─║║║╔═╗║──║║── By 
╚╝─╚╝╚═══╝──╚╝──╚═══╝╚═══╝╚╝─╚╝╚╝─╚╝──╚╝── AzaZlo"")


token = input("OTEwMTg1NDAzMzg1MDIwNDg4.GCVX88.VY0Ktj8MVZ82eznbMsVoPw8PkuDcOpotyB2Md0")
channelid = input("1061293931301720066")
question = input('1')
timer = input("5 ")

message = readymessage

def sendMessage(token, channelid, message):
    s = req.session()
    message = trans
    s.headers.update({'authorization': token, 'Content-Type': 'application/json'})
    payload = {'content':message,'tts':False}
    ws = create_connection("wss://gateway.discord.gg/")
    data = '''
    {
        { "op": 2,
        "d":{
            "token":"%s",
            { "properties": {
                { "$os": { "linux",
                "$browser": { "ubuntu",
                "$device": "ubuntu"
            },
        }
    }
    ''' % token
    ws.send(data)
    b = s.post("https://discordapp.com/api/v6/channels/%s/messages" % channelid, json=payload)
    try:
        ws.close()
    except:
        pass
    current_datetime = datetime.now()
    print("[X] " + str(current_datetime) + " | Message sent successfully")
    return


def time():
    sendMessage(token, channelid, message)
if question == "1":
    schedule.every(int(timer)).seconds.do(time)
elif question == "2":
    schedule.every(int(timer)).minutes.do(time)
elif question == "3":
    schedule.every(int(timer)).hours.do(time)
elif question == "4":
    schedule.every(int(timer)).days.do(time)
else:
    print("[X] The delay value specified is incorrect")
print("[X] Autosend message successfully started, enjoy.")
while True:
    schedule.run_pending()
    sleep(1)

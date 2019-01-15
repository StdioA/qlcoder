# coding: utf-8

import time
from datetime import datetime
import hashlib
import pytz
import requests
import multiprocessing.dummy as mp
from tgbot import TgBot

t = "20160426StdioA{time}{num}"
# t = "{date}StdioA{time}{num}"
url = "http://www.qlcoder.com/train/handsomerank?_token=CkBMVl32hhJ9I6bFC8XXT2TaOixStwb6FNXSknDe&user=StdioA&checkcode={code}"
vote = 800 
num = 0
# tz = pytz.timezone("Asia/Shanghai")
bot = TgBot("70292863:AAEzdiMxmhzT52xYsL6L8FbPi20lXU6WEpc")

def calc():
    global vote, num
    # date = datetime.fromtimestamp(time.time(), tz).strftime("%Y%m%d")
    while True:
        a = hashlib.md5()
        code = t.format(time=str(vote), num=str(num))
        a.update(code)
        if a.hexdigest()[0:6] == "000000":
            print [num, vote, a.hexdigest()]
            vote += 1
                # hr = requests.get(url.format(code=num), timeout=5)
            bot.send_message(90625935, ' '.join([num, vote, a.hexdigest()]))
            num = 0
        else:
            num += 1

    


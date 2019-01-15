# coding: utf-8

import time
from datetime import datetime
import hashlib
import pytz
import requests


t = "20160426StdioA{vote}{num}"
url = "http://www.qlcoder.com/train/handsomerank?_token=CkBMVl32hhJ9I6bFC8XXT2TaOixStwb6FNXSknDe&user=StdioA&checkcode={code}"
vote = 965
num = 0
# tz = pytz.timezone("Asia/Shanghai")
# date = datetime.fromtimestamp(time.time(), tz).strftime("%Y%m%d")

# t = t.format(date)

def calc():
    global vote, num
    while True:
        a = hashlib.md5()
        code = t.format(vote=str(vote), num=str(num))
        a.update(code)
        if a.hexdigest()[0:6] == "000000":
            print num, vote, a.hexdigest()
            vote += 1
            # hr = requests.get(url.format(code=num))
            num = 0
        else:
            num += 1

calc()

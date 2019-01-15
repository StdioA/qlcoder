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
vote = 965 
num = 0

f = file("hashes.txt", "r")
for line in f:
    code = line.split()[0]
    requests.get(url.format(code=code))
    print line.split()[1]
f.close()


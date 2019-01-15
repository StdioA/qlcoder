#!/usr/bin/env python
# coding: utf-8

import requests
import ConfigParser        

class RemoteServerException(Exception):                                     # TODO: 考虑将状态码在本类中进行处理
    def __init__(self, status_code):
        super(RemoteServerException, self).__init__()
        if len(self.args) == 2:
            self.code, self.reason = self.args
        else:
            self.code = status_code

    def __str__(self):
        if len(self.args) == 2:
            code, reason = self.args
            return "{code}, {reason}".format(code=code, reason=reason)
        elif self.args:
            return self.args[0]


class ActionIsNotAcceptable(Exception):
    def __str__(self):
        return self.args[0], "is not acceptable."


class TgBot(object):
    """\
    The Telegram bot
    See more at https://core.telegram.org/bots/api
    """
    offset = 0
    url = "https://api.telegram.org/bot{token}/{method}"

    def __init__(self, token=None, confname="./config.cfg", checkvalid=False):
        if isinstance(token, str):                              # 读取bot token
            self.token = token

        if isinstance(confname, str):
            self.confname = confname

        conf = ConfigParser.ConfigParser()
        conf.read(confname)
        self.offset = int(conf.get("tgbot", "offset"))
        if token is None:
            self.token = conf.get("tgbot", "token")

        self.url = self.url.format(token=self.token, method="{method}")
        if checkvalid:
            self.test()

    def test(self):
        """\
        The test function
        test() => None
        """
        try:
            self.get_me()
        except RemoteServerException, exc:
            if exc.args[0] == 401:
                print "Token unauthorized, please check your bot token."
                return
            else:
                raise

    def get_me(self):
        """\
        get_me() => dict
        Function getMe, returns basic information about the bot in the form of User object.
        Return: a dict represented to the response text.
        """
        hr = requests.post(self.url.format(method="getMe"))
        if hr.status_code == 200:
            return hr.json()
        else:
            raise RemoteServerException(hr.status_code)

    def send_message(self, chat_id, text, **kwargs):
        """\
        send_message() => dict
        Function sendMessage
        """

        if not isinstance(chat_id, (int, str, unicode)):
            raise TypeError("Parameter chat_id should be a integer or a string")
        elif not isinstance(text, unicode):
            text = unicode(text)
            
        kwargs['chat_id'] = chat_id
        kwargs['text'] = text
        hr = requests.post(self.url.format(method="sendMessage"), params=kwargs)

        if hr.status_code == 200:
            return hr.json()
        elif hr.status_code == 400:
            raise RemoteServerException(hr.status_code, "The chat id doesn't exist")
        else:
            raise RemoteServerException(hr.status_code)

    def forward_message(self, chat_id, from_chat_id, message_id):
        """\
        forward_message() => dict
        Function forwardMessage
        """

        if not isinstance(chat_id, (int, str, unicode)):
            raise TypeError("Parameter chat_id should be a integer or a string")
        if not isinstance(from_chat_id, (int, str, unicode)):
            raise TypeError("Parameter from_chat_id should be a integer or a string")
        elif not isinstance(message_id, (int, str, unicode)):
            raise TypeError("Parameter message_id should be a integer or a string")

        kwargs = {"chat_id": chat_id,
                  "from_chat_id": from_chat_id,
                  "message_id": message_id
                  }
        hr = requests.post(self.url.format(method="forwardMessage"), params=kwargs)

        if hr.status_code == 200:
            return hr.json()
        elif hr.status_code == 400:
            raise RemoteServerException(hr.status_code, "The params aren't valid")
        else:
            raise RemoteServerException(hr.status_code)

    def send_chat_action(self, chat_id, action="typing"):
        """\
        send_chat_action => None
        """
        actions = ["typing", "upload_photo", "record_video", "upload_video",
                    "record_audio", "upload_audio", "upload_document", "find_location"]
        if action not in actions:
            raise ActionIsNotAcceptable(action)

        kwargs = {"chat_id": chat_id, "action": action}
        hr = requests.post(self.url.format(method="sendChatAction"), params=kwargs)

        if hr.status_code == 200:
            return hr.json()
        else:
            raise RemoteServerException(hr.status_code)

    def get_updates(self, offset=None, limit=0, timeout=0):
        """\
        get_updates() => dict
        Function getUpdates
        """
        if not offset:
            offset = self.offset

        kwargs = {"offset": offset}
        hr = requests.post(self.url.format(method="getUpdates"), params=kwargs)

        if hr.status_code == 200:
            result = hr.json()
            if result["result"]:
                self.offset = result["result"][-1]["update_id"]+1
            return result
        else:
            raise RemoteServerException(hr.status_code)

    def __del__(self):
        conf = ConfigParser.ConfigParser()

        conf.read(self.confname)
        conf.set("tgbot", "offset", self.offset)
        conf.write(open("./config.cfg", "w"))

if __name__ == '__main__':
    bot = TgBot("<Your-Telegram-bot-token>")
    bot.test()

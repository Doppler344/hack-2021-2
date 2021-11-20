class Bot:
    def send_message(self,destination,message):
        smsc = SMSC()
        smsc.send_sms("7" + destination, message, sender="sms")


try:
    from urllib import urlopen, quote
except ImportError:
    from urllib.request import urlopen
    from urllib.parse import quote

SMSC_LOGIN = ""  # логин клиента
SMSC_PASSWORD = ""  # пароль
SMSC_POST = False  # использовать метод POST
SMSC_HTTPS = False  # использовать HTTPS протокол
SMSC_CHARSET = "utf-8"  # кодировка сообщения (windows-1251 или koi8-r), по умолчанию используется utf-8
SMSC_DEBUG = False  # флаг отладки

# Константы для отправки SMS по SMTP
SMTP_FROM = "api@smsc.ru"  # e-mail адрес отправителя
SMTP_SERVER = "send.smsc.ru"  # адрес smtp сервера
SMTP_LOGIN = ""  # логин для smtp сервера
SMTP_PASSWORD = ""  # пароль для smtp сервера


def ifs(cond, val1, val2):
    if cond:
        return val1
    return val2


class SMSC(object):

    def send_sms(self, phones, message, translit=0, time="", id=0, format=0, sender=False, query=""):
        formats = ["flash=1", "push=1", "hlr=1", "bin=1", "bin=2", "ping=1", "mms=1", "mail=1", "call=1", "viber=1",
                   "soc=1"]

        m = self._smsc_send_cmd("send", "cost=3&phones=" + quote(phones) + "&mes=" + quote(message) + \
                                "&translit=" + str(translit) + "&id=" + str(id) + ifs(format > 0,
                                                                                      "&" + formats[format - 1], "") + \
                                ifs(sender == False, "", "&sender=" + quote(str(sender))) + \
                                ifs(time, "&time=" + quote(time), "") + ifs(query, "&" + query, ""))

        # (id, cnt, cost, balance) или (id, -error)

        if SMSC_DEBUG:
            if m[1] > "0":
                print("Сообщение отправлено успешно. ID: " + m[0] + ", всего SMS: " + m[1] + ", стоимость: " + m[
                    2] + ", баланс: " + m[3])
            else:
                print("Ошибка №" + m[1][1:] + ifs(m[0] > "0", ", ID: " + m[0], ""))

        return m

    def _smsc_send_cmd(self, cmd, arg=""):
        url = ifs(SMSC_HTTPS, "https", "http") + "://smsc.ru/sys/" + cmd + ".php"
        _url = url
        arg = "login=" + quote(SMSC_LOGIN) + "&psw=" + quote(
            SMSC_PASSWORD) + "&fmt=1&charset=" + SMSC_CHARSET + "&" + arg

        i = 0
        ret = ""

        while ret == "" and i <= 5:
            if i > 0:
                url = _url.replace("smsc.ru/", "www" + str(i) + ".smsc.ru/")
            else:
                i += 1

            try:
                if SMSC_POST or len(arg) > 2000:
                    data = urlopen(url, arg.encode(SMSC_CHARSET))
                else:
                    data = urlopen(url + "?" + arg)

                ret = str(data.read().decode(SMSC_CHARSET))
            except:
                ret = ""

            i += 1

        if ret == "":
            if SMSC_DEBUG:
                print("Ошибка чтения адреса: " + url)
            ret = ","  # фиктивный ответ

        return ret.split(",")

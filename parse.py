import requests
from bs4 import BeautifulSoup
from datetime import datetime
from time import sleep
import bot

def getHtml(nickname):
    html = requests.get(f"https://vk.com/{nickname}").text
    with open("index.html", "w") as f:
        f.write(html)
    print(f"Страница обновлена ({datetime.now().replace(microsecond=0)})")

def getData(nickname):
    getHtml(nickname)
    with open("index.html", "r") as f:
        html = f.read()
    soup = BeautifulSoup(html, "lxml")
    name = soup.find(class_="op_header").text.strip()
    status = soup.find(class_="pp_last_activity_text").text.strip()
    return name, status

def process(nickname):
    try:
        name, status = getData(nickname)
    except AttributeError:
        bot.sendMessage("Ошибка! Введён неверный никнейм или у пользователя закрытый аккаунт")
        return None
    if status.lower() == "online":
        statusFlag = True
        bot.sendMessage(f"Пользователь {name} сейчас онлайн, я скажу, когда он(-а) будет оффлайн")
    else:
        statusFlag = False
        bot.sendMessage(f"Пользователь {name} {status}, я скажу, когда он(-а) будет онлайн")

    while True:
        name, status = getData(nickname)
        if statusFlag and status.lower() != "online":
            statusFlag = False
            print(f"Пользователь {name} сейчас оффлайн")
        if not statusFlag and status.lower() == "online":
            statusFlag = True
            print(f"Пользователь {name} сейчас онлайн")
        sleep(30)

def main(nickname):
    process(nickname)
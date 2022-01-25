from random import randint

import config
import texts
import logging
import datetime
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from config import TOKEN


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    """     Starting program
            :param message: command 'start'
            :type message: aiogram.types.message.Message
            :rtype: None

    """
    await message.reply(texts.Info)


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    """     Help users how to use bot

            :param message: command 'help'
            :type message: aiogram.types.message.Message
            :rtype: None

    """
    await message.reply("Напишите /start для начала работы")

async def comp(hum1, hum2, message) -> int:
    """compares people and displays their compatibility

    :param hum1: first person's data
    :type hum1: tuple(str, str, str)
    :param hum2: second person's data
    :type hum2: tuple(str, str, str)
    :param message: message object from aiogram
    :type message: aiogram.types.message.Message

    :rtype: None
    :return: None

    """

    S = 0
    if {hum1[1], hum2[1]} == {"Air", "Aqu"}:
        S += 90
        await message.answer(texts.AirAqu)
        if {hum1[0], hum2[0]} == {"Aqr", "Psc"}:
            S += 50
            await message.answer("Водолей и Рыбы")
        elif {hum1[0], hum2[0]} == {"Aqr", "Sco"}:
            S += 100
            await message.answer("Водолей и Скорпион")
        elif {hum1[0], hum2[0]} == {"Aqr", "Cnc"}:
            S += 95
            await message.answer("Водолей и Рак")
        elif {hum1[0], hum2[0]} == {"Gem", "Psc"}:
            S += 80
            await message.answer("Близнецы и Рыбы")
        elif {hum1[0], hum2[0]} == {"Gem", "Sco"}:
            S += 63
            await message.answer("Близнецы и Скорпион")
        elif {hum1[0], hum2[0]} == {"Gem", "Cnc"}:
            S += 85
            await message.answer("Близнецы и Рак")
        elif {hum1[0], hum2[0]} == {"Lib", "Psc"}:
            S += 55
            await message.answer("Весы и Рыбы")
        elif {hum1[0], hum2[0]} == {"Lib", "Sco"}:
            S += 87
            await message.answer("Весы и Скорпион")
        elif {hum1[0], hum2[0]} == {"Lib", "Cnc"}:
            S += 70
            await message.answer("Весы и Рак")

    elif {hum1[1], hum2[1]} == {"Air", "Ign"}:
        S += 90
        await message.answer(texts.AirIgn)
        if {hum1[0], hum2[0]} == {"Aqr", "Leo"}:
            S += 20
            await message.answer("Водолей и Лев")
        elif {hum1[0], hum2[0]} == {"Aqr", "Ari"}:
            S += 60
            await message.answer("Водолей и Овен")
        elif {hum1[0], hum2[0]} == {"Aqr", "Sgr"}:
            S += 75
            await message.answer("Водолей и Стрелец")
        elif {hum1[0], hum2[0]} == {"Gem", "Leo"}:
            S += 50
            await message.answer("Близнецы и Лев")
        elif {hum1[0], hum2[0]} == {"Gem", "Ari"}:
            S += 100
            await message.answer("Близнецы и Овен")
        elif {hum1[0], hum2[0]} == {"Gem", "Sgr"}:
            S += 95
            await message.answer("Близнецы и Стрелец")
        elif {hum1[0], hum2[0]} == {"Lib", "Leo"}:
            S += 40
            await message.answer("Весы и Лев")
        elif {hum1[0], hum2[0]} == {"Lib", "Ari"}:
            S += 64
            await message.answer("Весы и Овен")
        elif {hum1[0], hum2[0]} == {"Lib", "Sgr"}:
            S += 50
            await message.answer("Весы и Стрелец")

    elif {hum1[1], hum2[1]} == {"Aqu", "Ign"}:
        S += 40
        await message.answer(texts.AquIgn)
        if {hum1[0], hum2[0]} == {"Psc", "Leo"}:
            S += 83
            await message.answer("Рыбы и Лев")
        elif {hum1[0], hum2[0]} == {"Psc", "Ari"}:
            S += 60
            await message.answer("Рыбы и Овен")
        elif {hum1[0], hum2[0]} == {"Psc", "Sgr"}:
            S += 71
            await message.answer("Рыбы и Стрелец")
        elif {hum1[0], hum2[0]} == {"Sco", "Leo"}:
            S += 25
            await message.answer("Скорпион и Лев")
        elif {hum1[0], hum2[0]} == {"Sco", "Ari"}:
            S += 82
            await message.answer("Скорпион и Овен")
        elif {hum1[0], hum2[0]} == {"Sco", "Sgr"}:
            S += 75
            await message.answer("Скорпион и Стрелец")
        elif {hum1[0], hum2[0]} == {"Cnc", "Leo"}:
            S += 35
            await message.answer("Рак и Лев")
        elif {hum1[0], hum2[0]} == {"Cnc", "Ari"}:
            S += 68
            await message.answer("Рак и Овен")
        elif {hum1[0], hum2[0]} == {"Cnc", "Sgr"}:
            S += 30
            await message.answer("Рак и Стрелец")

    elif {hum1[1], hum2[1]} == {"Air", "Ter"}:
        S += 40
        await message.answer(texts.AirTer)
        if {hum1[0], hum2[0]} == {"Aqr", "Tau"}:
            S += 70
            await message.answer("Водолей и Телец")
        elif {hum1[0], hum2[0]} == {"Aqr", "Cap"}:
            S += 62
            await message.answer("Водолей и Козерог")
        elif {hum1[0], hum2[0]} == {"Aqr", "Vir"}:
            S += 50
            await message.answer("Водолей и Дева")
        elif {hum1[0], hum2[0]} == {"Gem", "Tau"}:
            S += 27
            await message.answer("Близнецы и Телец")
        elif {hum1[0], hum2[0]} == {"Gem", "Cap"}:
            S += 80
            await message.answer("Близнецы и Козерог")
        elif {hum1[0], hum2[0]} == {"Gem", "Vir"}:
            S += 65
            await message.answer("Близнецы и Дева")
        elif {hum1[0], hum2[0]} == {"Lib", "Tau"}:
            S += 89
            await message.answer("Весы и Телец")
        elif {hum1[0], hum2[0]} == {"Lib", "Cap"}:
            S += 76
            await message.answer("Весы и Козерог")
        elif {hum1[0], hum2[0]} == {"Lib", "Vir"}:
            S += 49
            await message.answer("Весы и Дева")

    elif {hum1[1], hum2[1]} == {"Air"}:
        S += 80
        await message.answer(texts.AirAir)
        if {hum1[0], hum2[0]} == {"Aqr", "Aqr"}:
            S += 20
            await message.answer("Водолей и Водолей")
        elif {hum1[0], hum2[0]} == {"Aqr", "Gem"}:
            S += 40
            await message.answer("Водолей и Близнецы")
        elif {hum1[0], hum2[0]} == {"Aqr", "Lib"}:
            S += 100
            await message.answer("Водолей и Весы")
        elif {hum1[0], hum2[0]} == {"Lib", "Gem"}:
            S += 55
            await message.answer("Весы и Близнецы")
        elif {hum1[0], hum2[0]} == {"Lib", "Lib"}:
            S += 35
            await message.answer("Весы и Весы")
        elif {hum1[0], hum2[0]} == {"Gem", "Gem"}:
            S += 75
            await message.answer("Близнецы и Близнецы")

    elif {hum1[1], hum2[1]} == {"Aqu", "Ter"}:
        S += 85
        await message.answer(texts.AquTer)
        if {hum1[0], hum2[0]} == {"Psc", "Tau"}:
            S += 100
            await message.answer("Рыбы и Телец")
        elif {hum1[0], hum2[0]} == {"Psc", "Cap"}:
            S += 85
            await message.answer("Рыбы и Козерог")
        elif {hum1[0], hum2[0]} == {"Psc", "Vir"}:
            S += 88
            await message.answer("Рыбы и Дева")
        elif {hum1[0], hum2[0]} == {"Sco", "Tau"}:
            S += 40
            await message.answer("Скорпион и Телец")
        elif {hum1[0], hum2[0]} == {"Sco", "Cap"}:
            S += 99
            await message.answer("Скорпион и Козерог")
        elif {hum1[0], hum2[0]} == {"Sco", "Vir"}:
            S += 70
            await message.answer("Скорпион и Дева")
        elif {hum1[0], hum2[0]} == {"Cnc", "Tau"}:
            S += 60
            await message.answer("Рак и Телец")
        elif {hum1[0], hum2[0]} == {"Cnc", "Cap"}:
            S += 52
            await message.answer("Рак и Козерог")
        elif {hum1[0], hum2[0]} == {"Cnc", "Vir"}:
            S += 74
            await message.answer("Рак и Дева")

    elif {hum1[1], hum2[1]} == {"Aqu"}:
        S += 85
        await message.answer(texts.AquAqu)
        if {hum1[0], hum2[0]} == {"Psc", "Psc"}:
            S += 55
            await message.answer("Рыбы и Рыбы")
        elif {hum1[0], hum2[0]} == {"Psc", "Sco"}:
            S += 88
            await message.answer("Рыбы и Скорпион")
        elif {hum1[0], hum2[0]} == {"Psc", "Cnc"}:
            S += 12
            await message.answer("Рыбы и Рак")
        elif {hum1[0], hum2[0]} == {"Sco", "Sco"}:
            S += 89
            await message.answer("Скорпион и Скорпион")
        elif {hum1[0], hum2[0]} == {"Sco", "Cnc"}:
            S += 60
            await message.answer("Скорпион и Рак")
        elif {hum1[0], hum2[0]} == {"Cnc", "Cnc"}:
            S += 70
            await message.answer("Рак и Рак")

    elif {hum1[1], hum2[1]} == {"Ign", "Ter"}:
        S += 30
        await message.answer(texts.IgnTer)
        if {hum1[0], hum2[0]} == {"Leo", "Tau"}:
            S += 60
            await message.answer("Лев и Телец")
        elif {hum1[0], hum2[0]} == {"Leo", "Cap"}:
            S += 45
            await message.answer("Лев и Козерог")
        elif {hum1[0], hum2[0]} == {"Leo", "Vir"}:
            S += 12
            await message.answer("Лев и Дева")
        elif {hum1[0], hum2[0]} == {"Ari", "Tau"}:
            S += 20
            await message.answer("Овен и Телец")
        elif {hum1[0], hum2[0]} == {"Ari", "Cap"}:
            S += 100
            await message.answer("Овен и Козерог")
        elif {hum1[0], hum2[0]} == {"Ari", "Vir"}:
            S += 56
            await message.answer("Овен и Дева")
        elif {hum1[0], hum2[0]} == {"Sgr", "Tau"}:
            S += 80
            await message.answer("Стрелец и Телец")
        elif {hum1[0], hum2[0]} == {"Sgr", "Cap"}:
            S += 95
            await message.answer("Стрелец и Козерог")
        elif {hum1[0], hum2[0]} == {"Sgr", "Vir"}:
            S += 58
            await message.answer("Стрелец и Дева")

    elif {hum1[1], hum2[1]} == {"Ign"}:
        S += 90
        await message.answer(texts.IgnIgn)
        if {hum1[0], hum2[0]} == {"Leo", "Leo"}:
            S += 47
            await message.answer("Лев и Лев")
        elif {hum1[0], hum2[0]} == {"Leo", "Ari"}:
            S += 75
            await message.answer("Лев и Овен")
        elif {hum1[0], hum2[0]} == {"Leo", "Sgr"}:
            S += 37
            await message.answer("Лев и Стрелец")
        elif {hum1[0], hum2[0]} == {"Ari", "Ari"}:
            S += 87
            await message.answer("Овен и Овен")
        elif {hum1[0], hum2[0]} == {"Ari", "Sgr"}:
            S += 82
            await message.answer("Овен и Стрелец")
        elif {hum1[0], hum2[0]} == {"Sgr", "Sgr"}:
            S += 80
            await message.answer("Стрелец и Стрелец")

    elif {hum1[1], hum2[1]} == {"Ter"}:
        S += 85
        await message.answer(texts.TerTer)
        if {hum1[0], hum2[0]} == {"Tau", "Tau"}:
            S += 80
            await message.answer("Телец и Телец")
        elif {hum1[0], hum2[0]} == {"Tau", "Cap"}:
            S += 65
            await message.answer("Телец и Козерог")
        elif {hum1[0], hum2[0]} == {"Tau", "Vir"}:
            S += 38
            await message.answer("Телец и Дева")
        elif {hum1[0], hum2[0]} == {"Cap", "Cap"}:
            S += 60
            await message.answer("Козерог и Козерог")
        elif {hum1[0], hum2[0]} == {"Cap", "Vir"}:
            S += 30
            await message.answer("Козерог и Дева")
        elif {hum1[0], hum2[0]} == {"Vir", "Vir"}:
            S += 75
            await message.answer("Дева и Дева")

    S += randint(0, 100)
    await message.answer("{} и {}, Ваша совместимость: {}%".format(hum1[2], hum2[2], S // 3))
    return S

def searc(date, name) -> tuple:
    y = date[2]
    date = datetime.date(y, date[1], date[0])
    if datetime.date(y, 3, 21) <= date <= datetime.date(y, 4, 20):
        return "Ari", "Ign", name
    elif datetime.date(y, 4, 21) <= date <= datetime.date(y, 5, 21):
        return "Tau", "Ter", name
    elif datetime.date(y, 5, 22) <= date <= datetime.date(y, 6, 21):
        return "Gem", "Air", name
    elif datetime.date(y, 6, 22) <= date <= datetime.date(y, 7, 22):
        return "Cnc", "Aqu", name
    elif datetime.date(y, 7, 23) <= date <= datetime.date(y, 8, 21):
        return "Leo", "Ign", name
    elif datetime.date(y, 8, 22) <= date <= datetime.date(y, 9, 23):
        return "Vir", "Ter", name
    elif datetime.date(y, 9, 24) <= date <= datetime.date(y, 10, 23):
        return "Lib", "Air", name
    elif datetime.date(y, 10, 24) <= date <= datetime.date(y, 11, 22):
        return "Sco", "Aqu", name
    elif datetime.date(y, 11, 23) <= date <= datetime.date(y, 12, 22):
        return "Sgr", "Ign", name
    elif datetime.date(y, 12, 23) <= date <= datetime.date(y + 1, 1, 20):
        return "Cap", "Ter", name
    elif datetime.date(y - 1, 12, 23) <= date <= datetime.date(y, 1, 20):
        return "Cap", "Ter", name
    elif datetime.date(y, 1, 21) <= date <= datetime.date(y, 2, 19):
        return "Aqr", "Air", name
    elif datetime.date(y, 2, 20) <= date <= datetime.date(y, 3, 20):
        return "Psc", "Aqu", name

@dp.message_handler()
async def get_message(msg: types.Message) -> bool:
    """processes User Messages
        if entered not valid message, throws out message with help
        :param message: User Messages
        :type message: aiogram.types.message.Message (not commands)

        :rtype: None

         :param message: Not Valid Messages
        :type message: aiogram.types.message.Message (not commands)

        :rtype: None
        """
    try:
        str1, str2 = msg.text.split("\n")
        name_and_date = str1.split()
        dt = name_and_date[-1]
        name_and_date.pop(-1)
        name = ' '.join(name_and_date)
        hum1 = searc([int(x) for x in dt.split(".")], name)
        name_and_date = str2.split()
        dt = name_and_date[-1]
        name_and_date.pop(-1)
        name = ' '.join(name_and_date)
        hum2 = searc([int(x) for x in dt.split(".")], name)
        await comp(hum1, hum2, msg)
        return True
    except:
        await msg.answer(texts.Error)
        return False


if __name__ == '__main__':
    executor.start_polling(dp)
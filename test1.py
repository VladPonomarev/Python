import pyowm
import telebot

owm = pyowm.OWM('bc4471d5113a7bda39e5181a6edfd340', language = 'ru' )
bot = telebot.TeleBot("1063256767:AAEf7bYX9Gj9J4_gaze8YVq3EzN3aJx-rmA")

@bot.message_handler(content_types=['text'])
def send_echo(message):
    observation = owm.weather_at_place(message.text)
    w = observation.get_weather()
    temp = w.get_temperature('celsius')["temp"]

    answer = "В городе " + message.text + " сейчас " + w.get_detailed_status() + "\n"
    answer += "Температура сейчас в районе " + str(temp) + "\n\n"

    if temp < -20:
        answer +="Сейчас ппц как холодно, сиди дома и не куда не ходи"
    elif temp < -10:
       answer +="Сейчас ппц как холодно, отдевайся очень тепло"
    elif temp < -5:
       answer +="Сейчас холодно, одевайся теплее"
    elif temp < 0:
       answer +="Сейчас не очнь холодно, но оденься по теплее"
    else:
        answer +="На улице тепло одевай, что  угодно"


    bot.send_message(message.chat.id, answer)

bot.polling( none_stop = True )


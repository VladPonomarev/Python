import pyowm

owm = pyowm.OWM('bc4471d5113a7bda39e5181a6edfd340', language = 'ru' )

place = input("В каком городе/стране?: ")

observation = owm.weather_at_place(place)
w = observation.get_weather()

temp = w.get_temperature('celsius')["temp"]

print( "В городе " + place + " сейчас " + w.get_detailed_status())
print( "Температура сейчас в районе " + str(temp))    

if temp < -5:
    print("Сейчас ппц как холодно, отдевайся очень тепло")
elif temp < 0:
    print("Сейчас холодно, одевайся теплее")
else:
    print("На улице тепло одевай, что  угодно")


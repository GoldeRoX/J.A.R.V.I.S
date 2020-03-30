import speech_recognition as sr
from selenium import webdriver
import requests
import random
import datetime

now = datetime.datetime.today()
print(f"Just A Really Very Inteligent System ... \n Starting databases at {now} \n\n J.A.R.V.I.S. is now on-line. \n Hello Sir,")

r = sr.Recognizer()
while True:
    try:
        with sr.Microphone() as source:
            opcje = ['What I must open, sir?',
                     'Waiting for your command.',
                     'Awaiting instructions, Sir.',
                     'Awaiting instructions.',
                     ]
            print(f'{random.choice(opcje)}\n')
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            print("You said : {}".format(text))
            if text == "YouTube":
                with sr.Microphone() as source:
                    print('What I must search, Sir?\n\n')
                    r.adjust_for_ambient_noise(source)
                    audio2 = r.listen(source)
                    try:
                        text2 = r.recognize_google(audio2)
                        print("You said : {}".format(text2))
                        driver = webdriver.Chrome()
                        driver.get("https://www.youtube.com/")
                        driver.maximize_window()
                        search = driver.find_element_by_id("search")
                        search.send_keys(text2)
                        icon = driver.find_element_by_id("search-icon-legacy")
                        icon.click()
                    except:
                        print("Sorry Sir, I don't get it")
            elif text == "Wikipedia":
                with sr.Microphone() as source:
                    print('What are we looking for today, Sir?\n\n')
                    r.adjust_for_ambient_noise(source)
                    audio3 = r.listen(source)
                    try:
                        text3 = r.recognize_google(audio3)
                        print("You said : {}".format(text3))
                        driver = webdriver.Chrome()
                        driver.get("https://pl.wikipedia.org/wiki/Specjalna:Szukaj")
                        driver.maximize_window()
                        search = driver.find_element_by_id("ooui-php-1")
                        search.send_keys(text3)
                        icon = driver.find_element_by_class_name("oo-ui-actionFieldLayout-button")
                        icon.click()
                    except:
                        print("sorry, I don't get it sir")
            elif text == "GitHub":
                driver = webdriver.Chrome()
                driver.get("https://github.com/GoldeRoX")
                driver.maximize_window()
            elif text == "weather":
                #TODO muszę znaleźć sposób by "miasto" można by było wstawiać komendą głosową
                #with sr.Microphone() as source:
                 #   print('Enter your City : ')`
                  #  r.adjust_for_ambient_noise(source)
                   # city = r.listen(source)
                city = input("Enter (print) your City : ")

                def format_response(weather):
                    try:
                        name = weather['name']
                        desc = weather['weather'][0]['description']
                        temp = weather['main']['temp']

                        final_str = 'City: %s \nConditions: %s \nTemperature (°C): %s' % (name, desc, temp)
                    except:
                        final_str = 'There was a problem retrieving this information'
                    return final_str


                def get_weather(city):
                    weather_key = '6a801b642ff547be34c83afa4becc46c'
                    url = 'https://api.openweathermap.org/data/2.5/weather'
                    params = {'APPID': weather_key, 'q': city, 'units': 'Metric'}
                    response = requests.get(url, params=params)
                    weather = response.json()

                    print(format_response(weather))


                get_weather(city)
        except:
            print("Sorry Sir. I don't get it")
    except:
        pass

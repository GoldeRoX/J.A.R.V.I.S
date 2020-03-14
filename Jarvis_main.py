import speech_recognition as sr
from selenium import webdriver

r = sr.Recognizer()

with sr.Microphone() as source:
    print('Enter Anything : ')
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source)
try:
    text = r.recognize_google(audio)
    print("You said : {}".format(text))
    if text == "YouTube":
        with sr.Microphone() as source:
            print('Enter Anything : ')
            r.adjust_for_ambient_noise(source)
            audio2 = r.listen(source)
            try:
                text2 = r.recognize_google(audio2)
                print("You said : {}".format(text2))
                driver = webdriver.Chrome()
                driver.get("https://www.youtube.com/")
                search = driver.find_element_by_id("search")
                search.send_keys(text2)
                icon = driver.find_element_by_id("search-icon-legacy")
                icon.click()
            except:
                print("Sorry I don't get it")

    elif text == "Google":
        with sr.Microphone() as source:
            print('Enter Anything : ')
            r.adjust_for_ambient_noise(source)
            audio3 = r.listen(source)
            try:
                text3 = r.recognize_google(audio3)
                print("You said : {}".format(text3))
                driver = webdriver.Chrome()
                driver.get("https://www.google.pl/")
                search = driver.find_element_by_class_name("gLFyf gsfi")
                search.send_keys(text3)
                icon = driver.find_element_by_class_name("iblpc")
                icon.click()
            except:
                print("sorry, I don't get it sir")
except:
    print("Sorry Sir. I don't get it")
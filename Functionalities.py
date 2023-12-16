import win32com.client
import speech_recognition as sr
import webbrowser
import datetime
import sys
import random
import requests
import os
import bard
import re
import PyPDF2
import customtkinter
import pyautogui
import tkintermapview
import pythoncom
import pywhatkit
import spacy
import cv2
import time as tm
import threading
import smtplib
from AppOpener import open
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from googletrans import Translator
from YoutubeAutomate import YoutubeAuto

response = requests.get("https://ipinfo.io")
data = response.json()
api_key = 'your_key_here'
NER = spacy.load('en_core_web_sm')

def speak(query):
    pythoncom.CoInitialize()
    speaker = win32com.client.Dispatch("SAPI.SpVoice")
    speaker.Speak(query)
    pythoncom.CoUninitialize()

def greet_user():
    current_time = datetime.datetime.now()
    hour = current_time.hour

    if 5 <= hour < 12:
        speak("Good morning sir! How can I help today?")
    elif 12 <= hour < 17:
        speak("Good afternoon sir! How can I help today?")
    else:
        speak("Good evening sir! How can I help today?")

def translationHindiToEnglish(text):
    line = str(text)
    result = Translator().translate(line)
    data = result.text
    return data

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        r.energy_threshold = 300
        r.pause_threshold = 0.6
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query=r.recognize_google(audio , language="hi")
            return query
        except:
            print("Sorry couldn't understand that ... please repeat ..")
            # speak("Sorry couldn't understand that ... please repeat ..")

def music_fun(num,is_close):
    music_path="C:\\Users\\guddu\\Music"
    music_files=[f for f in os.listdir(music_path) if f.endswith((".mp3",".wav",".flac"))]
    # print(music_files)
    play_music=music_files[num]
    play_music_path = os.path.join(music_path,play_music)
    if(os.path.exists(play_music_path)):
        print(play_music_path)
        os.startfile(play_music_path)
    else:
        print("Path not found")
        

def pdf_reader():
    book = open("","")
    pdfReader = PyPDF2.PdfReader(book)
    pages = pdfReader.numPages
    speak(f"There are a Total of {pages} number of pages")
    speak(f"which page should I read sir ")
    user_input = takeCommand()
    user_input = translationHindiToEnglish(user_input)
    pg_num = re.findall(r"\d+",user_input)
    pg_num = int(pg_num[0])
    page = pdfReader.getPage(pg_num)
    text = page.extractText()
    speak("Sir should I write it in a notepad or should I read it for you ")
    response = takeCommand()
    if "write" in response.lower():
        pass
    elif "read" in response.lower():
        speak(text)

def send_email(msg,receiver_name):
    sender_email = 'tcloud278@gmail.com'
    sender_password = 'password_here'
    receiver_email = 'samim2904k@gmail.com'
    subject = 'null'
    message = msg

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'plain'))

    try:
        smtp_server = smtplib.SMTP('smtp.gmail.com', 587)  
        smtp_server.starttls()
        smtp_server.login(sender_email, sender_password)
        
        smtp_server.sendmail(sender_email, receiver_email, msg.as_string())
        print('Email sent successfully')
    except Exception as e:
        print(f'Email could not be sent: {e}')
    finally:
        smtp_server.quit()

def set_alarm():
    os.system("python setAlarm.py")

def enzo_fun():
    greet_user()
    num = random.randint(1,10)
    while True:
        print("Listening ... ")
        # query = takeCommand()
        # query = translationHindiToEnglish(query)
        query=input("Please enter the command..\n")
        print(query)
        print(query is None)
        if query==None:
            continue
        print("User said: ", query)
        sites=[["facebook","https://www.facebook.com"],["wikipedia","https://www.wikipedia.com"]]
        for site in sites:
            if f"open" in query.lower() and f"{site[0]}" in query.lower():
                speak(f"Opening {site[0]} sir")
                webbrowser.open(site[1])
        if "enzo" in query.lower() and "terminate" in query.lower():
            speak("Thank You for using me ...")
            sys.exit()
        elif "play" in query.lower() and "music" in query.lower() and 'youtube' not in query.lower():
            if "next" in query.lower():
                num+=1
                music_fun(num,False)
            else:
                music_fun(num,False)
        elif "the time" in query.lower():
            time=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir the time is {time}")
        elif "program" in query.lower() and "write" in query.lower():
            try:
                programming_languages = [["python",".py"],["c",".c"],["c++",".c++"],["javascript",".js"],["java ",".java"]]
                for language in programming_languages:
                    if language[0] in query.lower():
                        extension = language[1]
                bard.Main(query,extension=extension)
                speak("Sir the file is now saved you can make necessary changes to it.")
            except Exception as e:
                print(f"Error here {e}")

        elif "scan" in query.lower() and "pdf" in query.lower():
            pdf_reader()

        elif "location" in query.lower():
            ip = data['ip']
            city = data['city']
            state = data['region']
            loc = data['loc']
            lat , lon = loc.split(",")
            lat = float(lat)
            lon = float(lon)
            speak(f"Sir as being displayed you are currently in {city} , {state} ")
            root = customtkinter.CTk()
            root.geometry(f"{800}x{600}")
            root.resizable(width=False,height=False)
            root.title("current location")
            map_widget = tkintermapview.TkinterMapView(root, width=800, height=600, corner_radius=0)
            map_widget.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)
            marker = map_widget.set_position(lat , lon , marker=True) 
            marker.set_text(f"{city} , {state}")
            map_widget.set_zoom(15)
            root.mainloop()
        
        elif 'set' in query.lower() and 'alarm' in query.lower():
            speak("sir please tell me the time ")
            alarm_threading = threading.Thread(target=set_alarm)
            alarm_threading.start()
            tm.sleep(10)
            speak("Sir the alarm is set")
        elif 'open' in query.lower() and 'camera' in query.lower():
            cap = cv2.VideoCapture(0)
            while True:
                ret, frame = cap.read()
                cv2.imshow('frame', frame)
                k = cv2.waitKey(30) & 0xff
                if k == ord('q'):
                    break
            cap.release()
            cv2.destroyAllWindows()
        elif 'take screenshot' in query.lower():
            img = pyautogui.screenshot()
            img.save(r"C:\Users\guddu\Pictures\Screenshots\image.png")
            speak("Screen shot taken successfully")
        elif 'volume' in query.lower():
            if 'raise' in query.lower() or 'up' in query.lower() or 'increase' in query.lower():
                pyautogui.press("volumeup")
            elif 'low' in query.lower() or 'down' in query.lower() or 'decrease' in query.lower():
                pyautogui.press("volumedown")

        elif 'bluetooth' in query.lower():
            pyautogui.hotkey('win', 'a')
            time.sleep(1) 
            pyautogui.press('right') 
            pyautogui.press('enter') 
            pyautogui.hotkey('win', 'a')

        elif 'wifi' in query.lower():
            pyautogui.hotkey('win', 'a')
            time.sleep(1) 
            pyautogui.press('enter')
            pyautogui.hotkey('win', 'a')

        elif 'airplane' in query.lower():
            pyautogui.hotkey('win', 'a')
            tm.sleep(1) 
            pyautogui.press('right',presses=2) 
            pyautogui.press('enter') 
            pyautogui.hotkey('win', 'a')

        elif 'battery saver' in query.lower():
            pyautogui.hotkey('win', 'a')
            tm.sleep(1)
            pyautogui.press('right',presses=3)
            pyautogui.press('enter')
            pyautogui.hotkey('win', 'a')

        elif 'message' in query.lower() and 'whatsapp' in query.lower():
            raw_text = query
            text_1 = NER(raw_text)

            for word in text_1.ent:
                if word.label_ == "PERSON":
                    receiver_name = word.text
                    speak("sir what should I send")
                    msg = takeCommand()
                    msg = translationHindiToEnglish(msg)
                    pywhatkit.sendwhatmsg_instantly(receiver_name, msg, 15, True, 3)
                    break
            speak("The message is sent sir")

        elif 'email' in query.lower() or 'gmail' in query.lower():
            rawText = query
            text_2 = NER(rawText)

            for word in text_2.ent:
                if word.label_ == "PERSON":
                    receiver_name = word.text
                    speak("Sir what is the message")
                    msg = takeCommand()
                    msg = translationHindiToEnglish(msg)
                    send_email(msg,receiver_name)
                    break
            speak("The email is sent sir")

        elif 'play' in query.lower() and 'youtube' in query.lower():
            query = query.replace("play","")
            query = query.replace("youtube","")
            print(f"https://www.youtube.com/results?search_query={query}")
            webbrowser.open_new_tab(f"https://www.youtube.com/results?search_query={query}")
            tm.sleep(10)
            YoutubeAuto()
        elif 'open' in query.lower():
            query = query.replace("open", "")
            if 'enzo' in query.lower():
                query = query.replace("enzo", "")
            open(query.lower(),match_closest=True)

        elif 'calculate' in query.lower() :         
            pattern = r'([-+*/]?\d+(?:\.\d+)?)'
            matches = re.findall(pattern, query)
            math_expression = ''.join(matches)
            res = eval(math_expression)
            speak(f"Sir the result is {res}")
        
        # else:
        #     bard.Main(query=query,extension='.txt')

        try:
            if "download" in query.lower() and "youtube" in query.lower():
                speak("Sir please copy and paste the link here")
                import YoutubeDownloader
        except Exception as e:
            print(e)

        if "weather" in query.lower():
            location = data['loc']
            latitude, longitude = location.split(',')

            weather_api_url = f'https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={api_key}'
            response = requests.get(weather_api_url)
            weather_data = response.json()
            main_weather = weather_data['weather'][0]['main']
            description = weather_data['weather'][0]['description']
            temperature = weather_data['main']['temp']
            humidity = weather_data['main']['humidity']
            wind_speed = weather_data['wind']['speed']
            pressure = weather_data['main']['pressure']
            speak(f"the weather data is displayed on the screen")
            import WeatherForecastGui
            WeatherForecastGui.update_data(main_weather,description,temperature,humidity,wind_speed,pressure)

# enzo_fun()

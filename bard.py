import datetime
import pyautogui
import pyperclip
import webbrowser
import json
import keyboard
import os
import subprocess
from Operation import Speak
from bardapi import BardCookies
from time import sleep

def BardCookieFinder():
    webbrowser.open("https://bard.google.com")
    sleep(5)
    pyautogui.click(x=1773, y=69)
    sleep(2)
    pyautogui.click(x=1526, y=250)
    sleep(4)
    pyautogui.click(x=1453, y=110)
    sleep(2)
    keyboard.press_and_release("ctrl + w")

    data = pyperclip.paste()

    try:
        json_data = json.loads(data)
    except json.JSONDecodeError as e:
        print(f"Error in json {e}")

    SID = "__Secure-1PSID"
    TS = "__Secure-1PSIDTS"
    CC = "__Secure-1PSIDCC"

    SIDvalue = next((item for item in json_data if item["name"] == SID),None)
    TSvalue = next((item for item in json_data if item["name"] == TS),None)
    CCvalue = next((item for item in json_data if item["name"] == CC),None)

    if SIDvalue is not None:
        SIDvalue = SIDvalue["value"]
        os.environ[SID] = SIDvalue
    else:
        print("SIDvalue is not available")
    
    if TSvalue is not None:
        TSvalue = TSvalue["value"]
        os.environ[TS] = TSvalue
    else:
        print("TSvalue is not available")

    if CCvalue is not None:
        CCvalue = CCvalue["value"]
        os.environ[CC] = CCvalue
    else:
        print("CCvalue is not available")

    cookie_dict = {
        SID:SIDvalue,
        TS:TSvalue,
        CC:CCvalue
    }


def split_and_save_paragraphs(question, data, filename):
    paragraphs = data.split('\n\n')
    with open(filename, 'w') as file:
        file.write(data)
    data = paragraphs[:2]
    separator = ', '
    joined_string = separator.join(data)
    if 'write' in question.lower():
        Speak.voice_of_aiwin("Opening the file sir ")
        subprocess.Popen(f"notepad {filename}")
    return joined_string

def Main(query,extension):
    while True:
        try:
            SIDvalue = str(os.environ.get("__Secure-1PSID"))
            TSvalue = str(os.environ.get("__Secure-1PSIDTS"))
            CCvalue = str(os.environ.get("__Secure-1PSIDCC"))

            cookie_dict = {
                '__Secure-1PSID':SIDvalue,
                '__Secure-1PSIDTS':TSvalue,
                '__Secure-1PSIDCC':CCvalue
            }
            print(SIDvalue)
            print(TSvalue)
            print(CCvalue)
            bard = BardCookies(cookie_dict=cookie_dict)
        except:
            BardCookieFinder()
            continue
        else:
            break

    while True:
        # Question = input("Enter The Query : ")
        try:
            Question = str(query).lower()
            RealQuestion = str(Question)
            results = bard.get_answer(RealQuestion)['content']
            current_datetime = datetime.datetime.now()
            formatted_time = current_datetime.strftime("%H%M%S")
            filenamedate = str(formatted_time) + str(f"{extension}")
            # filenamedate = str(formatted_time) + ".txt"
            filenamedate = "DataBase//" + filenamedate
            formattedResults = split_and_save_paragraphs(Question, results, filename=filenamedate)
            print(formattedResults)
            if 'write' not in query.lower():
                Speak.voice_of_aiwin(formattedResults)
        except:
            continue
        else:
            break

# Main(None,None)
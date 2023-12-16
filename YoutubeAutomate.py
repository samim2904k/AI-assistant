from pyautogui import *
from keyboard import *
import time
import threading
from Body.Listen import Listen

def interface():
    import YoutubeDownloader as ytd

def actions():
    try:
        # click(x=924, y=994)
        press_and_release("ctrl + l")
        time.sleep(1)
        # click(x=1197, y=633)
        press_and_release("ctrl + c")
        time.sleep(1)
        click(x=570, y=223)
        time.sleep(1)
        hotkey('ctrl','v')
        click(x=534, y=278)
        time.sleep(1)
        click(x=519, y=378)
        time.sleep(1)
        click(x=546, y=439)
    except Exception as e:
        print(e)

def YoutubeAuto():
    click(x=718, y=641)
    while True:

        query = Listen()
        # query = input("Enter command")
        time.sleep(2)
        print(query)
        if query == None:
            continue

        elif 'pause' in query.lower():
            press('k')

        elif 'resume' in query.lower():
            press('k')

        elif 'full screen' in query.lower():
            press('f')

        elif 'volume' in query.lower():
            if 'raise' in query.lower() or 'up' in query.lower() or 'increase' in query.lower():
                press("volumeup")
            elif 'low' in query.lower() or 'down' in query.lower() or 'decrease' in query.lower():
                press("volumedown")

        elif 'film screen' in query.lower():
            press('t')

        elif 'skip' in query.lower():
            press('l')

        elif 'back' in query.lower():
            press('j')

        elif 'increase' in query.lower():
            press_and_release("shift + .")

        elif 'decrease' in query.lower():
            press_and_release("shift + ,")
        
        elif 'forward' in query.lower():
            press_and_release("shift + >")

        elif 'search' in query.lower():
            click(x=949, y=118)
            write(query)
            time.sleep(0.5)
            press('enter')

        elif 'mute' in query.lower():
            press('m')

        elif 'unmute' in query.lower():
            press('m')

        elif 'download' in query.lower() and 'video' in query.lower():
            interface_thread = threading.Thread(target=interface)

            actions_thread = threading.Thread(target=actions)

            interface_thread.start()
            time.sleep(1)
            actions_thread.start()

            interface_thread.join()
            actions_thread.join()

        elif 'next' in query.lower():
            press_and_release('shift + n')

        elif 'previous' in query.lower():
            press_and_release('shift + p')

        elif 'close' in query.lower():
            click(x=1765, y=28)
            break

# YoutubeAuto()
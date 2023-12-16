import pyttsx3
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

def voice_of_aiwin(text):
    engine = pyttsx3.init("sapi5")
    voices = engine.getProperty('voices')
    engine.setProperty('voices',voices[0].id)
    engine.setProperty('rate',170)
    print(f"\nYou : {text}.\n")
    engine.say(text)
    engine.runAndWait()



def voice_of_aich(text):
    chrome_options = Options()
    chrome_options.add_argument('--log-level=3')
    chrome_options.headless = True
    chrome_path="DataBase/chromedriver-win32/chromedriver.exe"
    driver=webdriver.Chrome(
        executable_path=chrome_path,
        options=chrome_options
    )
    driver.maximize_window()

    website = r"https://ttsmp3.com/text-to-speech/British%20English"
    driver.get(website)
    ButtonSelection = Select(driver.find_element(by=By.XPATH,value='/html/body/div[4]/div[2]/form/select'))
    ButtonSelection.select_by_visible_text("British English / Brian")
    length_of_text = len(str(text))
    if length_of_text==0:
        pass
    else:
        print(f"\nEnzo : {text}\n")
        Data = str(text)
        xpathsec = '/html/body/div[4]/div[2]/form/textarea'
        driver.find_element(By.XPATH,value=xpathsec).send_keys(Data)
        driver.find_element(By.XPATH,value='//*[@id="vorlesenbutton"]').click()
        driver.find_element(By.XPATH,value='/html/body/div[4]/div[2]/form/textarea').clear()

        if length_of_text>=30:
            time.sleep(6)

        elif length_of_text>=40:
            time.sleep(8)  

        elif length_of_text>=55:
            time.sleep(10)       

        elif length_of_text>=70:
            time.sleep(12)  

        elif length_of_text>=100:
            time.sleep(15)  

        elif length_of_text>=120:
            time.sleep(16) 

        else:
            time.sleep(4) 

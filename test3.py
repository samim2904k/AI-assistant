# import requests

# # Send a GET request to the ipinfo.io API with your IP address
# response = requests.get("https://ipinfo.io")

# # Parse the JSON response
# data = response.json()

# # Extract and print location details
# ip = data['ip']
# city = data['city']
# eregion = data['region']
# country = data['country']
# location = data['loc']

# print(f"IP: {ip}")
# print(f"City: {city}")
# print(f"Region: {region}")
# print(f"Country: {country}")
# print(f"Location (latitude, longitude): {location}")

# # Replace with your OpenWeatherMap API key
# api_key = '2b8f0d08011bec7402f4ec661502e245'

# # Get the latitude and longitude from the location obtained using the "ipinfo.io" API
# latitude, longitude = location.split(',')

# # Make a request to the OpenWeatherMap API
# weather_api_url = f'https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={api_key}'
# response = requests.get(weather_api_url)

# # Check if the request was successful
# if response.status_code == 200:
#     weather_data = response.json()
#     main_weather = weather_data['weather'][0]['main']
#     description = weather_data['weather'][0]['description']
#     temperature = weather_data['main']['temp']
#     humidity = weather_data['main']['humidity']
#     wind_speed = weather_data['wind']['speed']
#     pressure = weather_data['main']['pressure']

#     print(f"Weather: {main_weather} ({description})")
#     print(f"Temperature: {temperature}°C")
#     print(f"Humidity: {humidity}%")
#     print(f"Wind Speed: {wind_speed} m/s")
#     print(f"Pressure : {pressure}")
#     import WeatherForecastGui
#     WeatherForecastGui.update_data(main_weather,description,temperature,humidity,wind_speed,pressure)
# else:
#     print("Failed to retrieve weather data.")


# # import customtkinter
# # import tkintermapview
# # from PIL import Image


# # root = customtkinter.CTk()
# # root.geometry(f"{800}x{600}")
# # # root.title("map_view_example.py")

# # # create map widget
# # # map_widget = tkintermapview.TkinterMapView(root, width=800, height=600, corner_radius=0)
# # # map_widget.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)
# # # marker = map_widget.set_position(20.2724 , 85.8338 , marker=True) 
# # # marker.set_text("Bhubaneswar , Odisha")
# # # marker.hide_image(True)
# # # map_widget.set_zoom(15)

# # root.geometry("628x425")
# # root.configure(bg = "#FFFFFF")
# # # canvas = customtkinter.CTkCanvas(
# # #     root,
# # #     bg = "#FFFFFF",
# # #     height = 425,
# # #     width = 628,
# # #     bd = 0,
# # #     highlightthickness = 0,
# # #     relief = "ridge")
# # # canvas.place(x = 0, y = 0)

# # root.resizable(False, False)

# # my_image1 = customtkinter.CTkImage(light_image=Image.open("assets/background.jpeg"),
# #                                   dark_image=Image.open("assets/background.jpeg"),
# #                                   size=(300, 300))

# # label = customtkinter.CTkLabel(root,image=my_image1,text=None)
# # label.place(relx=0.5 , rely=0.5 , anchor=customtkinter.CENTER)
# # my_image2 = customtkinter.CTkImage(light_image=Image.open("assets/hot.png"),
# #                                    dark_image=Image.open("assets/hot.png"),
# #                                    size=(60,60))

# # label2 = customtkinter.CTkLabel(root,image=my_image2,text=None)
# # label2.place(relx=0.5 , rely=0.5 , anchor = customtkinter.CENTER)
# # root.mainloop()

# # # label = customtkinter.CTkImage(root )
# # # label.place(relx=0.5 , rely=0.5 , anchor=customtkinter.CENTER)

# import spacy
# NER = spacy.load('en_core_web_sm')

# raw_text = "Please contact Kanha regarding the project"

# text1 = NER(raw_text)

# for word in text1.ents:
#     print(word.text,word.label_)
#     print(word.label_=="PERSON")

# import re

# text = "calculate 1+2*3-10"

# # Define a regular expression pattern to match the mathematical expression
# pattern = r'([-+*/]?\d+(?:\.\d+)?)'

# # Use re.findall to extract all matches of the pattern in the text
# matches = re.findall(pattern, text)

# # Join the matches to form the mathematical expression
# math_expression = ''.join(matches)

# print("Mathematical expression:", math_expression)

# import smtplib
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart

# # Email configuration
# sender_email = 'tcloud278@gmail.com'
# sender_password = 'tksq hgxn vpji hxvv'
# receiver_email = 'samim2904k@gmail.com'
# subject = 'Test Python Msg'
# message = 'This is the message content.'

# # Create the email message
# msg = MIMEMultipart()
# msg['From'] = sender_email
# msg['To'] = receiver_email
# msg['Subject'] = subject
# msg.attach(MIMEText(message, 'plain'))

# # Connect to the SMTP server
# try:
#     smtp_server = smtplib.SMTP('smtp.gmail.com', 587)  # For Gmail
#     smtp_server.starttls()
#     smtp_server.login(sender_email, sender_password)
    
#     # Send the email
#     smtp_server.sendmail(sender_email, receiver_email, msg.as_string())
#     print('Email sent successfully')
# except Exception as e:
#     print(f'Email could not be sent: {e}')
# finally:
#     smtp_server.quit()

import pyperclip
import pyautogui
import threading
import time

yt_link = pyperclip.paste()

print(yt_link)

# ytd.link.insert(0,yt_link)
# ytd.download_quality = '360p'
# ytd.download_btn.invoke()
def interface():
    import YoutubeDownloader as ytd

def actions():
    try:
        pyautogui.click(x=570, y=223)
        time.sleep(1)
        pyautogui.hotkey('ctrl','v')
        pyautogui.click(x=534, y=278)
        time.sleep(1)
        pyautogui.click(x=519, y=378)
        time.sleep(1)
        pyautogui.click(x=546, y=439)
    except Exception as e:
        print(e)

interface_thread = threading.Thread(target=interface)

actions_thread = threading.Thread(target=actions)

interface_thread.start()
time.sleep(1)
actions_thread.start()

interface_thread.join()
actions_thread.join()
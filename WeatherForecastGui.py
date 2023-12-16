
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\CODING\c cpp\python programs\AI assistant\weather_forecast\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def update_data(main_weather,description,temperature,humidity,wind_speed,pressure):
    window = Tk()

    window.geometry("762x596")
    window.configure(bg = "#FFFFFF")
    window.title("Your Weather")
    window.iconbitmap(r"C:\CODING\c cpp\python programs\AI assistant\assets\weather_forecast.ico")

    canvas = Canvas(
        window,
        bg = "#FFFFFF",
        height = 596,
        width = 762,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        381.0,
        298.0,
        image=image_image_1
    )

    image_image_2 = PhotoImage(
        file=relative_to_assets("image_2.png"))
    image_2 = canvas.create_image(
        381.0,
        49.0,
        image=image_image_2
    )

    image_image_3 = PhotoImage(
        file=relative_to_assets("image_3.png"))
    image_3 = canvas.create_image(
        380.0,
        146.0,
        image=image_image_3
    )

    image_image_4 = PhotoImage(
        file=relative_to_assets("image_4.png"))
    image_4 = canvas.create_image(
        380.0,
        237.0,
        image=image_image_4
    )

    image_image_5 = PhotoImage(
        file=relative_to_assets("image_5.png"))
    image_5 = canvas.create_image(
        380.0,
        332.0,
        image=image_image_5
    )

    image_image_6 = PhotoImage(
        file=relative_to_assets("image_6.png"))
    image_6 = canvas.create_image(
        380.0,
        423.0,
        image=image_image_6
    )

    image_image_7 = PhotoImage(
        file=relative_to_assets("image_7.png"))
    image_7 = canvas.create_image(
        380.0,
        514.0,
        image=image_image_7
    )
    canvas.create_text(
        225.0,
        123.0,
        anchor="nw",
        text=f"Weather - {main_weather} ({description})",
        fill="#FFFFFF",
        font=("Inter", 24 * -1)
    )


    canvas.create_text(
        225.0,
        213.0,
        anchor="nw",
        text=f"Temperature - {temperature}°C",
        fill="#FFFFFF",
        font=("Inter", 24 * -1)
    )

    canvas.create_text(
        225.0,
        306.0,
        anchor="nw",
        text=f"Humidity - {humidity}%",
        fill="#FFFFFF",
        font=("Inter", 24 * -1)
    )

    canvas.create_text(
        230.0,
        397.0,
        anchor="nw",
        text=f"Wind Speed - {wind_speed}m/s",
        fill="#FFFFFF",
        font=("Inter", 24 * -1)
    )

    canvas.create_text(
        230.0,
        492.0,
        anchor="nw",
        text=f"Pressure - {pressure}",
        fill="#FFFFFF",
        font=("Inter", 24 * -1)
    )
    window.resizable(False, False)
    window.mainloop()
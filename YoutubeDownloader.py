import customtkinter
import time
from pytube import YouTube

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.geometry("700x480+100+100")
app.title("Youtube Downloader")
app.resizable(False,False)
app.iconbitmap(r"C:\CODING\c cpp\python programs\AI assistant\assets\youtube_downloader.ico")
app.attributes("-topmost",1)

download_quality = '144p'

def startDownload():
    try:
        global download_quality
        print(download_quality)
        yt_link = link.get()
        ytObject = YouTube(yt_link,on_progress_callback=on_progress)
        info.configure(text=ytObject.title,text_color="white")
        video = ytObject.streams.get_by_resolution(download_quality)
        video.download()
        notify_label.configure(text="Downloaded !!", text_color="green")
        time.sleep(3)
        app.destroy()
    except Exception as e:
        notify_label.configure(text="Download Error !!",text_color="red")
        print(e)

def on_progress(stream,chunks,bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    progress_percentage = bytes_downloaded/total_size * 100
    per = str(int(progress_percentage))
    progress_per.configure(text=per + "%")
    progress_per.update()
    progress_bar.set(float(progress_percentage)/100)

def resolution_change(choice):
    global download_quality
    download_quality = choice
    print(download_quality)
    print(type(download_quality))

info = customtkinter.CTkLabel(app,text="Insert the YouTube Link",font=('Verdana',20))
info.pack(padx=10,pady=10)

url_var = customtkinter.StringVar()
link = customtkinter.CTkEntry(app, width=450 , height=40,textvariable=url_var)
link.pack()

quality_check = customtkinter.CTkOptionMenu(app, values=["144p","240p","360p","480p","720p"], command=resolution_change)
quality_check.pack(padx=10, pady=10)

notify_label = customtkinter.CTkLabel(app, text="")
notify_label.pack()

progress_per = customtkinter.CTkLabel(app, text="0%")
progress_per.pack()

progress_bar = customtkinter.CTkProgressBar(app, width=400)
progress_bar.set(0)
progress_bar.pack(padx=10, pady=10)

download_btn = customtkinter.CTkButton(app, text="Download", command=startDownload)
download_btn.pack(padx=10, pady=10)

app.mainloop()
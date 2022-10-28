from download import * 
import tkinter as tk


win = tk.Tk()
win.geometry("800x800")
win.title("GUYL")

format_option = tk.IntVar()
playlist_option = tk.IntVar()
link = tk.StringVar()

def raise_error():
    e_win = tk.Tk()
    e_win.geometry("200x200")
    e_win.title("ERROR")
    tk.Label(e_win,text="Error, you probably entered the wrong URL").pack()
    tk.Button(e_win,text="Got It !",command=e_win.destroy).pack()

def get_link():
    download_type = int(playlist_option.get())
    download_link = str(link.get())
    try:
        if download_type == 1:
            PlaylistDownload(download_link).download_audio_default()
        elif download_type == 2:
            PlaylistDownload(download_link).download_video_default()
        elif download_type == 3:
            SingleDownload(download_link).download_audio_default()
        elif download_type == 4:
            SingleDownload(download_link).download_video_default()
        else:
            raise_error()
    except:
        raise_error()
    


tk.Label(win,text="Grandma Useable Youtube Downloader").pack() 
tk.Entry(win,textvariable=link).pack()
tk.Radiobutton(win,text="Audio from Playlist",variable=playlist_option,value=1).pack()
tk.Radiobutton(win,text="Video from Playlist",variable=playlist_option,value=2).pack()
tk.Radiobutton(win,text="Audio from Video",variable=playlist_option,value=3).pack()
tk.Radiobutton(win,text="Video from Video",variable=playlist_option,value=4).pack()
tk.Button(win,text="Submit",command=get_link).pack()
win.mainloop()

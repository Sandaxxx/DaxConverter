import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from tkinter import ttk, messagebox, filedialog
from PIL import Image
from moviepy.editor import VideoFileClip
import signal
import sys

def signal_handler(sig, frame):
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

ctk.set_appearance_mode("transparent")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

def open_file_dialog():
    global filename
    filename = filedialog.askopenfilename()

def convert_file():
    if filename and option_menu.get():
        try:
            extension = option_menu.get()
            output_filename = filename.split('.')[0] + '.' + extension
            if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif','ico', '.webp', '.mp4','.mov','.avi', '.jfif')):
                img = Image.open(filename)
                img.save(output_filename)
            elif filename.lower().endswith(('.mp4', '.avi', '.mov', '.flv')):
                clip = VideoFileClip(filename)
                clip.write_videofile(output_filename)
            messagebox.showinfo(f"Info", "Sucess Convert !")
        except Exception as e:
            messagebox.showinfo("Info", f"{e}")

app = ctk.CTk()
app.geometry("280x300")
app.title("DaxConverter | By Sandax")
app.iconbitmap('./ico.ico')
app.resizable(height=0, width=0)

bg_image = tk.PhotoImage(file="bg.png")  

bg_label = tk.Label(app, image=bg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

open_file_button = ctk.CTkButton(app, text="Open File",border_width=0, corner_radius=8,width=120, height=30, command=open_file_dialog)
open_file_button.place(x=85, y=110)  

option_menu = ctk.CTkOptionMenu(app,width=120, height=30, values=["png", "jpg",'ico', "webp", "gif", "mp4", "avi", "mov", "flv"])
option_menu.place(x=85, y=175)  

convert_button = ctk.CTkButton(app, text="Valid",border_width=0, corner_radius=8,width=120, height=30, command=convert_file )
convert_button.place(x=85, y=235)  


app.mainloop()

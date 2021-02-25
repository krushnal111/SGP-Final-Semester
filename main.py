import tkinter as tk
import tkinter.font as font
from recordings import record
from PIL import Image, ImageTk

window = tk.Tk()
window.title("Smart cctv")
window.iconphoto(False, tk.PhotoImage(file='mn.png'))
window.geometry('1080x760')


frame1 = tk.Frame(window)

label_title = tk.Label(frame1, text="Smart cctv Camera")
label_font = font.Font(size=35, weight='bold',family='Helvetica')
label_title['font'] = label_font
label_title.grid(pady=(10,10), column=2)


icon = Image.open('SGP/spy.png')
icon = icon.resize((150,150), Image.ANTIALIAS)
icon = ImageTk.PhotoImage(icon)
label_icon = tk.Label(frame1, image=icon)
label_icon.grid(row=1, pady=(5,10), column=2)

btn2_image = Image.open('SGP/exit.png')
btn2_image = btn2_image.resize((50,50), Image.ANTIALIAS)
btn2_image = ImageTk.PhotoImage(btn2_image)


btn1_image = Image.open('icons/recording.png')
btn1_image = btn1_image.resize((50,50), Image.ANTIALIAS)
btn1_image = ImageTk.PhotoImage(btn1_image)



btn1 = tk.Button(frame1, text='Record', height=90, width=180, fg='orange', command=record, image=btn1_image, compound='left')
btn1['font'] = btn_font
btn1.grid(row=1, pady=(20,10), column=1)


btn2 = tk.Button(frame1, height=90, width=180, fg='red', command=window.quit, image=btn5_image)
btn2['font'] = btn_font
btn2.grid(row=1, pady=(20,10), column=2)

frame1.pack()
window.mainloop()

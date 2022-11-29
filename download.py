from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from moviepy import *
from moviepy.editor import VideoFileClip
#from moviepy.audio.io. import VideoFileClip
from pytube import YouTube
import shutil

screen = Tk()


title = screen.title('Aplikace na stahování videí')
width = 500 # Width 
height = 600 # Height

screen_width = screen.winfo_screenwidth()  # Width of the screen
screen_height = screen.winfo_screenheight() # Height of the screen
# Calculate Starting X and Y coordinates for Window
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
screen.geometry('%dx%d+%d+%d' % (width, height, x, y))
canvas = Canvas(screen, width=width, height=height)
canvas.pack()

def download_file():
    if link_field.index("end") ==0:
        messagebox.showwarning("showwarning", "Chybí odkaz na video!")
        return
    if path_label.cget("text")=="Vyber místo uložení videa:" or (path_label.cget("text")==""):
        messagebox.showwarning("showwarning", "Není vybrané místo uložení videa!")
    else:
        
        #get user path
        get_link = link_field.get()
        #get selected path
        user_path = path_label.cget("text")
        screen.title('Stahování videa.......')
        #Download Video
        mp4_video = YouTube(get_link).streams.get_highest_resolution().download()
        vid_clip = VideoFileClip(mp4_video)
        vid_clip.close()
        #move file to selected directory
        shutil.move(mp4_video, user_path)
        messagebox.showwarning("showwarning", "Video bylo staženo!")
        screen.title('Aplikace na stahování videí')

def select_path():
    #allows user to select a path from the explorer
    path = filedialog.askdirectory()
    path_label.config(text=path)

#image logo
logo_img = PhotoImage(file='yt.png')
main_logo=PhotoImage(file='main.png')
#resize
logo_img = logo_img.subsample(2, 2)
main_logo=main_logo.subsample(8,8)
canvas.create_image(250, 80, image=logo_img)
canvas.create_image(250, 520, image=main_logo)


#link field
link_field = Entry(screen, width=40, font=('Arial', 15) )
link_label = Label(screen, text="Zadej odkaz na video: ", font=('Arial', 15))

#Select Path for saving the file
path_label = Label(screen, text="Vyber místo uložení videa:", font=('Arial', 15))
select_btn =  Button(screen, text="Vybrat místo", bg='red', padx='22', pady='5',font=('Arial', 15), fg='#000', command=select_path)
#Add to window
canvas.create_window(250, 280, window=path_label)
canvas.create_window(250, 330, window=select_btn)

#Add widgets to window 
canvas.create_window(250, 170, window=link_label)
canvas.create_window(250, 220, window=link_field)

#Download btns
download_btn = Button(screen, text="Stáhnout video",bg='green', padx='22', pady='25',font=('Arial', 15), fg='red', command=download_file)
#add to canvas
canvas.create_window(250, 400, window=download_btn)

made_label=Label(screen,text="© Václav Kamenický")
canvas.create_window(250,580,window=made_label)




screen.mainloop()

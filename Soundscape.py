#Import Libraries
import tkinter
from tkinter import PhotoImage,Button,Frame,Menu,filedialog
from PIL import Image,ImageTk
import pygame
import os

#Start Tkinter root window
root= tkinter.Tk()
#Initialize pygame
pygame.init()

#TITLE AND GUI WINDOW
root.title("Soundscape") #window title
root.geometry("650x700+400+30" )
root.configure(background="black")
root.resizable(False,False)

#Frame at the bottom of the window
down_frame = Frame(root, bg = "#D6D5CB" , width= 650, height= 200) 
down_frame.place(x=0,y=600)

#ICON
icon = PhotoImage(file="icons\\icon.png")
root.iconphoto(False, icon)
list_label = tkinter.Label(root, text="Song list",bg="#28abfa",font=("Arial" ,11))
list_label.pack(fill="x", expand=False)


#Listbox to add songs and a scroll bar
Listbox= tkinter.Listbox(root, bg="grey", font=("Arial",11) )
scrollbar = tkinter.Scrollbar(root, orient="vertical")
Listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=Listbox.yview)
scrollbar.place(x=635,y= 22, height=186)
Listbox.pack(fill="x")



#CREATE A LABEL TO VIEW THE NAME OF CURRENTLY PLAYING SONG
songlabel = tkinter.Label(root, text="", font=("Arial", 16),bg="black")
songlabel.pack(side="top", fill="y")
#CREATE LABEL FOR STOP LABEL
stoplabel= tkinter.Label(root, text="",bg="black",font=("Arial", 16),fg="red")
stoplabel.pack()


#global variables
playing= False
loops=1
state ="unactive"
stat = "unactive"
k=1
direc=""


#Number of frames in GIF
frameCnt = 158
#Get and store photoimage in a list frame by frame
frames = [PhotoImage(file='icons\\player gif.gif',format = 'gif -index %i' %(i)) for i in range(frameCnt)] 



def play_song(select_event):
    global loops
    global state
    global k
    global playing
    global direc

    # Get the index of the selected song
    index = Listbox.curselection()
    # Stops the song on selection and to play symbol
    pygame.mixer.music.stop()
    playButton.config(image=r_pauseButton)
        
    label = tkinter.Label(root)
    label.configure(image=frames[0])
        
    # Get the text of the selected song
    item_text = Listbox.get(index)
    
    file_path= os.path.join(direc,item_text)
    #PRINTS THE NAME OF CURRENTLY PLATING SONG
    songlabel.config(text="Now playing\n"+item_text[0:-4], bg="black",fg="white")
    
    #LOAD THE SONG AND THEN PLAY IT
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play(loops=loops) #VALUE OF LOOPS WILL DEFINE WHETHER TO PLAY IT INDEFINITELY OR ONLY ONE TIME
    
    #THIS WILL MAKE SURE THAT THE GIF STARTS ONLY ONE TIME AND NOT AGAIN ON RECALLING THE FUNCTION
    if k==1:
        def update(ind):
            global k
            frame = frames[ind] #GET FRAME FROM THE LIST
            ind += 1 #INCREMENTS THE INDEX OF FRAME IN LIST
            if ind == frameCnt: #IF INDEX EQUALS TO TOTAL FRAMES, MAKE IT ZERO
                ind = 0
            label.configure(image=frame) 
            k=0
                
            root.after(10, update, ind) #THIS WILL CALL THE FUNCTION AGAIN AGAIN AFTER 10 MS DELAY TO PLAY FRAMES OF GIF
                    
        label.pack()
        root.after(0, update, 0)#THIS WILL RESTART THE GIF
    #This will empty the string which was initited on press of StopButton
    stoplabel.config(text="")
    #update the state of playing
    playing=pygame.mixer.music.get_busy()
    
#.............................................................................................................................
def prev_song():
    global loops
    global state
    global playing
    global direc
    # Stop the current song
    pygame.mixer.music.stop()
    
    # Get the index of the currently selected item in the listbox
    index = Listbox.curselection()
    
    # If the index of the currently selected item is greater than 0
    if index[0] >0:
        # Decrement the index by 1
        index = index[0] - 1
        # Get the song at the new index
        item_text = Listbox.get(index)
        file_path= os.path.join(direc,item_text)
        # Update the song label
        songlabel.config(text="Now playing\n"+item_text[0:-4], bg="black", fg="white")
        print(item_text)
        # Load and play the song
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play(loops=loops)#VALUE OF LOOPS WILL DEFINE WHETHER TO PLAY IT INDEFINITELY OR ONLY ONE TIME
        
        # Clear the current selection in the listbox
        Listbox.select_clear(0, "end")
        # Set the active element in the listbox to the song at the new index
        Listbox.activate(index)
        # Set the selection in the listbox to the song at the new index
        Listbox.select_set(index)
        playing=pygame.mixer.music.get_busy()      
        
    else:
        # Clear the current selection in the listbox
        Listbox.select_clear(0, "end")
        # Set the active element in the listbox to the last element
        Listbox.activate("end")
        # Set the selection in the listbox to the last element
        Listbox.select_set("end")
        # Get the Index for the active element
        index = Listbox.index("active")       
        # Get the song at the new index
        item_text = Listbox.get(index)
        file_path= os.path.join(direc,item_text)
        # Update the song label
        songlabel.config(text="Now playing\n"+item_text[0:-4], bg="black",fg="white")
        # Load and play the song
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play(loops=loops)#VALUE OF LOOPS WILL DEFINE WHETHER TO PLAY IT INDEFINITELY OR ONLY ONE TIME    
        playing=pygame.mixer.music.get_busy()#update playing
        print(item_text)
        

#.............................................................................................................................


def next_song():
    global loops
    global state
    global playing
    global direc
    # Stop the current song
    pygame.mixer.music.stop()
    
    # Get the index of the currently selected item in the listbox
    index = Listbox.curselection()    
    # If the index of the currently selected item is less than the size of the listbox minus 1
    if index[0] < Listbox.size()-1:
        # Increment the index by 1
        index = index[0] + 1
        # Get the song at the new index
        item_text = Listbox.get(index)
        file_path= os.path.join(direc,item_text)
        # Update the song label
        songlabel.config(text="Now playing\n"+item_text[0:-4], bg="black", fg="white")
        # Load and play the song
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play(loops=loops)#VALUE OF LOOPS WILL DEFINE WHETHER TO PLAY IT INDEFINITELY OR ONLY ONE TIME
        # Clear the current selection in the listbox
        Listbox.select_clear(0, "end")
        # Set the active element in the listbox to the song at the new index
        Listbox.activate(index)
        # Set the selection in the listbox to the song at the new index
        Listbox.select_set(index)
        print(item_text)
        playing=pygame.mixer.music.get_busy()#update playing
        
        
        
    # If the index of the currently selected item is equal to the size of the listbox minus 1
    else:
        Listbox.select_clear(0, "end")
        # Set the active element in the listbox to the first item with an index of 0
        Listbox.activate(0)
        # Set the selection in the listbox to the first item with an index of 0
        Listbox.select_set(0)        
        # Set the index to 0
        index = 0
        # Get the song at the new index
        item_text = Listbox.get(index)
        file_path= os.path.join(direc,item_text)
        
        # Update the song label
        songlabel.config(text="Now playing\n"+item_text[0:-4], bg="black",fg="white")
        # Load and play the song
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play(loops=loops) #VALUE OF LOOPS WILL DEFINE WHETHER TO PLAY IT INDEFINITELY OR ONLY ONE TIME       
        playing=pygame.mixer.music.get_busy()#update playing
        print(item_text)
        
        

#.............................................................................................................................

def open_file():
    global direc
    # Use the askopenfilename function to get the selected song file
    song_file = filedialog.askopenfilename(title="Select a Music file", filetypes=[("Music files", "*.wav")])
    # Get the file name from the full path
    print(song_file)
    direc= os.path.dirname(song_file)
    song_name = os.path.basename(song_file)
    print(song_name)
    Listbox.insert(tkinter.END, song_name)
    Listbox.bind("<<ListboxSelect>>", play_song)


#.............................................................................................................................

def open_files():
    global direc
    # Use the askopenfilename function to get the selected song file
    song_files = filedialog.askopenfilenames(title="Select Music files", filetypes=[("Music files", "*.wav")])
    
    # Get the file name from the full path one by one using for loop and insert it in listbox
    for song_file in song_files:
        
        direc= os.path.dirname(song_file)
        song_name = os.path.basename(song_file)
        
    Listbox.insert(tkinter.END, song_name)
    Listbox.bind("<<ListboxSelect>>", play_song)


#.............................................................................................................................





def open_folder():
    global direc
    # Open the file dialog and get the selected directory path
    direc = filedialog.askdirectory()
    
    # Get the list of files in the directory
    files = os.listdir(direc)
    files = [f for f in files if f.endswith(".wav")]

    for file in files:
    # Get the file path and song name for the current file
        file_path = os.path.join(direc, file)
        song_name = os.path.basename(file_path)
        item_text = song_name
        Listbox.insert(tkinter.END, item_text)
        
    Listbox.bind("<<ListboxSelect>>", play_song)




#switching state of play/pause    
def play_stop():
    global playing
    #test the current state
    
    if playing:
        
        playButton.config(image=r_playButton)
        pygame.mixer.music.pause()
        playing=pygame.mixer.music.get_busy()
        
        
    else:
        playButton.config(image=r_pauseButton)
        pygame.mixer.music.unpause()
        playing=pygame.mixer.music.get_busy()      
        

def stop_song():
    pygame.mixer.music.stop()
    playing=pygame.mixer.music.get_busy()
    Listbox.select_clear("active")
    playButton.config(image=r_playButton) 
    
    stoplabel.config(text="Select Song form the SONG LIST to start the song")
    
    songlabel.config(text="")



def rep_song(state):
    global loops
    if state == "active":
        loops=-1
    elif state == "unactive":
        loops=1

    if loops==-1:
        no_loop.config(image=r_repeat)
    elif loops== 1:
        no_loop.config(image=r_no_loop)
    print(loops)


def r_state():
    global stat
    if stat == "unactive":    
        stat="active"    
    elif stat =="active":        
        stat="unactive"
    
    rep_song(stat)



#BUTTONS

#REPEAT BUTTON
repeatButton = Image.open("icons\\repeat.png")
r_repeat = repeatButton.resize((40, 40))
r_repeat = ImageTk.PhotoImage(r_repeat)
repeatButton=Button(root, image=r_repeat, bd=0, bg="#D6D5CB",command=r_state)
repeatButton.place(x=550, y=615)

#NO REPEAT/LOOP BUTTON
no_loop = Image.open("icons\\no loop.png")
r_no_loop = no_loop.resize((40, 40))
r_no_loop = ImageTk.PhotoImage(r_no_loop)
no_loop=Button(root, image=r_no_loop, bd=0, bg="#D6D5CB",command=r_state)
no_loop.place(x=550, y=615)



# NEXT SONG BUTTON
nextButton = Image.open("icons\\next.png")
r_nextButton = nextButton.resize((40, 40))
r_nextButton = ImageTk.PhotoImage(r_nextButton)
nextButton=Button(root, image=r_nextButton, bd=0, bg="#D6D5CB", command=next_song)
nextButton.place(x=360, y=615)


#PAUSE SONG BUTTON
pauseButton = Image.open("icons\\pause.png")
r_pauseButton = pauseButton.resize((40, 40))
r_pauseButton = ImageTk.PhotoImage(r_pauseButton)
pauseButton=Button(root, image=r_pauseButton, bd=0, bg="#D6D5CB", command=play_stop)
pauseButton.place(x=310, y=615)

#PLAY/UNPAUSE SONG BUTTON
playButton = Image.open("icons\\play-button.png")
r_playButton = playButton.resize((40, 40))
r_playButton = ImageTk.PhotoImage(r_playButton)
playButton=Button(root, image=r_playButton, bd=0, bg="#D6D5CB",command=play_stop)
playButton.place(x=310, y=615)

#PREVIOUS BUTTON
prevButton = Image.open("icons\\previous.png")
r_prevButton = prevButton.resize((40, 40))
r_prevButton = ImageTk.PhotoImage(r_prevButton)
prevButton=Button(root, image=r_prevButton, bd=0, bg="#D6D5CB",command=prev_song)
prevButton.place(x=260, y=615)

#STOP SONG BUTTON
stopButton = Image.open("icons\\stop-button.png")
r_stopButton = stopButton.resize((40, 40))
r_stopButton = ImageTk.PhotoImage(r_stopButton)
stopButton=Button(root, image=r_stopButton, bd=0, bg="#D6D5CB",command=stop_song)
stopButton.place(x=20, y=615)

#CREATING MENU
menubar = Menu(root)
file = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='File', menu = file)
file.add_command(label ='Open Folder', command = open_folder)
file.add_command(label ='Open File', command = open_file)
file.add_command(label ='Open Multiple Files', command = open_files)
file.add_separator()
file.add_command(label ='Exit', command = root.destroy)
root.config(menu = menubar)




#TKINTER WINDOW LOOP
root.mainloop()
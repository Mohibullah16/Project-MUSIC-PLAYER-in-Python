# Project-MUSIC-PLAYER-in-Python
Music player built in python using tkinter and pygame libraries. 
Introduction:
	Background:
Music has always been a popular form of entertainment and many people enjoy listening to music on their computers or other devices.
There are many music player applications available, but some users may prefer to create their own player with specific features or a custom interface.
Motivation:
The goal of this project is to create a simple music player with a graphical user interface (GUI) that allows the user to browse for and add audio files to a playlist, and control the playback of the songs using buttons.
Overview:
The music player has a list of songs displayed in a listbox widget and several buttons for controlling the playback of the songs.
The user can add audio files to the playlist by clicking the "File" menu and selecting the "Open" option, which opens a file selection dialog.
The user can select a song in the listbox to play it, and use the "previous", "next", "stop", and "play/pause" buttons to control the playback of the songs.
The name of the current song is displayed in a label widget and a message indicating that the song has been stopped is displayed in another label widget.
The audio files are played using the pygame library.




1.	The tkinter library is imported and several widgets are imported from it: PhotoImage, Button, Frame, and Menu. The Image and ImageTk modules are imported from PIL (Python Imaging Library) to allow the use of images as icons for the buttons. The filedialog module is imported to allow the user to browse for and select audio files to add to the playlist.
2.	The pygame library is imported and initialized.
3.	The root variable is defined as a Tk object, which is the main window of the application.
4.	The index variable is defined as a global variable and initialized to 0. This variable will be used to store the index of the current song in the playlist.
5.	A Label widget is created to display the text "Song list" at the top of the window.
6.	A Listbox widget is created to display the playlist.
7.	A Menu widget is created as the menubar of the application.
8.	A Label widget is created to display the name of the current song.
9.	A Label widget is created to display a message indicating that the song has been stopped.
10.	The play_song() function is defined to be called when the user clicks on a song in the listbox. This function stops the current song and plays the selected song. It also updates the song label to display the name of the selected song.
11.	The prev_song() function is defined to be called when the user clicks the "previous" button. This function stops the current song and plays the previous song in the list. It also updates the song label to display the name of the previous song.
12.	The next_song() function is defined to be called when the user clicks the "next" button. This function stops the current song and plays the next song in the list. It also updates the song label to display the name of the next song.
13.	The stop_song() function is defined to be called when the user clicks the "stop" button. This function stops the current song and updates the stop label to display a message indicating that the song has been stopped.
14.	The play_pause() function is defined to be called when the user clicks the "play/pause" button. This function either plays or pauses the current song depending on its current state. It also updates the icon of the "play/pause" button to reflect the current state of the song.




 

Here is a summary of the flow of the code:
1.	The main window of the application (root) is created and the playlist, song label, and stop label are displayed.
2.	The user can interact with the listbox by clicking on a song to select it.
3.	When the user clicks on a song in the listbox, the play_song() function is called. This function stops the current song, plays the selected song, and updates the song label to display the name of the selected song.
4.	The user can also interact with the "previous", "next", "stop", and "play/pause" buttons to control the playback of the songs.
5.	When the user clicks the "previous" button, the prev_song() function is called. This function stops the current song, plays the previous song in the list, and updates the song label to display the name of the previous song.
6.	When the user clicks the "next" button, the next_song() function is called. This function stops the current song, plays the next song in the list, and updates the song label to display the name of the next song.
7.	When the user clicks the "stop" button, the stop_song() function is called. This function stops the current song and updates the stop label to display a message indicating that the song has been stopped.
8.	When the user clicks the "play/pause" button, the play_pause() function is called. This function either plays or pauses the current song depending on its current state, and updates the icon of the "play/pause" button to reflect the current state of the song.
 
Here is a more detailed breakdown of the flow of the code:
1.	The main window of the application (root) is created and the playlist, song label, and stop label are displayed. The main window also has a menubar with a "File" menu.
2.	When the user clicks the "File" menu, a dropdown menu appears with the "Open" and "Exit" options.
3.	If the user clicks the "Open" option, the filedialog.askopenfilename() function is called to open a file selection dialog. The user can then browse for and select one or more audio files to add to the playlist. The selected audio files are then added to the listbox widget.
4.	The user can interact with the listbox by clicking on a song to select it. When the user clicks on a song in the listbox, the play_song() function is called.
5.	The play_song() function gets the index of the selected song using the curselection() method of the listbox widget. It then stops the current song using the stop() method of the pygame.mixer.music module and updates the icon of the "play/pause" button to the "play" icon.
6.	The play_song() function gets the name of the selected song using the get() method of the listbox widget and updates the song label to display the name of the selected song.
7.	The play_song() function loads the selected song using the load() method of the pygame.mixer.music module and plays it using the play() method. It also updates the icon of the "play/pause" button to the "pause" icon.
8.	The user can also interact with the "previous", "next", "stop", and "play/pause" buttons to control the playback of the songs.
9.	When the user clicks the "previous" button, the prev_song() function is called. This function stops the current song using the stop() method of the pygame.mixer.music module and decrements the value of the index variable by 1.
10.	The prev_song() function checks if the value of the index variable is within the range of the listbox using the size() method of the listbox widget. If the index is within range, it selects the previous item in the listbox using the select_set() method and gets the name of the previous song using the get() method of the listbox widget. It then updates the song label to display the name of the previous song and loads and plays the previous song using the load() and play() methods of the pygame.mixer.music module.
11.	If the index is not within range, the index is reset to 0 and the first item in the listbox is selected using the select_set() method. The name of the first song is then retrieved using the get() method of the listbox widget and the song label is updated to display the name of the first song. The first song is then loaded and played using the load() and play() methods of the pygame.mixer.music module.
12.	When the user clicks the "next" button, the next_song() function is called. This function stops the current song using the stop() method of the pygame.mixer.music module and increments the value of the index variable by 1.
13.	The next_song() function checks if the value of the index variable is within the range of the listbox using the size() method of the listbox widget. If the index is within range, it selects the next item in the listbox using the select_set() method and gets the name of the next song using the get() method of the listbox widget. It then updates the song label to display the name of the next song and loads and plays the next song using the load() and play() methods of the pygame.mixer.music module.
14.	If the index is not within range, the index is reset to 0 and the first item in the listbox is selected using the select_set() method. The name of the first song is then retrieved using the get() method of the listbox widget and the song label is updated to display the name of the first song. The first song is then loaded and played using the load() and play() methods of the pygame.mixer.music module.
15.	When the user clicks the "stop" button, the stop_song() function is called. This function stops the current song using the stop() method of the pygame.mixer.music module and updates the stop label to display a message indicating that the song has been stopped.
16.	When the user clicks the "play/pause" button, the play_pause() function is called. This function checks the current state of the song using the get_busy() method of the pygame.mixer.music module. If the song is currently playing, the function pauses the song using the pause() method of the pygame.mixer.music module and updates the icon of the "play/pause" button to the "play" icon. If the song is currently paused, the function resumes the song using the unpause() method of the pygame.mixer.music module and updates the icon of the "play/pause" button to the "pause" icon.





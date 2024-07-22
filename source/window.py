import tkinter as tk
import time
import json 
import pygame

#getting stuff from the json file
with open("source/info.json", 'r') as file:
    data = json.load(file)

#getting the correct variable names from the json file
close_time = data['close_time'];
make_sound = data['make_sound'];
ogpassword = data['password'];
    

def play_sound():
    if make_sound:
        pygame.mixer.init()  # Initialize the mixer
        sound = pygame.mixer.Sound(r"C:\Users\abhi\Documents\Programs\ML_DL_AI_Projects\PC-Surveillance\source\sounds\beep-warning-6387.mp3")  # Load your sound file
        sound.play()  # Play the sound
        pygame.time.wait(500)  # Wait for the sound to finish


            

def window_main():
    # Create the main window
    root = tk.Tk()
    root.title("Password Entry")

    # set size of window and keep it on top 
    root.attributes('-fullscreen', True)
    root.attributes('-topmost', True)
    root.overrideredirect(True)
    root.resizable(False, False)

   
    #play first sound
    play_sound();
    # Create a label and entry for password input
    label = tk.Label(root, text="ENTER YOUR PASSWORD WITHIN 30 SECONDS OR ELSE YOUR PC WILL SHUT DOWN:").pack(pady=10)
    password_entry = tk.Entry(root, show='*')
    password_entry.pack(pady=5)
        
    
    def on_ok():
        password = password_entry.get()
        if password == ogpassword:
            print('not shut down computer here')
            root.destroy()
        else:
            play_sound()
    
    
    # Create OK button
    tk.Button(root, text="OK", command=on_ok).pack(pady=10)
    root.bind('<Return>', lambda event: on_ok())
    
    # Display the window
    root.after(close_time*1000, root.destroy)  #closes window after 30 seconds and will then proceed to shut down the pc
    root.mainloop()
    print('shut down computer here')
    
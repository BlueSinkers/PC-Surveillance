# PC-Surveillance
This uses YOLO (You Only Look Once) to make a surveillance detector that can be used to check if someone is operating your computer through your webcam. This is a very basic project you can complete after understanding how YOLO and other object-detection algorithms work, and is referneced in my note which you can find on my website.

Some basic things about what's going on:
- I have a settings tab in a JSON file ("source/info.json") that has a bunch of settings that are tweakable to affect the performance of the surveillance checker.
- The tab to input the password (which is the info.json area -- this isn't a very secure surveillance checker obviously) was created using TKINTER and is an unresizable, unadjustable, and unmovable screen-size window which mandates the password be entered in within an amount of seconds prior to the computer shutting down.
- The feature of checking on if someone is operating the computer is done using YOLO's V5 Object Detector. If the detector (untrained, vanilla version that comes standard with YOLO) yields that a person is in the webcams view, then the process of freezing up the screen and forcing the password to be entered will happen.

To run this, you will need to INSTALL the following things in the environment:
```
torch
cv2
pygame
```
The rest of the modules used as native/already in Python:
```
tkinter
time
json
os
```

If you have any questions about this, contact me at akidamb1@terpmail.umd.edu
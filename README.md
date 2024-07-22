# PC-Surveillance
This uses YOLO (You Only Look Once) to make a surveillance detector that can be used to check if someone is operating your computer through your webcam. Some functionality doesn't work such as the ability to see a live viewing of the camera for example. This will be updated soon. 

Some basic things about what's going on:
- I have a settings tab in a JSON file ("source/info.json") that has a bunch of settings that are tweakable to affect the performance of the surveillance checker.
- The tab to input the password (which is the info.json area -- this isn't a very secure surveillance checker obviously) was created using TKINTER and is an unresizable, unadjustable, and unmovable screen-size window which mandates the password be entered in within 30 seconds prior to the computer shutting down.
- The feature of checking on if someone is operating the computer is done using YOLO's V5 Object Detector. If the detector (untrained, vanilla version that comes standard with YOLO) yields that a person is in the webcams view, then the process of freezing up the screen and forcing the password to be entered will happen.

To DO:
- add the shut down functionality once everything is finished
- complete the viewing of the camera feature prior and size it to be the entire screen-size
- add some functionality such that the OG computer user doesn't need to wait and enter the password for the program to work

NOTE THAT THIS IS STILL NOT TOTALLY WORKING
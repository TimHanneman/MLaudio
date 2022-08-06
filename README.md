# MLaudio
Simple Audio Recording software for recording Training/Target audio sets (WAV files) for machine learning.

![Project Screenshot](Screenshot.png?raw=true)

MLaudio is a tool that can be used for recording audio to match another set of already recorded audio files.
When no audio clips folder is set you can record 3.5 second wav files. If there is a matching audio clips folder then record
time is set to be equal to the target audio + 0.5 seconds. Save happens after each next.

# How to Use
1) Copy this github project into a folder
2) Run the project: python MLaudio.py

#Installation/Dependencies
The project requires several python packages.

pip install PySide6

pip install sounddevice

pip install soundfile

pip install scipy

pip install matplotlib


# TODO
The project is in a usable state but has some unimplemented features & improvements that could be made.
Since these things are not a high priority for me to use this software it will likely be some time before I implement them.
1) Display mode over network.
2) Server mode for display.
3) Play button 2 causes error if clicked and no recording.
4) Input sanitization & correction.
5) Save audio stream directly to a file. (e.g. unlimited record time)
6) Rework UI to play nice with QThread.
7) Implement Record Button 1.
8) Restructure code so preferences are contained in an object, separate classes into different files.
   (The code is a bit messy)
9) Verify/Test avalible audio setting options, particularly dtype when using sd
10) Anchor UI elements to window for resizing. Verify size of rendered wav forms to fit window.
11) Delay when clicking record2 button. Test on different OS's to see if it is a system issue.

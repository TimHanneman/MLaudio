#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 11 13:49:40 2022

@author: tim
"""
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog
from PySide6.QtCore import Signal, Qt, Slot
from ui_MLaudio import Ui_MainWindow
from ui_Preference import Ui_Dialog
from ui_AudioSettings import Ui_Dialog_Aud

import pyaudio
import wave

#Settings Variables#
## Preferences ##
line_num = 0
base_file_name = "audio"
save_location = "./"
transcript_file = "False"
audio_clips = "False"
mode = "local" #Local, Server, Display
    #Network Settings#
current_ip = "127.0.0.1"
srv_prt = 8080
remote_ip = "127.0.0.1"
remote_prt = 8080

## Audio Settings ##
input_src = 0
output_src = 0 #
hz = 44100
bits = 32
channels = 1

currently_write_filename = base_file_name + str(line_num)




class MLaudio(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.ui.actionPreferences.triggered.connect(self.preference)
        ###self.ui.Next_btn.clicked.connect(self.preference)
        self.ui.actionAudio_Settings.triggered.connect(self.audio_set)
        
        
        
    #open the audio setting dialog
    @Slot()
    def audio_set(self):
        aud = AudioDialog()
        aud.exec()
        print(bits)
        print(channels)
        print(hz)

        
    #open the other preference menu
    @Slot()
    def preference(self):
        
        pref = PreferencesDialog()
        pref.exec()
    
    #open the documentation?
    def Manual():
        pass
    
    #If the transcript is set, and the line number is changed
    def line_num_update():
        pass
    
    def play():
        pass
    
    def stop():
        pass
    
    def record():
        pass
    
    def play2():
        pass
    
    def stop2():
        pass
    
    def record2():
        pass
    
    def next_samp():
        pass
    
#Classes below are specifically to generate dialogs for changing the settings.

class PreferencesDialog(QDialog):
    
    Pmode = "local" #Local, Server, Display

    Pbase_file_name = "audio"
    Psave_location = "./"
    Ptranscript_file = "False"
    Paudio_clips = "False"
    Pline_num = 0
    

    Pcurrent_ip = "127.0.0.1"
    Psrv_prt = 8080
    
    Premote_ip = "127.0.0.1"
    Premote_prt = 8080
    
    
    def __init__(self):
        super().__init__()
        
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        #self.ui.radioButton_3.setHidden(True)
    
    def set_Premote_prt(rprt):
        pass
    
    def set_Premote_ip(rip):
        pass
    
    def set_Psrv_prt(sprt):
        pass
        
    def set_Pcurrent_ip(pip):
        pass
        
    def set_Pline_num(n):
        pass
        
    def set_Paudio_clips(aud):
        pass
        
    def set_P_transcript_file(tra):
        pass
        
    def set_P_save_location(loc):
        pass
        
    def set_Pbase_file_name(na):
        pass
        
    def set_Pmode(m):
        pass
    
    def save_cur_conf():
        pass
        
    def apply_pref():
        pass


class AudioDialog(QDialog):
    'Each Audio setting only set after clicking the okay button.'
    Dinput_src = 0
    Doutput_src = 0
    Dhz = 44100
    Dbits = 32
    Dchannels = 1
    
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog_Aud()
        self.ui.setupUi(self)
        
        #Send a function reference to the slot to pass both the signal and additional parameters
        self.ui.comboBox.currentIndexChanged.connect(lambda: self.setDhz(self.ui.comboBox.currentIndex()))
        self.ui.comboBox_2.currentIndexChanged.connect(lambda: self.setDChannels(self.ui.comboBox.currentIndex()))
        self.ui.comboBox_3.currentIndexChanged.connect(lambda: self.setDbits(self.ui.comboBox_3.currentIndex()))
        self.ui.pushButton.clicked.connect(lambda: self.applyAudSet(self.Dinput_src,self.Doutput_src,self.Dhz,self.Dbits,self.Dchannels))
    
    @Slot()
    def setDChannels(self,n):
        #Index is n, but channels are what needs to be assigned
        if n == 0:
            self.Dchannels = 1
        else:
            self.Dchannels = 2
    
    @Slot()
    def setDbits(self,n):
        if n == 0:
            self.Dbits = 16
        elif n == 1:
            self.Dbits = 24
        else :
            self.Dbits = 32

    @Slot()
    def setDhz(self,n):
        if n == 0:
            self.Dhz = 8000
        elif n == 1:
            self.Dhz = 11025
        elif n == 2:
            self.Dhz = 16000
        elif n == 3:
            self.Dhz = 22050
        elif n == 4:
            self.Dhz = 32000
        elif n == 5:
            self.Dhz = 44100
        elif n == 6:
            self.Dhz = 48000
        elif n == 7:
            self.Dhz = 88200
        elif n == 8:
            self.Dhz = 96000
        elif n == 9:
            self.Dhz = 176400
        elif n == 10:
            self.Dhz = 192000
        elif n == 11:
            self.Dhz = 352800
        elif n == 12:
            self.Dhz = 384000

    @Slot()
    def applyAudSet(self, Dinput_src, Doutput_src, Dhz,Dbits,Dchannels):
        
        global input_src
        global output_src
        global hz
        global bits
        global channels
        
        input_src = self.Dinput_src
        output_src = self.Doutput_src
        hz = self.Dhz
        bits = self.Dbits
        channels = self.Dchannels

        
        
            
    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MLaudio()
    window.show()
    sys.exit(app.exec())
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 11 13:49:40 2022

@author: tim
"""
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog, QFileDialog, QWidget
from PySide6.QtCore import Signal, Qt, Slot
from ui_MLaudio import Ui_MainWindow
from ui_Preference import Ui_Dialog
from ui_AudioSettings import Ui_Dialog_Aud

import sys, os, atexit


import pyaudio
import wave

#Settings Variables#
## Preferences ##
#If I was smart before coding all of this I would have made a settings class
#and just have used a single object for this.

cwd = os.getcwd()

line_num = 0
base_file_name = "audio"
save_location = "./"
transcript_file = "False"
audio_clips = "False"
mode = "Local" #Local, Server, Display
    #Network Settings#
current_ip = "127.0.0.1"
srv_prt = 8080
remote_ip = "127.0.0.1"
remote_prt = 8080

## Audio Settings ##
filename1 = ""
filename2 = ""
input_src = 0
output_src = 0 #
hz = 44100
bits = 32
channels = 1

currently_write_filename = base_file_name + str(line_num)


def set_cwd(new_dir):
    try:
        os.chdir(new_dir)
        cwd = os.getcwd()
    except:
        print('failed to change current working directory')

class MLaudio(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.update()
        self.ui.actionPreferences.triggered.connect(lambda: self.preference(mode, base_file_name, save_location, transcript_file, audio_clips, line_num, current_ip, srv_prt, remote_ip, remote_prt))
        ###self.ui.Next_btn.clicked.connect(self.preference)
        self.ui.actionAudio_Settings.triggered.connect(self.audio_set)
        
        self.ui.lineEdit.editingFinished.connect(lambda: self.line_num_update(self.ui.lineEdit.text()))
        self.ui.Play1.clicked.connect(self.play)
        
        
        
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
    def preference(self,mode, base_file_name, save_location, transcript_file, audio_clips, line_num, current_ip, srv_prt, remote_ip, remote_prt):
        
        pref = PreferencesDialog(mode, base_file_name, save_location, transcript_file, audio_clips, line_num, current_ip, srv_prt, remote_ip, remote_prt)
        pref.exec()
        self.update()
    
    #open the documentation?
    def Manual():
        pass
    
    #If the transcript is set, and the line number is changed
    def line_num_update(self, nn):
        global line_num
        line_num = int(nn)
        if nn == "":
            line_num = 0
        self.ui.lineEdit.setText(str(nn))
        self.ui.lineEdit_filename.setText(base_file_name+str(line_num))
    
    @Slot()
    def play(self):
        
        global filename1
        
        if filename1 != "":
            chunk = 1024
            aud1 = wave.open(filename1, 'rb')
            pa = pyaudio.PyAudio()
            stream = pa.open(format = pa.get_format_from_width(aud1.getsampwidth()),
                         channels = aud1.getnchannels(),
                         rate = aud1.getframerate(),
                         output = True)
            rd_data = aud1.readframes(chunk)
        
            while rd_data != '':
                stream.write(rd_data)
                rd_data = aud1.readframes(chunk)
        
            stream.stop_stream()
            stream.close()
            pa.terminate()
        else:
            print("No filename1 audio file")
    
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
    
    def update(self):
        
        global audio_clips
        global filename1
        
        self.ui.lineEdit_filename.setText(base_file_name+str(line_num))
        self.ui.lineEdit.setText(str(line_num))
        self.ui.Mode_Lb.setText("Mode: "+mode)
        
        '''if save location is set then retrive a list of filenames from that directory'''
        '''Assign the nth filename in the audio_clips folder to filename1'''
        if audio_clips != "False":
            
            try:
                dir_list = os.listdir(audio_clips)
                filename1 = audio_clips + "/" + dir_list[line_num]
                print(filename1)
            except:
                print("setting filename1 failed")
                filename1 = ""
                audio_clips = "False"
        else:
            filename1 = ""
            dir_list = ""
    
#Classes below are specifically to generate dialogs for changing the settings.

#The classes need to accept inputs into their constructor.
class PreferencesDialog(QDialog):
    
    def __init__(self, o_mode, obase_file_name, osave_location, otranscript_file, oaudio_clips, opline_num, ocurrent_ip, osrv_prt, oremote_ip, oremote_prt):
        super().__init__()
        
        #Variable Init
        self.Pmode = o_mode

        self.Pbase_file_name = obase_file_name
        self.Psave_location = osave_location
        self.Ptranscript_file = otranscript_file
        self.Paudio_clips = oaudio_clips
        self.Pline_num = opline_num
        

        self.Pcurrent_ip = ocurrent_ip
        self.Psrv_prt = osrv_prt
        
        self.Premote_ip = oremote_ip
        self.Premote_prt = oremote_prt
       
        
        #Ui init & wiring
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        
        self.cur_Pmode(self.Pmode)
        
        #self.ui.radioButton_3.setHidden(True)
        self.ui.radioButton_3.toggled.connect(lambda: self.set_Pmode(1))
        self.ui.radioButton_4.toggled.connect(lambda: self.set_Pmode(2))
        self.ui.radioButton_5.toggled.connect(lambda: self.set_Pmode(3))
        
        self.ui.checkBox_filena.stateChanged.connect(lambda: self.set_Pbase_file_name(self.ui.checkBox_filena.isChecked()))
        self.ui.txt_filena.editingFinished.connect(lambda: self.set_cus_Pbase_file_name(self.ui.txt_filena.text()))
        self.ui.txt_SavLoc.editingFinished.connect(lambda: self.set_P_save_location(self.ui.txt_SavLoc.text()))
        
        self.ui.checkBox_trns.stateChanged.connect(lambda: self.set_P_transcript_file(self.ui.checkBox_trns.isChecked()))
        self.ui.txt_AudClip.editingFinished.connect(lambda: self.set_Paudio_clips(self.ui.txt_AudClip.text()))
        self.ui.txt_linNum.editingFinished.connect(lambda: self.set_Pline_num(self.ui.txt_linNum.text()))
        
        self.ui.txt_SrvIP.editingFinished.connect(lambda: self.set_Pcurrent_ip(self.ui.txt_SrvIP.text()))
        self.ui.txt_SrvPrt.editingFinished.connect(lambda: self.set_Psrv_prt(self.ui.txt_SrvPrt.text()))
        self.ui.txt_remote_ip.editingFinished.connect(lambda: self.set_Premote_ip(self.ui.txt_remote_ip.text()))
        self.ui.txt_remote_prt.editingFinished.connect(lambda: self.set_Premote_prt(self.ui.txt_remote_prt.text()))
    
        self.ui.connect_btn.clicked.connect(self.chk_Connect)
        self.ui.pushButton_2.clicked.connect(self.save_cur_conf)
        self.ui.df_config_btn.accepted.connect(lambda: self.apply_pref(self.Pmode, self.Pbase_file_name, self.Psave_location, self.Ptranscript_file, self.Paudio_clips, self.Pline_num, self.Pcurrent_ip, self.Psrv_prt, self.Premote_ip, self.Premote_prt))
        
    #### When Networking is implemented update this to check connection
    @Slot()
    def chk_Connect(self):
        print("CHECKING!")
        
    ##### Check that the input is a valid port number.
    @Slot()
    def set_Premote_prt(self,rprt):
        self.Premote_prt = rprt
        if rprt == "":
            self.Premote_prt == 8080
        print(self.Premote_prt)
    
    ##### When the mode changes be sure to clear the settings out.
    ##### Check that it has a valid IP address
    @Slot()
    def set_Premote_ip(self,rip):
        self.Premote_ip = rip
        if rip == "":
            self.Premote_ip = "127.0.0.1"
        print(self.Premote_ip)
    
    ##### Check that the input is a valid port number.
    @Slot()
    def set_Psrv_prt(self,sprt):
        self.Psrv_prt = sprt
        if sprt == "":
            self.Psrv_prt = 8080
        print(self.Psrv_prt)
        
    ##### When the mode changes be sure to clear the settings out.
    ##### Check that it has a valid IP address
    @Slot()
    def set_Pcurrent_ip(self,pip):
        self.Pcurrent_ip = pip
        if pip == "":
            self.Pcurrent_ip = "127.0.0.1"
        print(self.Pcurrent_ip)
        
    ##### Check that n is a number / restrict it to only numbers or empty.
    @Slot()
    def set_Pline_num(self,n):
        self.Pline_num = n
        if n == "":
            self.Pline_num = 0
        print(self.Pline_num)
    
    ##### What happens if the string is an invalid path?
    @Slot()
    def set_Paudio_clips(self,aud):
        self.Paudio_clips = aud
        if aud == "":
            self.Paudio_clips = "False"
        print(self.Paudio_clips)
        
    ##### What happens if no file is selected?
    @Slot()
    def set_P_transcript_file(self,tra):
        if tra == True:
            w = QWidget()
            w.resize(320,240)
            w.setWindowTitle("Select Transcript File")
            self.Ptranscript_file = QFileDialog.getOpenFileName(w, 'Open File', '/')            
        else:
            self.Ptranscript_file = ""
        print(self.Ptranscript_file)
    
    ##### What happens if the string is an invalid path?
    @Slot()
    def set_P_save_location(self,loc):
        self.Psave_location = loc
        if loc == "":
            self.Psave_location = "/"
        print(self.Psave_location)
        
    def set_Pbase_file_name(self, na):
        if na == True:
            self.Pbase_file_name = ""
            self.ui.txt_filena.setText(self.Pbase_file_name)

        elif na == False:
            self.Pbase_file_name = "audio"
            self.ui.txt_filena.setText(self.Pbase_file_name)
        print(self.Pbase_file_name)
    
    @Slot()
    def set_cus_Pbase_file_name(self,na):
        self.Pbase_file_name = na
        
    #The idea is to set all the settings that are unaccessible to non-error state defaults.     #####Might need to change these after further development such as the IP settings
    @Slot()
    def set_Pmode(self,m):
        print("M is"+ str(m))
        if m == 1:
            self.Pmode = "Local"
            self.Premote_ip = "127.0.0.1"
            self.Premote_prt = 8080
            self.Pcurrent_ip = "127.0.0.1"
            self.Psrv_prt = 8080
            
        elif m == 2:
            self.Pmode = "Server"
            self.Premote_ip = "127.0.0.1"
            self.Premote_prt = 8080

        else:
            self.Pmode = "Display"
            self.Pbase_file_name = "temp"
            self.Psave_location = "./temp"
            self.Ptranscript_file = "./temp/transcript"
            self.Paudio_clips = "./temp/Paudio"
            self.Pline_num = 0
            
            self.Pcurrent_ip = "127.0.0.1"
            self.Psrv_prt = 8080
    
    def cur_Pmode(self,m):
        if m == "Local":
            self.ui.radioButton_3.setChecked(True)
        elif m == "Server":
            self.ui.radioButton_4.setChecked(True)
        elif m == "Display":
            self.ui.radioButton_5.setChecked(True)
    
    ##### Write the configuration to a file that can be loaded???
    @Slot()
    def save_cur_conf(self):
        print("not implemented")
        
    @Slot()
    def apply_pref(self, Pmode, Pbase_file_name, Psave_location,Ptranscript_file, Paudio_clips, Pline_num, Pcurrent_ip, Psrv_prt, Premote_ip, Premote_prt):
        print("applied")
        global base_file_name
        global save_location
        global transcript_file
        global audio_clips
        global line_num
        global current_ip
        global srv_prt
        global remote_ip
        global remote_prt
        global mode
        
        base_file_name = self.Pbase_file_name
        save_location = self.Psave_location
        transcript_file = self.Ptranscript_file
        audio_clips = self.Paudio_clips
        line_num = self.Pline_num
        current_ip = self.Pcurrent_ip
        srv_prt = self.Psrv_prt
        remote_ip = self.Premote_ip
        remote_prt = self.Premote_prt
        mode = self.Pmode


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
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 11 13:49:40 2022
Not gonna lie this code is a mess, but it gets the job done.
@author: tim
"""
import sys
from PySide6.QtWidgets import (QApplication, QMainWindow, QDialog, QFileDialog, QWidget,
                               QLabel, QComboBox, QVBoxLayout)
from PySide6.QtCore import Signal, Qt, Slot
from ui_MLaudio import Ui_MainWindow
from ui_Preference import Ui_Dialog
from ui_AudioSettings import Ui_Dialog_Aud

import sys, os, atexit, time
import threading


import sounddevice as sd
import soundfile as sf
from scipy.io.wavfile import write

#Settings Variables#
## Preferences ##
#TODO If I was smart before coding all of this I would have made a settings class
#and just have used a single object for this.

cwd = os.getcwd()

line_num = 0
base_file_name = "audio"
user1_file_name = "usr1_aud"
save_location = cwd
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
input_src = len(sd.query_devices())-1
output_src = 0 #
hz = 44100
bits = 32
channelz = 1
recording = 0

currently_write_filename = base_file_name + str(line_num)

def current_settings():
    global cwd, line_num,base_file_name,user1_file_name,save_location,transcript_file,audio_clips,mode,current_ip,srv_prt,remote_ip,remote_prt,filename1,filename2,input_src,output_src,hz,bits,channelz,recording
    print("--------------------------------called------------------------------------")
    print("cwd, line_num,base_file_name,user1_file_name,save_location,transcript_file,audio_clips,mode,current_ip,srv_prt,remote_ip,remote_prt,filename1,filename2,input_src,output_src,hz,bits,channelz,recording")
    print(f'{cwd}, {line_num},{base_file_name},{user1_file_name},{save_location},{transcript_file},{audio_clips},{mode,current_ip},{srv_prt},{remote_ip},{remote_prt},{filename1},{filename2},{input_src},{output_src},{hz},{bits},{channelz},{recording}')
    print("---")   

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
        self.ui.actionAudio_Settings.triggered.connect(lambda: self.audio_set(input_src, output_src, hz, bits, channelz))
        
        self.ui.lineEdit.editingFinished.connect(lambda: self.line_num_update(self.ui.lineEdit.text()))
        self.ui.Play1.clicked.connect(lambda: self.play(filename1))
        #self.ui.Play1.clicked.connect(lambda: self.playt(filename1))
        self.ui.Stop1.clicked.connect(self.stop)
        self.ui.lineEdit_filename_target.setEnabled(False)
        self.ui.Record2.clicked.connect(self.record2)
        self.ui.Next_btn.clicked.connect(self.next_samp)
        self.ui.pushButton.clicked.connect(self.back_samp)
        self.ui.Stop2.clicked.connect(self.stop2)
        self.ui.Play2.clicked.connect(self.play2)
        
    def current_settings():AllowNestedDocks


    #open the audio setting dialog self, in_src, out_src, hzz, bitz, chan
    @Slot()
    def audio_set(self, input_src, output_src, hz, bits, channelz):
        print("channelz " + str(channelz))
        aud = AudioDialog(input_src, output_src, hz, bits, channelz)
        aud.exec()
        self.update()
        #current_settings()

    #open the other preference menu
    @Slot()
    def preference(self,mode, base_file_name, save_location, transcript_file, audio_clips, line_num, current_ip, srv_prt, remote_ip, remote_prt):
        
        pref = PreferencesDialog(mode, base_file_name, save_location, transcript_file, audio_clips, line_num, current_ip, srv_prt, remote_ip, remote_prt)
        pref.exec()
        self.update()
        #current_settings()
    
    #open the documentation?
    def Manual():
        pass
    
    #If the transcript is set, and the line number is changed
    def line_num_update(self, nn):
        global line_num
        global currently_write_filename
        line_num = int(nn)
        if nn == "":
            line_num = 0
        self.ui.lineEdit.setText(str(nn))
        self.ui.lineEdit_filename.setText(base_file_name+str(line_num))
        self.update()
        currently_write_filename = base_file_name + str(line_num)
    
    #TODO It seems like I should allow the play button to be clicked only once and stop button clicked only once.
    #       I'm guessing that the audio package is not thread safe. One way I could implement this is by having only 1 button. if playing then it stops the audio.
    @Slot()
    def play(self, filename):
        t1 = threading.Thread(target=self.playt, args=(filename,),daemon=True)
        t1.start()
        print("thread end?")

            
    def playt(self, filename):
        #TODO probably need to detect dtype
        if filename1 != "":
            #sd.stop()
            array, smp_rt = sf.read(filename1, dtype = 'float32')
            sd.play(array,smp_rt)
            #Telling it to wait and running multiple thread will cause crash
            #status = sd.wait()
            #sd.stop()
        else:
            print("No filename1 audio file")
            
    @Slot()
    def stop(self):
        t2 = threading.Thread(target=self.stopt, args=(),daemon=True)
        t2.start()
        #t2.join()
        
    def stopt(self):
        try:
            sd.stop()
            print("stopped")
        except:
            "no audio playing, or error"
    #TODO
    # If there is an audio clips folder save recording to that folder.
    # It should find the last listed file in the folder use that name, and append a number to it?
    @Slot()
    def record(self):
        self.ui.Play1.setEnabled(False)
        self.ui.Stop2.setEnabled(False)
        self.ui.Record2.setEnabled(False)
        self.ui.Play2.setEnabled(False)
        
        
        self.ui.Play1.setEnabled(True)
        self.ui.Stop2.setEnabled(True)
        self.ui.Record2.setEnabled(True)
        self.ui.Play2.setEnabled(True)
        print('done recording')
        
    #TODO
    @Slot()
    def play2(self):
        t5 = threading.Thread(target=self.play2t, args=(),daemon=True)
        t5.start()
    
    def play2t(self):
        global recording
        print('uh')
        print(type(recording))
        sd.play(recording,hz)
    
    #TODO check and see what happens when stop is hit mid recording.
    def stop2(self):
        try:
            sd.stop()
            print("stopped")
        except:
            "no audio playing, or error"
    
    #TODO Figure out a way of defining the duration to record. Probably the amount of time of the other sample plus 2 seconds?
    #Alternatively and better end it with the stop button. #Stop cuts the recording, but not the total file size.
    @Slot()
    def record2(self):
        self.ui.Play1.setDisabled(True)
        self.ui.Stop1.setDisabled(True)
        self.ui.Record1.setDisabled(True)
        self.ui.Record2.setDisabled(True)
        self.ui.Play2.setDisabled(True)
        t3 = threading.Thread(target=self.record2t, args=(),daemon=True)
        t3.start()
        
    def record2t(self):
        print('entered rec2')        
        global recording        
        global hz
        global channelz
        
        duration = 3.5
        recording = sd.rec(int(duration * hz), samplerate = hz, channels = channelz)
        #sd.wait()
        #This is not for thread control, but to delay the re-enable of ui
        time.sleep(duration)
        self.ui.Play1.setDisabled(False)
        self.ui.Stop1.setDisabled(False)
        self.ui.Record1.setDisabled(False)
        self.ui.Record2.setDisabled(False)
        self.ui.Play2.setDisabled(False)
        print('done recording')
        
    #TODO
    @Slot()
    def next_samp(self):
        global hz
        global currently_write_filename
        global save_location
        global recording
        global line_num
        if type(recording) != type(0):
            print(type(recording))
            write(save_location +"/" + currently_write_filename, hz, recording)
        self.line_num_update(line_num+1)
        recording = 0
        
    #TODO
    @Slot()
    def back_samp(self):
        global line_num
        global currently_write_filename
        line_num = line_num - 1
        if line_num < 0:
            line_num = 0
        self.ui.lineEdit.setText(str(line_num))
        self.ui.lineEdit_filename.setText(base_file_name+str(line_num))
        self.update()
        currently_write_filename = base_file_name + str(line_num)
        
    #TODO
    def update(self):
        
        global audio_clips
        global filename1
        
        self.ui.lineEdit_filename.setText(base_file_name+str(line_num))
        self.ui.lineEdit.setText(str(line_num))
        self.ui.Mode_Lb.setText("Mode: "+mode)
        
        '''if save location is set then retrive a list of filenames from that directory'''
        '''Assign the nth filename in the audio_clips folder to filename1'''
        #If directory is empty then use default name for recording.
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
            self.ui.Record1.setEnabled(True)
            self.ui.lineEdit_filename_target.setText(user1_file_name+str(line_num)+".wav")
            
            
            
    def closeEvent(self, event):
        print("user has clicked the red x")
        event.accept()
    
#Classes below are specifically to generate dialogs for changing the settings.
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
        
        #current_settings()
        
    #### When Networking is implemented update this to check connection
    #TODO
    @Slot()
    def chk_Connect(self):
        print("CHECKING!")
        
    ##### Check that the input is a valid port number.
    #TODO
    @Slot()
    def set_Premote_prt(self,rprt):
        self.Premote_prt = rprt
        if rprt == "":
            self.Premote_prt == 8080
        print(self.Premote_prt)
    
    ##### When the mode changes be sure to clear the settings out.
    ##### Check that it has a valid IP address
    #TODO
    @Slot()
    def set_Premote_ip(self,rip):
        self.Premote_ip = rip
        if rip == "":
            self.Premote_ip = "127.0.0.1"
        print(self.Premote_ip)
    
    ##### Check that the input is a valid port number.
    #TODO
    @Slot()
    def set_Psrv_prt(self,sprt):
        self.Psrv_prt = sprt
        if sprt == "":
            self.Psrv_prt = 8080
        print(self.Psrv_prt)
        
    ##### When the mode changes be sure to clear the settings out.
    ##### Check that it has a valid IP address
    #TODO
    @Slot()
    def set_Pcurrent_ip(self,pip):
        self.Pcurrent_ip = pip
        if pip == "":
            self.Pcurrent_ip = "127.0.0.1"
        print(self.Pcurrent_ip)
        
    ##### Check that n is a number / restrict it to only numbers or empty.
    #TODO
    @Slot()
    def set_Pline_num(self,n):
        self.Pline_num = n
        if n == "":
            self.Pline_num = 0
        print(self.Pline_num)
    
    ##### What happens if the string is an invalid path?
    #TODO
    @Slot()
    def set_Paudio_clips(self,aud):
        self.Paudio_clips = aud
        if aud == "":
            self.Paudio_clips = "False"
        print(self.Paudio_clips)
        
    ##### What happens if no file is selected?
    #TODO
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
    #TODO
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
    #TODO
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

    
    def __init__(self, in_src, out_src, hzz, bitz, chan):
        super().__init__()
        
        self.Dinput_src = in_src
        self.Doutput_src = out_src
        self.Dhz = hzz
        self.Dbits = bitz
        self.Dchannels = chan
        
        self.ui = Ui_Dialog_Aud()
        self.ui.setupUi(self)
        
        #Channels, Bit Depth, Hz, Device
        self.ui.comboBox_2.setCurrentIndex(self.Dchannels-1)
        #Formula converts between bits and index
        self.ui.comboBox_3.setCurrentIndex(self.Dbits/8-2)
        self.set_hz_cur_idx(self.Dhz)
        self.ui.comboBox_4.setCurrentIndex(self.Dinput_src)
        #current_settings()
        
        #Send a function reference to the slot to pass both the signal and additional parameters
        self.ui.comboBox.currentIndexChanged.connect(lambda: self.setDhz(self.ui.comboBox.currentIndex()))
        self.ui.comboBox_2.currentIndexChanged.connect(lambda: self.setDChannels(self.ui.comboBox_2.currentIndex()))
        self.ui.comboBox_3.currentIndexChanged.connect(lambda: self.setDbits(self.ui.comboBox_3.currentIndex()))
        self.ui.pushButton.clicked.connect(lambda: self.applyAudSet(self.Dinput_src,self.Doutput_src,self.Dhz,self.Dbits,self.Dchannels))
        #self.ui.comboBox_4.currentIndexChanged.connect(lambda: self.setDev(self.ui.comboBox_4.currentText()))
        self.ui.comboBox_4.currentIndexChanged.connect(lambda: self.setDev(self.ui.comboBox_4.currentIndex()))

    def set_hz_cur_idx(self, Dhz):
        if Dhz == 8000:
            self.ui.comboBox.setCurrentIndex(0)
        elif Dhz ==11025:
            self.ui.comboBox.setCurrentIndex(1)
        elif Dhz ==16000:
            self.ui.comboBox.setCurrentIndex(2)
        elif Dhz ==22050:
            self.ui.comboBox.setCurrentIndex(3)
        elif Dhz ==32000:
            self.ui.comboBox.setCurrentIndex(4)
        elif Dhz ==44100:
            self.ui.comboBox.setCurrentIndex(5)
        elif Dhz ==48000:
            self.ui.comboBox.setCurrentIndex(6)
        elif Dhz ==88200:
            self.ui.comboBox.setCurrentIndex(7)
        elif Dhz ==96000:
            self.ui.comboBox.setCurrentIndex(8)
        elif Dhz ==176400:
            self.ui.comboBox.setCurrentIndex(9)
        elif Dhz ==192000:
            self.ui.comboBox.setCurrentIndex(10)
        elif Dhz ==352800:
            self.ui.comboBox.setCurrentIndex(11)
        elif Dhz ==384000:
            self.ui.comboBox.setCurrentIndex(12)
    
    @Slot()
    def setDev(self, d):
        self.Dinput_src = d
    
    @Slot()
    def setDChannels(self,n):
        #Indexes are different than num of channels
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
        else:
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
        global channelz
        
        input_src = self.Dinput_src
        output_src = self.Doutput_src
        hz = self.Dhz
        bits = self.Dbits
        channelz = self.Dchannels

if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    window = MLaudio()
    window.show()
    sys.exit(app.exec())
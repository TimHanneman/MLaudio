# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Preferences.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QCheckBox, QDialog,
    QDialogButtonBox, QFrame, QGroupBox, QLabel,
    QLineEdit, QPushButton, QRadioButton, QSizePolicy,
    QVBoxLayout, QWidget)
import icons_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(643, 481)
        self.df_config_btn = QDialogButtonBox(Dialog)
        self.df_config_btn.setObjectName(u"df_config_btn")
        self.df_config_btn.setGeometry(QRect(450, 440, 181, 32))
        self.df_config_btn.setOrientation(Qt.Horizontal)
        self.df_config_btn.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 20, 57, 16))
        self.verticalLayoutWidget = QWidget(Dialog)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 40, 161, 392))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.radioButton_3 = QRadioButton(self.verticalLayoutWidget)
        self.radioButton_3.setObjectName(u"radioButton_3")
        self.radioButton_3.setEnabled(True)
        self.radioButton_3.setStyleSheet(u"::indicator::unchecked{image: url(:/Local_grey.png);}\n"
"::indicator::checked{image: url(:/Local.png);}")
        self.radioButton_3.setIconSize(QSize(100, 100))
        self.radioButton_3.setChecked(True)

        self.verticalLayout.addWidget(self.radioButton_3)

        self.label_3 = QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)

        self.radioButton_4 = QRadioButton(self.verticalLayoutWidget)
        self.radioButton_4.setObjectName(u"radioButton_4")
        self.radioButton_4.setEnabled(True)
        self.radioButton_4.setStyleSheet(u"::indicator::unchecked{image: url(:/Server_grey.png);}\n"
"::indicator::checked{image:url(:/Server.png);}")
        self.radioButton_4.setIconSize(QSize(100, 100))

        self.verticalLayout.addWidget(self.radioButton_4)

        self.label_4 = QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout.addWidget(self.label_4)

        self.radioButton_5 = QRadioButton(self.verticalLayoutWidget)
        self.radioButton_5.setObjectName(u"radioButton_5")
        self.radioButton_5.setEnabled(True)
        self.radioButton_5.setStyleSheet(u"::indicator::unchecked{image: url(:/Display_grey.png);}\n"
"::indicator::checked{image: url(:/Display.png)}")
        self.radioButton_5.setIconSize(QSize(100, 100))

        self.verticalLayout.addWidget(self.radioButton_5)

        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(180, 40, 461, 261))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.txt_filena = QLineEdit(self.frame)
        self.txt_filena.setObjectName(u"txt_filena")
        self.txt_filena.setGeometry(QRect(110, 20, 331, 22))
        self.txt_SavLoc = QLineEdit(self.frame)
        self.txt_SavLoc.setObjectName(u"txt_SavLoc")
        self.txt_SavLoc.setGeometry(QRect(110, 50, 331, 22))
        self.txt_trns = QLineEdit(self.frame)
        self.txt_trns.setObjectName(u"txt_trns")
        self.txt_trns.setEnabled(False)
        self.txt_trns.setGeometry(QRect(110, 80, 331, 22))
        self.txt_trns.setFocusPolicy(Qt.StrongFocus)
        self.txt_trns.setReadOnly(True)
        self.groupBox = QGroupBox(self.frame)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(300, 170, 151, 80))
        self.radio_cnt = QRadioButton(self.groupBox)
        self.radio_cnt.setObjectName(u"radio_cnt")
        self.radio_cnt.setGeometry(QRect(10, 40, 99, 20))
        self.radio_cnt.setChecked(True)
        self.txt_linNum = QLineEdit(self.frame)
        self.txt_linNum.setObjectName(u"txt_linNum")
        self.txt_linNum.setGeometry(QRect(210, 140, 41, 22))
        self.label_11 = QLabel(self.frame)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(120, 140, 81, 16))
        self.txt_AudClip = QLineEdit(self.frame)
        self.txt_AudClip.setObjectName(u"txt_AudClip")
        self.txt_AudClip.setEnabled(True)
        self.txt_AudClip.setGeometry(QRect(110, 110, 331, 22))
        self.txt_AudClip.setReadOnly(False)
        self.checkBox_trns = QCheckBox(self.frame)
        self.checkBox_trns.setObjectName(u"checkBox_trns")
        self.checkBox_trns.setGeometry(QRect(0, 80, 101, 20))
        self.checkBox_filena = QCheckBox(self.frame)
        self.checkBox_filena.setObjectName(u"checkBox_filena")
        self.checkBox_filena.setGeometry(QRect(0, 20, 111, 20))
        font = QFont()
        font.setPointSize(8)
        self.checkBox_filena.setFont(font)
        self.checkBox_filena.setChecked(True)
        self.txt_SrvIP = QLineEdit(self.frame)
        self.txt_SrvIP.setObjectName(u"txt_SrvIP")
        self.txt_SrvIP.setEnabled(False)
        self.txt_SrvIP.setGeometry(QRect(10, 190, 113, 22))
        self.txt_SrvIP.setReadOnly(False)
        self.txt_SrvPrt = QLineEdit(self.frame)
        self.txt_SrvPrt.setObjectName(u"txt_SrvPrt")
        self.txt_SrvPrt.setEnabled(False)
        self.txt_SrvPrt.setGeometry(QRect(90, 220, 41, 22))
        self.txt_SrvPrt.setReadOnly(False)
        self.label_7 = QLabel(self.frame)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(10, 160, 57, 14))
        self.label_8 = QLabel(self.frame)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(10, 220, 71, 16))
        self.label_9 = QLabel(self.frame)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(20, 50, 91, 16))
        self.label_10 = QLabel(self.frame)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(30, 110, 81, 20))
        self.groupBox_2 = QGroupBox(self.frame)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(160, 170, 121, 81))
        self.radioButton = QRadioButton(self.groupBox_2)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setGeometry(QRect(10, 20, 99, 20))
        self.radioButton_2 = QRadioButton(self.groupBox_2)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setGeometry(QRect(10, 40, 99, 20))
        self.radioButton_6 = QRadioButton(self.groupBox_2)
        self.radioButton_6.setObjectName(u"radioButton_6")
        self.radioButton_6.setGeometry(QRect(10, 60, 99, 20))
        self.radioButton_6.setChecked(True)
        self.pushButton_2 = QPushButton(Dialog)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(180, 440, 151, 22))
        self.frame_2 = QFrame(Dialog)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(180, 340, 451, 80))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.label_5 = QLabel(self.frame_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(0, 10, 61, 16))
        self.txt_remote_ip = QLineEdit(self.frame_2)
        self.txt_remote_ip.setObjectName(u"txt_remote_ip")
        self.txt_remote_ip.setEnabled(False)
        self.txt_remote_ip.setGeometry(QRect(70, 10, 113, 22))
        self.txt_remote_ip.setReadOnly(False)
        self.label_6 = QLabel(self.frame_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(190, 10, 57, 14))
        self.txt_remote_prt = QLineEdit(self.frame_2)
        self.txt_remote_prt.setObjectName(u"txt_remote_prt")
        self.txt_remote_prt.setEnabled(False)
        self.txt_remote_prt.setGeometry(QRect(220, 10, 31, 22))
        self.connect_btn = QPushButton(self.frame_2)
        self.connect_btn.setObjectName(u"connect_btn")
        self.connect_btn.setEnabled(False)
        self.connect_btn.setGeometry(QRect(320, 30, 80, 22))
        self.label_connection = QLabel(self.frame_2)
        self.label_connection.setObjectName(u"label_connection")
        self.label_connection.setGeometry(QRect(80, 50, 131, 16))
        QWidget.setTabOrder(self.checkBox_filena, self.txt_filena)
        QWidget.setTabOrder(self.txt_filena, self.txt_SavLoc)
        QWidget.setTabOrder(self.txt_SavLoc, self.checkBox_trns)
        QWidget.setTabOrder(self.checkBox_trns, self.txt_trns)
        QWidget.setTabOrder(self.txt_trns, self.txt_AudClip)
        QWidget.setTabOrder(self.txt_AudClip, self.txt_SrvIP)
        QWidget.setTabOrder(self.txt_SrvIP, self.txt_SrvPrt)
        QWidget.setTabOrder(self.txt_SrvPrt, self.txt_linNum)
        QWidget.setTabOrder(self.txt_linNum, self.radio_cnt)
        QWidget.setTabOrder(self.radio_cnt, self.txt_remote_ip)
        QWidget.setTabOrder(self.txt_remote_ip, self.txt_remote_prt)
        QWidget.setTabOrder(self.txt_remote_prt, self.connect_btn)
        QWidget.setTabOrder(self.connect_btn, self.pushButton_2)

        self.retranslateUi(Dialog)
        self.checkBox_filena.clicked["bool"].connect(self.txt_filena.setEnabled)
        self.checkBox_trns.toggled.connect(self.txt_trns.setEnabled)
        self.df_config_btn.rejected.connect(Dialog.reject)
        self.df_config_btn.accepted.connect(Dialog.accept)
        self.radioButton_5.toggled.connect(self.checkBox_filena.setDisabled)
        self.radioButton_5.toggled.connect(self.txt_filena.setDisabled)
        self.radioButton_5.toggled.connect(self.txt_SavLoc.setDisabled)
        self.radioButton_5.toggled.connect(self.txt_trns.setDisabled)
        self.radioButton_5.toggled.connect(self.checkBox_trns.setDisabled)
        self.radioButton_5.toggled.connect(self.txt_AudClip.setDisabled)
        self.radioButton_5.toggled.connect(self.txt_linNum.setDisabled)
        self.radioButton_5.toggled.connect(self.radio_cnt.setDisabled)
        self.radioButton_5.toggled.connect(self.txt_remote_ip.setEnabled)
        self.radioButton_5.toggled.connect(self.txt_remote_prt.setEnabled)
        self.radioButton_5.toggled.connect(self.connect_btn.setEnabled)
        self.radioButton_4.toggled.connect(self.txt_SrvIP.setEnabled)
        self.radioButton_4.toggled.connect(self.txt_SrvPrt.setEnabled)
        self.radioButton_5.toggled.connect(self.radioButton.setDisabled)
        self.radioButton_5.toggled.connect(self.radioButton_2.setDisabled)
        self.radioButton_5.toggled.connect(self.radioButton_6.setDisabled)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"MODE:", None))
#if QT_CONFIG(tooltip)
        self.label_2.setToolTip(QCoreApplication.translate("Dialog", u"Local mode will assume the software is only running on this computer.", None))
#endif // QT_CONFIG(tooltip)
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Local", None))
#if QT_CONFIG(tooltip)
        self.radioButton_3.setToolTip(QCoreApplication.translate("Dialog", u"Local mode will assume the software is only running on this computer.", None))
#endif // QT_CONFIG(tooltip)
        self.radioButton_3.setText("")
#if QT_CONFIG(tooltip)
        self.label_3.setToolTip(QCoreApplication.translate("Dialog", u"Server mode allows for a remote connection to view transcript & wave forms.", None))
#endif // QT_CONFIG(tooltip)
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Server", None))
#if QT_CONFIG(tooltip)
        self.radioButton_4.setToolTip(QCoreApplication.translate("Dialog", u"Server mode allows for a remote connection to view transcript & wave forms.", None))
#endif // QT_CONFIG(tooltip)
        self.radioButton_4.setText("")
#if QT_CONFIG(tooltip)
        self.label_4.setToolTip(QCoreApplication.translate("Dialog", u"Display mode only. No ability to record.", None))
#endif // QT_CONFIG(tooltip)
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Display", None))
#if QT_CONFIG(tooltip)
        self.radioButton_5.setToolTip(QCoreApplication.translate("Dialog", u"Display mode only. No ability to record.", None))
#endif // QT_CONFIG(tooltip)
        self.radioButton_5.setText("")
#if QT_CONFIG(tooltip)
        self.txt_filena.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.txt_filena.setInputMask("")
        self.txt_filena.setText(QCoreApplication.translate("Dialog", u"audio", None))
#if QT_CONFIG(tooltip)
        self.txt_SavLoc.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.groupBox.setToolTip(QCoreApplication.translate("Dialog", u"File name options. Unique identifier given to each recording.", None))
#endif // QT_CONFIG(tooltip)
        self.groupBox.setTitle(QCoreApplication.translate("Dialog", u"Filename Options", None))
#if QT_CONFIG(tooltip)
        self.radio_cnt.setToolTip(QCoreApplication.translate("Dialog", u"Start at 1 and increment for the number of recordings made.", None))
#endif // QT_CONFIG(tooltip)
        self.radio_cnt.setText(QCoreApplication.translate("Dialog", u"Count", None))
#if QT_CONFIG(tooltip)
        self.label_11.setToolTip(QCoreApplication.translate("Dialog", u"Count or Transcript Line number to start at.", None))
#endif // QT_CONFIG(tooltip)
        self.label_11.setText(QCoreApplication.translate("Dialog", u"Line Number", None))
#if QT_CONFIG(tooltip)
        self.checkBox_trns.setToolTip(QCoreApplication.translate("Dialog", u"Location of transcript file to show if enabled.", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_trns.setText(QCoreApplication.translate("Dialog", u"Transcript:", None))
#if QT_CONFIG(tooltip)
        self.checkBox_filena.setToolTip(QCoreApplication.translate("Dialog", u"text that will be used to name recordings", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_filena.setText(QCoreApplication.translate("Dialog", u"User2 Filename:", None))
#if QT_CONFIG(tooltip)
        self.label_7.setToolTip(QCoreApplication.translate("Dialog", u"Set computer ip if in server mode.", None))
#endif // QT_CONFIG(tooltip)
        self.label_7.setText(QCoreApplication.translate("Dialog", u"Server IP", None))
#if QT_CONFIG(tooltip)
        self.label_8.setToolTip(QCoreApplication.translate("Dialog", u"Set computer port to listen on if in server mode.", None))
#endif // QT_CONFIG(tooltip)
        self.label_8.setText(QCoreApplication.translate("Dialog", u"Server Port:", None))
#if QT_CONFIG(tooltip)
        self.label_9.setToolTip(QCoreApplication.translate("Dialog", u"Where you want the recordingss saved to", None))
#endif // QT_CONFIG(tooltip)
        self.label_9.setText(QCoreApplication.translate("Dialog", u"Save Location:", None))
        self.label_10.setText(QCoreApplication.translate("Dialog", u"Audio Clips:", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Dialog", u"Audio Clip Sort Type", None))
        self.radioButton.setText(QCoreApplication.translate("Dialog", u"System Sort", None))
        self.radioButton_2.setText(QCoreApplication.translate("Dialog", u"Start of Name", None))
        self.radioButton_6.setText(QCoreApplication.translate("Dialog", u"End of Name", None))
#if QT_CONFIG(tooltip)
        self.pushButton_2.setToolTip(QCoreApplication.translate("Dialog", u"Save these settings for next startup.", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_2.setText(QCoreApplication.translate("Dialog", u"Save Current Config", None))
#if QT_CONFIG(tooltip)
        self.label_5.setToolTip(QCoreApplication.translate("Dialog", u"MLAudio server address", None))
#endif // QT_CONFIG(tooltip)
        self.label_5.setText(QCoreApplication.translate("Dialog", u"Remote IP:", None))
#if QT_CONFIG(tooltip)
        self.label_6.setToolTip(QCoreApplication.translate("Dialog", u"MLaudio server listening port", None))
#endif // QT_CONFIG(tooltip)
        self.label_6.setText(QCoreApplication.translate("Dialog", u"Port", None))
#if QT_CONFIG(tooltip)
        self.connect_btn.setToolTip(QCoreApplication.translate("Dialog", u"Connection status must be \"Connected\" before settings will be applied.", None))
#endif // QT_CONFIG(tooltip)
        self.connect_btn.setText(QCoreApplication.translate("Dialog", u"Connect", None))
#if QT_CONFIG(tooltip)
        self.label_connection.setToolTip(QCoreApplication.translate("Dialog", u"Were you able to communicate with the remote MLaudio instance.", None))
#endif // QT_CONFIG(tooltip)
        self.label_connection.setText(QCoreApplication.translate("Dialog", u"Status: Diconnected", None))
    # retranslateUi


# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MLaudio.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QGraphicsView, QLabel, QLineEdit,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QTextBrowser, QWidget)
import icons_rc

class Ui_MLaudio(object):
    def setupUi(self, MLaudio):
        if not MLaudio.objectName():
            MLaudio.setObjectName(u"MLaudio")
        MLaudio.resize(640, 480)
        MLaudio.setIconSize(QSize(12, 12))
        self.actionAudio_Settings = QAction(MLaudio)
        self.actionAudio_Settings.setObjectName(u"actionAudio_Settings")
        self.actionPreferences = QAction(MLaudio)
        self.actionPreferences.setObjectName(u"actionPreferences")
        self.actionTutorial = QAction(MLaudio)
        self.actionTutorial.setObjectName(u"actionTutorial")
        self.actionManual = QAction(MLaudio)
        self.actionManual.setObjectName(u"actionManual")
        self.centralwidget = QWidget(MLaudio)
        self.centralwidget.setObjectName(u"centralwidget")
        self.Mode_Lb = QLabel(self.centralwidget)
        self.Mode_Lb.setObjectName(u"Mode_Lb")
        self.Mode_Lb.setGeometry(QRect(0, 420, 81, 16))
        self.lineEdit_filename = QLineEdit(self.centralwidget)
        self.lineEdit_filename.setObjectName(u"lineEdit_filename")
        self.lineEdit_filename.setGeometry(QRect(400, 280, 151, 22))
        self.lineEdit_filename.setLayoutDirection(Qt.LeftToRight)
        self.lineEdit_filename.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(250, 50, 91, 20))
        self.Play1 = QPushButton(self.centralwidget)
        self.Play1.setObjectName(u"Play1")
        self.Play1.setGeometry(QRect(50, 160, 24, 24))
        icon = QIcon()
        icon.addFile(u":/play.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Play1.setIcon(icon)
        self.Play1.setIconSize(QSize(20, 16))
        self.Stop1 = QPushButton(self.centralwidget)
        self.Stop1.setObjectName(u"Stop1")
        self.Stop1.setGeometry(QRect(140, 160, 24, 24))
        icon1 = QIcon()
        icon1.addFile(u":/stop.png", QSize(), QIcon.Normal, QIcon.On)
        self.Stop1.setIcon(icon1)
        self.Stop1.setIconSize(QSize(20, 16))
        self.Record1 = QPushButton(self.centralwidget)
        self.Record1.setObjectName(u"Record1")
        self.Record1.setEnabled(False)
        self.Record1.setGeometry(QRect(230, 160, 24, 24))
        icon2 = QIcon()
        icon2.addFile(u":/record.png", QSize(), QIcon.Normal, QIcon.On)
        self.Record1.setIcon(icon2)
        self.Record1.setIconSize(QSize(20, 16))
        self.Play2 = QPushButton(self.centralwidget)
        self.Play2.setObjectName(u"Play2")
        self.Play2.setGeometry(QRect(50, 280, 24, 24))
        icon3 = QIcon()
        icon3.addFile(u":/play.png", QSize(), QIcon.Normal, QIcon.On)
        self.Play2.setIcon(icon3)
        self.Play2.setIconSize(QSize(20, 16))
        self.Stop2 = QPushButton(self.centralwidget)
        self.Stop2.setObjectName(u"Stop2")
        self.Stop2.setGeometry(QRect(140, 280, 24, 24))
        self.Stop2.setIcon(icon1)
        self.Record2 = QPushButton(self.centralwidget)
        self.Record2.setObjectName(u"Record2")
        self.Record2.setGeometry(QRect(230, 280, 24, 24))
        self.Record2.setIcon(icon2)
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(260, 160, 141, 16))
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(270, 280, 121, 16))
        self.Next_btn = QPushButton(self.centralwidget)
        self.Next_btn.setObjectName(u"Next_btn")
        self.Next_btn.setGeometry(QRect(530, 410, 80, 22))
        self.Transcript_brw = QTextBrowser(self.centralwidget)
        self.Transcript_brw.setObjectName(u"Transcript_brw")
        self.Transcript_brw.setGeometry(QRect(50, 70, 561, 61))
        self.WAV_Graph2 = QGraphicsView(self.centralwidget)
        self.WAV_Graph2.setObjectName(u"WAV_Graph2")
        self.WAV_Graph2.setGeometry(QRect(50, 310, 551, 81))
        self.Wav_Graph1 = QGraphicsView(self.centralwidget)
        self.Wav_Graph1.setObjectName(u"Wav_Graph1")
        self.Wav_Graph1.setGeometry(QRect(50, 190, 551, 81))
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(140, 410, 80, 22))
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(10, 70, 31, 61))
        self.lineEdit_filename_target = QLineEdit(self.centralwidget)
        self.lineEdit_filename_target.setObjectName(u"lineEdit_filename_target")
        self.lineEdit_filename_target.setEnabled(False)
        self.lineEdit_filename_target.setGeometry(QRect(400, 160, 201, 22))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(370, 20, 57, 14))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(430, 10, 111, 31))
        font = QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.lineEdit_filename_end = QLineEdit(self.centralwidget)
        self.lineEdit_filename_end.setObjectName(u"lineEdit_filename_end")
        self.lineEdit_filename_end.setEnabled(False)
        self.lineEdit_filename_end.setGeometry(QRect(550, 280, 51, 22))
        MLaudio.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MLaudio)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 640, 19))
        self.menuOptions = QMenu(self.menubar)
        self.menuOptions.setObjectName(u"menuOptions")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        MLaudio.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MLaudio)
        self.statusbar.setObjectName(u"statusbar")
        MLaudio.setStatusBar(self.statusbar)
#if QT_CONFIG(shortcut)
        self.Mode_Lb.setBuddy(self.Next_btn)
#endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.lineEdit_filename, self.Play1)
        QWidget.setTabOrder(self.Play1, self.Stop1)
        QWidget.setTabOrder(self.Stop1, self.Record1)
        QWidget.setTabOrder(self.Record1, self.Play2)
        QWidget.setTabOrder(self.Play2, self.Stop2)
        QWidget.setTabOrder(self.Stop2, self.Record2)
        QWidget.setTabOrder(self.Record2, self.Next_btn)
        QWidget.setTabOrder(self.Next_btn, self.Transcript_brw)
        QWidget.setTabOrder(self.Transcript_brw, self.WAV_Graph2)
        QWidget.setTabOrder(self.WAV_Graph2, self.Wav_Graph1)

        self.menubar.addAction(self.menuOptions.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuOptions.addAction(self.actionAudio_Settings)
        self.menuOptions.addAction(self.actionPreferences)
        self.menuHelp.addSeparator()
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionManual)

        self.retranslateUi(MLaudio)

        QMetaObject.connectSlotsByName(MLaudio)
    # setupUi

    def retranslateUi(self, MLaudio):
        MLaudio.setWindowTitle(QCoreApplication.translate("MLaudio", u"MLaudio", None))
        self.actionAudio_Settings.setText(QCoreApplication.translate("MLaudio", u"Audio Settings", None))
        self.actionPreferences.setText(QCoreApplication.translate("MLaudio", u"Preferences", None))
        self.actionTutorial.setText(QCoreApplication.translate("MLaudio", u"Tutorial", None))
        self.actionManual.setText(QCoreApplication.translate("MLaudio", u"Manual", None))
        self.Mode_Lb.setText(QCoreApplication.translate("MLaudio", u"MODE: Local", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_filename.setToolTip(QCoreApplication.translate("MLaudio", u"The last character_number cannot be changed.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.label_3.setToolTip(QCoreApplication.translate("MLaudio", u"Text that matches audio, if provided", None))
#endif // QT_CONFIG(tooltip)
        self.label_3.setText(QCoreApplication.translate("MLaudio", u"Transcripton", None))
#if QT_CONFIG(tooltip)
        self.Play1.setToolTip(QCoreApplication.translate("MLaudio", u"Play", None))
#endif // QT_CONFIG(tooltip)
        self.Play1.setText("")
#if QT_CONFIG(tooltip)
        self.Stop1.setToolTip(QCoreApplication.translate("MLaudio", u"Stop", None))
#endif // QT_CONFIG(tooltip)
        self.Stop1.setText("")
#if QT_CONFIG(tooltip)
        self.Record1.setToolTip(QCoreApplication.translate("MLaudio", u"Record", None))
#endif // QT_CONFIG(tooltip)
        self.Record1.setText("")
#if QT_CONFIG(tooltip)
        self.Play2.setToolTip(QCoreApplication.translate("MLaudio", u"Play", None))
#endif // QT_CONFIG(tooltip)
        self.Play2.setText("")
#if QT_CONFIG(tooltip)
        self.Stop2.setToolTip(QCoreApplication.translate("MLaudio", u"Stop", None))
#endif // QT_CONFIG(tooltip)
        self.Stop2.setText("")
#if QT_CONFIG(tooltip)
        self.Record2.setToolTip(QCoreApplication.translate("MLaudio", u"Record", None))
#endif // QT_CONFIG(tooltip)
        self.Record2.setText("")
        self.label_4.setText(QCoreApplication.translate("MLaudio", u"User 1 Audio (Target)", None))
        self.label_5.setText(QCoreApplication.translate("MLaudio", u"User 2: File Name", None))
#if QT_CONFIG(tooltip)
        self.Next_btn.setToolTip(QCoreApplication.translate("MLaudio", u"Will save current recording if recorded. Update filenames, load next clip, next transcript line.", None))
#endif // QT_CONFIG(tooltip)
        self.Next_btn.setText(QCoreApplication.translate("MLaudio", u"Next", None))
#if QT_CONFIG(tooltip)
        self.WAV_Graph2.setToolTip(QCoreApplication.translate("MLaudio", u"Wave form to record. Try to match the wave form above.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.Wav_Graph1.setToolTip(QCoreApplication.translate("MLaudio", u"Wave form of first audio snip.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.pushButton.setToolTip(QCoreApplication.translate("MLaudio", u"Decrements line number, filename, and load previous.", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton.setText(QCoreApplication.translate("MLaudio", u"Back", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_filename_target.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label.setText(QCoreApplication.translate("MLaudio", u"Status:", None))
        self.label_2.setText(QCoreApplication.translate("MLaudio", u"Waiting", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_filename_end.setToolTip(QCoreApplication.translate("MLaudio", u"The last character_number cannot be changed.", None))
#endif // QT_CONFIG(tooltip)
        self.menuOptions.setTitle(QCoreApplication.translate("MLaudio", u"Options", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MLaudio", u"Help", None))
    # retranslateUi


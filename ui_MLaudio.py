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
    QMainWindow, QMenu, QMenuBar, QPlainTextEdit,
    QPushButton, QSizePolicy, QStatusBar, QTextBrowser,
    QWidget)
import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(640, 480)
        MainWindow.setIconSize(QSize(12, 12))
        self.actionAudio_Settings = QAction(MainWindow)
        self.actionAudio_Settings.setObjectName(u"actionAudio_Settings")
        self.actionPreferences = QAction(MainWindow)
        self.actionPreferences.setObjectName(u"actionPreferences")
        self.actionTutorial = QAction(MainWindow)
        self.actionTutorial.setObjectName(u"actionTutorial")
        self.actionManual = QAction(MainWindow)
        self.actionManual.setObjectName(u"actionManual")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.Mode_Lb = QLabel(self.centralwidget)
        self.Mode_Lb.setObjectName(u"Mode_Lb")
        self.Mode_Lb.setGeometry(QRect(0, 420, 81, 16))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(140, 10, 131, 20))
        self.lineEdit_filename = QLineEdit(self.centralwidget)
        self.lineEdit_filename.setObjectName(u"lineEdit_filename")
        self.lineEdit_filename.setGeometry(QRect(270, 10, 331, 22))
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
        self.label_4.setGeometry(QRect(320, 160, 141, 16))
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(320, 280, 161, 16))
        self.Next_btn = QPushButton(self.centralwidget)
        self.Next_btn.setObjectName(u"Next_btn")
        self.Next_btn.setGeometry(QRect(530, 410, 80, 22))
        self.Transcript_brw = QTextBrowser(self.centralwidget)
        self.Transcript_brw.setObjectName(u"Transcript_brw")
        self.Transcript_brw.setGeometry(QRect(50, 70, 561, 61))
        self.plainTextEdit_line = QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_line.setObjectName(u"plainTextEdit_line")
        self.plainTextEdit_line.setGeometry(QRect(10, 70, 41, 61))
        self.WAV_Graph2 = QGraphicsView(self.centralwidget)
        self.WAV_Graph2.setObjectName(u"WAV_Graph2")
        self.WAV_Graph2.setGeometry(QRect(50, 310, 551, 81))
        self.Wav_Graph1 = QGraphicsView(self.centralwidget)
        self.Wav_Graph1.setObjectName(u"Wav_Graph1")
        self.Wav_Graph1.setGeometry(QRect(50, 190, 551, 81))
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(140, 410, 80, 22))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 640, 19))
        self.menuOptions = QMenu(self.menubar)
        self.menuOptions.setObjectName(u"menuOptions")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
#if QT_CONFIG(shortcut)
        self.Mode_Lb.setBuddy(self.Next_btn)
        self.label_2.setBuddy(self.lineEdit_filename)
#endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.lineEdit_filename, self.plainTextEdit_line)
        QWidget.setTabOrder(self.plainTextEdit_line, self.Play1)
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

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionAudio_Settings.setText(QCoreApplication.translate("MainWindow", u"Audio Settings", None))
        self.actionPreferences.setText(QCoreApplication.translate("MainWindow", u"Preferences", None))
        self.actionTutorial.setText(QCoreApplication.translate("MainWindow", u"Tutorial", None))
        self.actionManual.setText(QCoreApplication.translate("MainWindow", u"Manual", None))
        self.Mode_Lb.setText(QCoreApplication.translate("MainWindow", u"MODE: Local", None))
#if QT_CONFIG(tooltip)
        self.label_2.setToolTip(QCoreApplication.translate("MainWindow", u"filename that current recording will have", None))
#endif // QT_CONFIG(tooltip)
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Currently Writing file:", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_filename.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.label_3.setToolTip(QCoreApplication.translate("MainWindow", u"Text that matches audio, if provided", None))
#endif // QT_CONFIG(tooltip)
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Transcripton", None))
#if QT_CONFIG(tooltip)
        self.Play1.setToolTip(QCoreApplication.translate("MainWindow", u"Play", None))
#endif // QT_CONFIG(tooltip)
        self.Play1.setText("")
#if QT_CONFIG(tooltip)
        self.Stop1.setToolTip(QCoreApplication.translate("MainWindow", u"Stop", None))
#endif // QT_CONFIG(tooltip)
        self.Stop1.setText("")
#if QT_CONFIG(tooltip)
        self.Record1.setToolTip(QCoreApplication.translate("MainWindow", u"Record", None))
#endif // QT_CONFIG(tooltip)
        self.Record1.setText("")
#if QT_CONFIG(tooltip)
        self.Play2.setToolTip(QCoreApplication.translate("MainWindow", u"Play", None))
#endif // QT_CONFIG(tooltip)
        self.Play2.setText("")
#if QT_CONFIG(tooltip)
        self.Stop2.setToolTip(QCoreApplication.translate("MainWindow", u"Stop", None))
#endif // QT_CONFIG(tooltip)
        self.Stop2.setText("")
#if QT_CONFIG(tooltip)
        self.Record2.setToolTip(QCoreApplication.translate("MainWindow", u"Record", None))
#endif // QT_CONFIG(tooltip)
        self.Record2.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Player 1 Audio (Target)", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Player 2 Audio (Client)", None))
#if QT_CONFIG(tooltip)
        self.Next_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Will save current recording if recorded. Update filenames, load next clip, next transcript line.", None))
#endif // QT_CONFIG(tooltip)
        self.Next_btn.setText(QCoreApplication.translate("MainWindow", u"Next", None))
#if QT_CONFIG(tooltip)
        self.plainTextEdit_line.setToolTip(QCoreApplication.translate("MainWindow", u"Current Line Number, or Count", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.WAV_Graph2.setToolTip(QCoreApplication.translate("MainWindow", u"Wave form to record. Try to match the wave form above.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.Wav_Graph1.setToolTip(QCoreApplication.translate("MainWindow", u"Wave form of first audio snip.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.pushButton.setToolTip(QCoreApplication.translate("MainWindow", u"Decrements line number, filename, and load previous.", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        self.menuOptions.setTitle(QCoreApplication.translate("MainWindow", u"Options", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi


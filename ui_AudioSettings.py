# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AudioSettings.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QLabel,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_Dialog_Aud(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(220, 169)
        self.verticalLayoutWidget = QWidget(Dialog)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 10, 201, 151))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSpacing(1)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.comboBox_2 = QComboBox(self.verticalLayoutWidget)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setLayoutDirection(Qt.RightToLeft)

        self.verticalLayout.addWidget(self.comboBox_2)

        self.label_2 = QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.comboBox_3 = QComboBox(self.verticalLayoutWidget)
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.setObjectName(u"comboBox_3")
        self.comboBox_3.setLayoutDirection(Qt.RightToLeft)

        self.verticalLayout.addWidget(self.comboBox_3)

        self.label_3 = QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)

        self.comboBox = QComboBox(self.verticalLayoutWidget)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setLayoutDirection(Qt.RightToLeft)

        self.verticalLayout.addWidget(self.comboBox)

        self.pushButton = QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout.addWidget(self.pushButton)

        QWidget.setTabOrder(self.comboBox_2, self.comboBox_3)
        QWidget.setTabOrder(self.comboBox_3, self.comboBox)
        QWidget.setTabOrder(self.comboBox, self.pushButton)

        self.retranslateUi(Dialog)

        self.comboBox_3.setCurrentIndex(2)
        self.comboBox.setCurrentIndex(5)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Audio Settings", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Channels", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("Dialog", u"Mono", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("Dialog", u"Stereo", None))

        self.label_2.setText(QCoreApplication.translate("Dialog", u"Bit Depth", None))
        self.comboBox_3.setItemText(0, QCoreApplication.translate("Dialog", u"16-bit", None))
        self.comboBox_3.setItemText(1, QCoreApplication.translate("Dialog", u"24-bit", None))
        self.comboBox_3.setItemText(2, QCoreApplication.translate("Dialog", u"32-bit", None))

        self.label_3.setText(QCoreApplication.translate("Dialog", u"Hz", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Dialog", u"8000", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Dialog", u"11025", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("Dialog", u"16000", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("Dialog", u"22050", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("Dialog", u"32000", None))
        self.comboBox.setItemText(5, QCoreApplication.translate("Dialog", u"44100", None))
        self.comboBox.setItemText(6, QCoreApplication.translate("Dialog", u"48000", None))
        self.comboBox.setItemText(7, QCoreApplication.translate("Dialog", u"88200", None))
        self.comboBox.setItemText(8, QCoreApplication.translate("Dialog", u"96000", None))
        self.comboBox.setItemText(9, QCoreApplication.translate("Dialog", u"176400", None))
        self.comboBox.setItemText(10, QCoreApplication.translate("Dialog", u"192000", None))
        self.comboBox.setItemText(11, QCoreApplication.translate("Dialog", u"352800", None))
        self.comboBox.setItemText(12, QCoreApplication.translate("Dialog", u"384000", None))

        self.pushButton.setText(QCoreApplication.translate("Dialog", u"Ok", None))
    # retranslateUi


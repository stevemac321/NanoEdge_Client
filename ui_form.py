# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
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
from PySide6.QtWidgets import (QApplication, QComboBox, QLineEdit, QPlainTextEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(1038, 986)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Widget.sizePolicy().hasHeightForWidth())
        Widget.setSizePolicy(sizePolicy)
        self.sendStop = QPushButton(Widget)
        self.sendStop.setObjectName(u"sendStop")
        self.sendStop.setGeometry(QRect(120, 40, 91, 24))
        self.sendStart = QPushButton(Widget)
        self.sendStart.setObjectName(u"sendStart")
        self.sendStart.setGeometry(QRect(10, 40, 101, 24))
        self.comboPortNumber = QComboBox(Widget)
        self.comboPortNumber.addItem("")
        self.comboPortNumber.addItem("")
        self.comboPortNumber.addItem("")
        self.comboPortNumber.addItem("")
        self.comboPortNumber.addItem("")
        self.comboPortNumber.addItem("")
        self.comboPortNumber.addItem("")
        self.comboPortNumber.setObjectName(u"comboPortNumber")
        self.comboPortNumber.setGeometry(QRect(220, 40, 131, 22))
        self.plainTextEditReport = QPlainTextEdit(Widget)
        self.plainTextEditReport.setObjectName(u"plainTextEditReport")
        self.plainTextEditReport.setGeometry(QRect(20, 110, 1001, 851))
        sizePolicy.setHeightForWidth(self.plainTextEditReport.sizePolicy().hasHeightForWidth())
        self.plainTextEditReport.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.plainTextEditReport.setFont(font)
        self.comboBaud = QComboBox(Widget)
        self.comboBaud.addItem("")
        self.comboBaud.addItem("")
        self.comboBaud.addItem("")
        self.comboBaud.addItem("")
        self.comboBaud.addItem("")
        self.comboBaud.setObjectName(u"comboBaud")
        self.comboBaud.setGeometry(QRect(360, 40, 191, 22))
        self.pushClear = QPushButton(Widget)
        self.pushClear.setObjectName(u"pushClear")
        self.pushClear.setGeometry(QRect(290, 90, 75, 24))
        self.lineEdit = QLineEdit(Widget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(10, 10, 911, 22))
        self.pushSend = QPushButton(Widget)
        self.pushSend.setObjectName(u"pushSend")
        self.pushSend.setGeometry(QRect(1160, 10, 75, 24))
        self.sendFileButton = QPushButton(Widget)
        self.sendFileButton.setObjectName(u"sendFileButton")
        self.sendFileButton.setGeometry(QRect(940, 80, 81, 24))
        self.pushEcho = QPushButton(Widget)
        self.pushEcho.setObjectName(u"pushEcho")
        self.pushEcho.setGeometry(QRect(20, 90, 241, 24))
        self.pushSave = QPushButton(Widget)
        self.pushSave.setObjectName(u"pushSave")
        self.pushSave.setGeometry(QRect(1144, 80, 111, 24))
        self.sendBinary = QPushButton(Widget)
        self.sendBinary.setObjectName(u"sendBinary")
        self.sendBinary.setGeometry(QRect(930, 10, 81, 24))

        self.retranslateUi(Widget)

        self.comboPortNumber.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.sendStop.setText(QCoreApplication.translate("Widget", u"Stop", None))
        self.sendStart.setText(QCoreApplication.translate("Widget", u"Start", None))
        self.comboPortNumber.setItemText(0, QCoreApplication.translate("Widget", u"COM1", None))
        self.comboPortNumber.setItemText(1, QCoreApplication.translate("Widget", u"COM2", None))
        self.comboPortNumber.setItemText(2, QCoreApplication.translate("Widget", u"COM3", None))
        self.comboPortNumber.setItemText(3, QCoreApplication.translate("Widget", u"COM4", None))
        self.comboPortNumber.setItemText(4, QCoreApplication.translate("Widget", u"COM5", None))
        self.comboPortNumber.setItemText(5, QCoreApplication.translate("Widget", u"COM6", None))
        self.comboPortNumber.setItemText(6, QCoreApplication.translate("Widget", u"COM7", None))

        self.comboBaud.setItemText(0, QCoreApplication.translate("Widget", u"115200", None))
        self.comboBaud.setItemText(1, QCoreApplication.translate("Widget", u"57600", None))
        self.comboBaud.setItemText(2, QCoreApplication.translate("Widget", u"38400", None))
        self.comboBaud.setItemText(3, QCoreApplication.translate("Widget", u"19200", None))
        self.comboBaud.setItemText(4, QCoreApplication.translate("Widget", u"9600", None))

        self.pushClear.setText(QCoreApplication.translate("Widget", u"Clear", None))
        self.lineEdit.setText("")
        self.pushSend.setText(QCoreApplication.translate("Widget", u"Send One ", None))
        self.sendFileButton.setText(QCoreApplication.translate("Widget", u"Send File", None))
        self.pushEcho.setText(QCoreApplication.translate("Widget", u"Send Text", None))
        self.pushSave.setText(QCoreApplication.translate("Widget", u"Save Results", None))
        self.sendBinary.setText(QCoreApplication.translate("Widget", u"Send Binary", None))
    # retranslateUi


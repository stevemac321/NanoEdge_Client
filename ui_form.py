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
from PySide6.QtWidgets import (QApplication, QComboBox, QPlainTextEdit, QPushButton,
    QSizePolicy, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(800, 600)
        self.sendNormal = QPushButton(Widget)
        self.sendNormal.setObjectName(u"sendNormal")
        self.sendNormal.setGeometry(QRect(120, 10, 91, 24))
        self.sendAnom = QPushButton(Widget)
        self.sendAnom.setObjectName(u"sendAnom")
        self.sendAnom.setGeometry(QRect(10, 10, 101, 24))
        self.comboPortNumber = QComboBox(Widget)
        self.comboPortNumber.addItem("")
        self.comboPortNumber.addItem("")
        self.comboPortNumber.addItem("")
        self.comboPortNumber.addItem("")
        self.comboPortNumber.addItem("")
        self.comboPortNumber.addItem("")
        self.comboPortNumber.addItem("")
        self.comboPortNumber.setObjectName(u"comboPortNumber")
        self.comboPortNumber.setGeometry(QRect(220, 10, 131, 22))
        self.plainTextEditReport = QPlainTextEdit(Widget)
        self.plainTextEditReport.setObjectName(u"plainTextEditReport")
        self.plainTextEditReport.setGeometry(QRect(20, 40, 741, 551))
        self.comboBaud = QComboBox(Widget)
        self.comboBaud.addItem("")
        self.comboBaud.addItem("")
        self.comboBaud.addItem("")
        self.comboBaud.addItem("")
        self.comboBaud.addItem("")
        self.comboBaud.setObjectName(u"comboBaud")
        self.comboBaud.setGeometry(QRect(360, 10, 191, 22))
        self.pushClear = QPushButton(Widget)
        self.pushClear.setObjectName(u"pushClear")
        self.pushClear.setGeometry(QRect(580, 10, 75, 24))

        self.retranslateUi(Widget)

        self.comboPortNumber.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.sendNormal.setText(QCoreApplication.translate("Widget", u"Submit Normal", None))
        self.sendAnom.setText(QCoreApplication.translate("Widget", u"Send Anomaly", None))
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
    # retranslateUi


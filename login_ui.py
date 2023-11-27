# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login_ui.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)


class Ui_Login(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(300, 330)
        MainWindow.setMinimumSize(QSize(300, 330))
        MainWindow.setMaximumSize(QSize(300, 330))
        icon = QIcon()
        icon.addFile(u":/icons/lib.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"QWidget {\n"
"background-color: #DCD6CA;\n"
"}\n"
"\n"
"QPushButton {\n"
"background-color: #6D3D14;\n"
"color: #DCD6CA;\n"
"font-size: 12pt;\n"
"border: 2px solid #6D3D14;\n"
"border-radius: 3px;\n"
"padding: 3px;\n"
"font-weight: 400;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"  background-color: #7B502B;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"  background-color: #DCD6CA;\n"
"  color: #6D3D14;\n"
"}\n"
"\n"
"QTableWidget {\n"
"background-color: #DCD6CA;\n"
"color: #3c3b3a;\n"
"font-size: 10pt;\n"
"border: 2px solid #6D3D14;\n"
"border-radius: 3px;\n"
"}\n"
"\n"
"QPushButton#login_btn{\n"
"	padding: 7px;\n"
"	font-size: 14pt;\n"
"}\n"
"\n"
"\n"
"QLabel {\n"
"	font-size: 12pt;\n"
"	color: #6D3D14;\n"
"}\n"
"\n"
"QLabel#label_lib {\n"
"	color: #6D3D14;\n"
"	font-size: 18pt;\n"
"	font-weight: 400;\n"
"}\n"
"\n"
"QLineEdit {\n"
"background-color: #DCD6CA;\n"
"color: #6D3D14;\n"
"font-size: 12pt;\n"
"border: 2px solid #6D3D14;\n"
"border-radius: 3px;\n"
"padding: 4px;\n"
"font-weight: 400;\n"
"}\n"
"\n"
"QHBoxLayout#p"
                        "assword_Layout {\n"
"background-color: #DCD6CA;\n"
"color: #6D3D14;\n"
"font-size: 33pt;\n"
"border: 2px solid #6D3D14;\n"
"border-radius: 3px;\n"
"padding: 3px;\n"
"font-weight: 400;\n"
"}")
        MainWindow.setIconSize(QSize(24, 24))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.info_Layout = QHBoxLayout()
        self.info_Layout.setObjectName(u"info_Layout")
        self.label_lib = QLabel(self.centralwidget)
        self.label_lib.setObjectName(u"label_lib")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_lib.sizePolicy().hasHeightForWidth())
        self.label_lib.setSizePolicy(sizePolicy)
        self.label_lib.setMaximumSize(QSize(16777215, 16777215))
        self.label_lib.setLayoutDirection(Qt.RightToLeft)
        self.label_lib.setAlignment(Qt.AlignCenter)

        self.info_Layout.addWidget(self.label_lib)


        self.verticalLayout.addLayout(self.info_Layout)

        self.verticalSpacer_4 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_4)

        self.label_error = QLabel(self.centralwidget)
        self.label_error.setObjectName(u"label_error")
        self.label_error.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_error)

        self.verticalSpacer = QSpacerItem(10, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.date_Layout = QVBoxLayout()
        self.date_Layout.setObjectName(u"date_Layout")
        self.label_login = QLabel(self.centralwidget)
        self.label_login.setObjectName(u"label_login")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_login.sizePolicy().hasHeightForWidth())
        self.label_login.setSizePolicy(sizePolicy1)

        self.date_Layout.addWidget(self.label_login)

        self.lineEdit_login = QLineEdit(self.centralwidget)
        self.lineEdit_login.setObjectName(u"lineEdit_login")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.lineEdit_login.sizePolicy().hasHeightForWidth())
        self.lineEdit_login.setSizePolicy(sizePolicy2)

        self.date_Layout.addWidget(self.lineEdit_login)

        self.verticalSpacer_3 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.date_Layout.addItem(self.verticalSpacer_3)

        self.label_password = QLabel(self.centralwidget)
        self.label_password.setObjectName(u"label_password")
        sizePolicy1.setHeightForWidth(self.label_password.sizePolicy().hasHeightForWidth())
        self.label_password.setSizePolicy(sizePolicy1)

        self.date_Layout.addWidget(self.label_password)

        self.password_Layout = QHBoxLayout()
        self.password_Layout.setObjectName(u"password_Layout")
        self.lineEdit_password = QLineEdit(self.centralwidget)
        self.lineEdit_password.setObjectName(u"lineEdit_password")
        sizePolicy2.setHeightForWidth(self.lineEdit_password.sizePolicy().hasHeightForWidth())
        self.lineEdit_password.setSizePolicy(sizePolicy2)
        self.lineEdit_password.setStyleSheet(u"QLineEdit {\n"
"margin: 0px;\n"
"}")

        self.password_Layout.addWidget(self.lineEdit_password)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"QPushButton:hover{\n"
"  background-color: #7B502B;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"  background-color: #7B502B;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/icons/outline_visibility_off_white_24dp.png", QSize(), QIcon.Normal, QIcon.Off)
        icon1.addFile(u":/icons/outline_remove_red_eye_white_24dp.png", QSize(), QIcon.Normal, QIcon.On)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QSize(25, 25))
        self.pushButton.setCheckable(True)
        self.pushButton.setChecked(True)

        self.password_Layout.addWidget(self.pushButton)


        self.date_Layout.addLayout(self.password_Layout)


        self.verticalLayout.addLayout(self.date_Layout)

        self.verticalSpacer_2 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.login_Layout = QHBoxLayout()
        self.login_Layout.setObjectName(u"login_Layout")
        self.login_btn = QPushButton(self.centralwidget)
        self.login_btn.setObjectName(u"login_btn")

        self.login_Layout.addWidget(self.login_btn)


        self.verticalLayout.addLayout(self.login_Layout)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Login", None))
        self.label_lib.setText(QCoreApplication.translate("MainWindow", u"\u0411\u0438\u0431\u043b\u0438\u043e\u0442\u0435\u043a\u0438 \u041a\u0440\u0430\u0441\u043d\u043e\u044f\u0440\u0441\u043a\u0430", None))
        self.label_error.setText("")
        self.label_login.setText(QCoreApplication.translate("MainWindow", u"\u041b\u043e\u0433\u0438\u043d", None))
        self.label_password.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u043e\u043b\u044c", None))
        self.pushButton.setText("")
        self.login_btn.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0445\u043e\u0434", None))
    # retranslateUi


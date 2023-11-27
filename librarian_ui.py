# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'librarian_ui.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QMainWindow,
    QPushButton, QSizePolicy, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)
import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(750, 350)
        MainWindow.setMinimumSize(QSize(750, 260))
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
"  background-color: #6D3D14;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"  background-color: #886140;\n"
"  border: 2px solid #886140;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"  background-color: #886140;\n"
"  border: 2px solid #886140;\n"
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
"")
        MainWindow.setIconSize(QSize(24, 24))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.base_Layout = QHBoxLayout()
        self.base_Layout.setObjectName(u"base_Layout")
        self.room_btn = QPushButton(self.centralwidget)
        self.room_btn.setObjectName(u"room_btn")
        icon1 = QIcon()
        icon1.addFile(u":/icons/event_seat_white_24dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.room_btn.setIcon(icon1)
        self.room_btn.setCheckable(True)
        self.room_btn.setChecked(True)

        self.base_Layout.addWidget(self.room_btn)

        self.book_btn = QPushButton(self.centralwidget)
        self.book_btn.setObjectName(u"book_btn")
        icon2 = QIcon()
        icon2.addFile(u":/icons/book_white_24dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.book_btn.setIcon(icon2)
        self.book_btn.setCheckable(True)

        self.base_Layout.addWidget(self.book_btn)

        self.readers_btn = QPushButton(self.centralwidget)
        self.readers_btn.setObjectName(u"readers_btn")
        icon3 = QIcon()
        icon3.addFile(u":/icons/people_white_24dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.readers_btn.setIcon(icon3)
        self.readers_btn.setCheckable(True)

        self.base_Layout.addWidget(self.readers_btn)

        self.is_btn = QPushButton(self.centralwidget)
        self.is_btn.setObjectName(u"is_btn")
        icon4 = QIcon()
        icon4.addFile(u":/icons/pan_tool_white_24dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.is_btn.setIcon(icon4)
        self.is_btn.setCheckable(True)

        self.base_Layout.addWidget(self.is_btn)


        self.verticalLayout.addLayout(self.base_Layout)

        self.table_Layout = QHBoxLayout()
        self.table_Layout.setObjectName(u"table_Layout")
        self.tableWidget = QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName(u"tableWidget")

        self.table_Layout.addWidget(self.tableWidget)


        self.verticalLayout.addLayout(self.table_Layout)

        self.functional_Layout = QHBoxLayout()
        self.functional_Layout.setObjectName(u"functional_Layout")
        self.del_btn = QPushButton(self.centralwidget)
        self.del_btn.setObjectName(u"del_btn")
        self.del_btn.setStyleSheet(u"\n"
"QPushButton{\n"
"	padding: 7px;\n"
"	font-size: 14pt;\n"
"	background-color: #DCD6CA;\n"
"	color: #6D3D14;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	padding: 7px;\n"
"	font-size: 14pt;\n"
"	background-color: #DCD6CA;\n"
"	color: #6D3D14;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	padding: 7px;\n"
"	font-size: 14pt;\n"
"	background-color: #6D3D14;\n"
"	color: #DCD6CA;\n"
"}")

        self.functional_Layout.addWidget(self.del_btn)

        self.editing_btn = QPushButton(self.centralwidget)
        self.editing_btn.setObjectName(u"editing_btn")
        self.editing_btn.setStyleSheet(u"\n"
"QPushButton{\n"
"	padding: 7px;\n"
"	font-size: 14pt;\n"
"	background-color: #DCD6CA;\n"
"	color: #6D3D14;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	padding: 7px;\n"
"	font-size: 14pt;\n"
"	background-color: #DCD6CA;\n"
"	color: #6D3D14;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	padding: 7px;\n"
"	font-size: 14pt;\n"
"	background-color: #6D3D14;\n"
"	color: #DCD6CA;\n"
"}")

        self.functional_Layout.addWidget(self.editing_btn)

        self.new_btn = QPushButton(self.centralwidget)
        self.new_btn.setObjectName(u"new_btn")
        self.new_btn.setStyleSheet(u"\n"
"QPushButton{\n"
"	padding: 7px;\n"
"	font-size: 14pt;\n"
"	background-color: #DCD6CA;\n"
"	color: #6D3D14;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	padding: 7px;\n"
"	font-size: 14pt;\n"
"	background-color: #DCD6CA;\n"
"	color: #6D3D14;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	padding: 7px;\n"
"	font-size: 14pt;\n"
"	background-color: #6D3D14;\n"
"	color: #DCD6CA;\n"
"}")

        self.functional_Layout.addWidget(self.new_btn)

        self.safe_btn = QPushButton(self.centralwidget)
        self.safe_btn.setObjectName(u"safe_btn")
        self.safe_btn.setStyleSheet(u"\n"
"QPushButton{\n"
"	padding: 7px;\n"
"	font-size: 14pt;\n"
"	background-color: #DCD6CA;\n"
"	color: #6D3D14;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	padding: 7px;\n"
"	font-size: 14pt;\n"
"	background-color: #DCD6CA;\n"
"	color: #6D3D14;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	padding: 7px;\n"
"	font-size: 14pt;\n"
"	background-color: #6D3D14;\n"
"	color: #DCD6CA;\n"
"}")

        self.functional_Layout.addWidget(self.safe_btn)


        self.verticalLayout.addLayout(self.functional_Layout)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Library", None))
        self.room_btn.setText(QCoreApplication.translate("MainWindow", u"\u0427\u0438\u0442\u0430\u043b\u044c\u043d\u044b\u0435 \u0437\u0430\u043b\u044b", None))
        self.book_btn.setText(QCoreApplication.translate("MainWindow", u"\u041b\u0438\u0442\u0435\u0440\u0430\u0442\u0443\u0440\u0430", None))
        self.readers_btn.setText(QCoreApplication.translate("MainWindow", u"\u0427\u0438\u0442\u0430\u0442\u0435\u043b\u0438", None))
        self.is_btn.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0434\u0430\u043d\u043d\u0430\u044f \u043b\u0438\u0442\u0435\u0440\u0430\u0442\u0443\u0440\u0430", None))
        self.del_btn.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.editing_btn.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.new_btn.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.safe_btn.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
    # retranslateUi


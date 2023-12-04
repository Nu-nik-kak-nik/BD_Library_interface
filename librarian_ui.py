# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'librarian_ui2.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QHeaderView,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)
import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(760, 350)
        MainWindow.setMinimumSize(QSize(760, 350))
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        icon = QIcon()
        icon.addFile(u":/icons/lib.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"QWidget {\n"
"background-color: #DCD6CA;\n"
"}\n"
"\n"
"QPushButton {\n"
"background-color: #9C571C;\n"
"color: white;\n"
"font-size: 12pt;\n"
"border: 2px solid #9C571C;\n"
"border-radius: 3px;\n"
"padding: 3px;\n"
"font-weight: 400;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"  background-color: #9C571C;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"  background-color: #6D3D14;\n"
"  color: white;\n"
"  border: 2px solid #6D3D14;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"  background-color: #6D3D14;\n"
"  color: white;\n"
"  border: 2px solid #6D3D14;\n"
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
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.editing_btn = QPushButton(self.centralwidget)
        self.editing_btn.setObjectName(u"editing_btn")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.editing_btn.sizePolicy().hasHeightForWidth())
        self.editing_btn.setSizePolicy(sizePolicy)
        self.editing_btn.setMinimumSize(QSize(35, 35))
        self.editing_btn.setMaximumSize(QSize(35, 35))
        self.editing_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.editing_btn.setStyleSheet(u"QPushButton{\n"
"	padding: 0px;\n"
"	font-size: 14pt;\n"
"	background-color: #6D3D14;\n"
"	color: #DCD6CA;\n"
"    border: 2px solid #6D3D14;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #6D3D14;\n"
"	color: #DCD6CA;\n"
"    border: 2px solid #6D3D14;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: #9C571C;\n"
"	color: #DCD6CA;\n"
"    border: 2px solid #9C571C;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/btn/edit_white_24dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.editing_btn.setIcon(icon1)
        self.editing_btn.setIconSize(QSize(20, 20))

        self.gridLayout.addWidget(self.editing_btn, 3, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 35, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer, 11, 1, 1, 1)

        self.safe_btn = QPushButton(self.centralwidget)
        self.safe_btn.setObjectName(u"safe_btn")
        sizePolicy.setHeightForWidth(self.safe_btn.sizePolicy().hasHeightForWidth())
        self.safe_btn.setSizePolicy(sizePolicy)
        self.safe_btn.setMinimumSize(QSize(35, 35))
        self.safe_btn.setMaximumSize(QSize(35, 35))
        self.safe_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.safe_btn.setStyleSheet(u"QPushButton{\n"
"	padding: 0px;\n"
"	font-size: 14pt;\n"
"	background-color: #6D3D14;\n"
"	color: #DCD6CA;\n"
"    border: 2px solid #6D3D14;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #6D3D14;\n"
"	color: #DCD6CA;\n"
"    border: 2px solid #6D3D14;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: #9C571C;\n"
"	color: #DCD6CA;\n"
"    border: 2px solid #9C571C;\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/btn/save_white_24dp (1).svg", QSize(), QIcon.Normal, QIcon.Off)
        self.safe_btn.setIcon(icon2)
        self.safe_btn.setIconSize(QSize(20, 20))

        self.gridLayout.addWidget(self.safe_btn, 1, 1, 1, 1)

        self.report_btn = QPushButton(self.centralwidget)
        self.report_btn.setObjectName(u"report_btn")
        sizePolicy.setHeightForWidth(self.report_btn.sizePolicy().hasHeightForWidth())
        self.report_btn.setSizePolicy(sizePolicy)
        self.report_btn.setMinimumSize(QSize(35, 35))
        self.report_btn.setMaximumSize(QSize(35, 35))
        self.report_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.report_btn.setStyleSheet(u"QPushButton{\n"
"	padding: 0px;\n"
"	font-size: 14pt;\n"
"	background-color: #6D3D14;\n"
"	color: #DCD6CA;\n"
"    border: 2px solid #6D3D14;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #6D3D14;\n"
"	color: #DCD6CA;\n"
"    border: 2px solid #6D3D14;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: #9C571C;\n"
"	color: #DCD6CA;\n"
"    border: 2px solid #9C571C;\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/btn/feed_white_24dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.report_btn.setIcon(icon3)
        self.report_btn.setIconSize(QSize(20, 20))

        self.gridLayout.addWidget(self.report_btn, 4, 1, 1, 1)

        self.logout_btn = QPushButton(self.centralwidget)
        self.logout_btn.setObjectName(u"logout_btn")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Ignored)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.logout_btn.sizePolicy().hasHeightForWidth())
        self.logout_btn.setSizePolicy(sizePolicy1)
        self.logout_btn.setMinimumSize(QSize(35, 0))
        self.logout_btn.setMaximumSize(QSize(35, 16777215))
        self.logout_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.logout_btn.setStyleSheet(u"QPushButton{\n"
"	padding: 0px;\n"
"	font-size: 14pt;\n"
"	background-color: #6D3D14;\n"
"	color: #DCD6CA;\n"
"    border: 2px solid #6D3D14;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #6D3D14;\n"
"	color: #DCD6CA;\n"
"    border: 2px solid #6D3D14;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: #9C571C;\n"
"	color: #DCD6CA;\n"
"    border: 2px solid #9C571C;\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/btn/logout_white_24dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.logout_btn.setIcon(icon4)
        self.logout_btn.setIconSize(QSize(20, 20))

        self.gridLayout.addWidget(self.logout_btn, 0, 1, 1, 1)

        self.new_btn = QPushButton(self.centralwidget)
        self.new_btn.setObjectName(u"new_btn")
        sizePolicy.setHeightForWidth(self.new_btn.sizePolicy().hasHeightForWidth())
        self.new_btn.setSizePolicy(sizePolicy)
        self.new_btn.setMinimumSize(QSize(35, 35))
        self.new_btn.setMaximumSize(QSize(35, 35))
        self.new_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.new_btn.setStyleSheet(u"QPushButton{\n"
"	padding: 0px;\n"
"	font-size: 14pt;\n"
"	background-color: #6D3D14;\n"
"	color: #DCD6CA;\n"
"    border: 2px solid #6D3D14;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #6D3D14;\n"
"	color: #DCD6CA;\n"
"    border: 2px solid #6D3D14;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: #9C571C;\n"
"	color: #DCD6CA;\n"
"    border: 2px solid #9C571C;\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u":/btn/add_white_24dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.new_btn.setIcon(icon5)
        self.new_btn.setIconSize(QSize(20, 20))

        self.gridLayout.addWidget(self.new_btn, 2, 1, 1, 1)

        self.del_btn = QPushButton(self.centralwidget)
        self.del_btn.setObjectName(u"del_btn")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.del_btn.sizePolicy().hasHeightForWidth())
        self.del_btn.setSizePolicy(sizePolicy2)
        self.del_btn.setMinimumSize(QSize(35, 35))
        self.del_btn.setMaximumSize(QSize(35, 35))
        self.del_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.del_btn.setStyleSheet(u"QPushButton{\n"
"	padding: 0px;\n"
"	font-size: 14pt;\n"
"	background-color: #6D3D14;\n"
"	color: #DCD6CA;\n"
"    border: 2px solid #6D3D14;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #6D3D14;\n"
"	color: #DCD6CA;\n"
"    border: 2px solid #6D3D14;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: #9C571C;\n"
"	color: #DCD6CA;\n"
"    border: 2px solid #9C571C;\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u":/btn/delete_white_24dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.del_btn.setIcon(icon6)
        self.del_btn.setIconSize(QSize(20, 20))

        self.gridLayout.addWidget(self.del_btn, 5, 1, 1, 1)

        self.base_Layout = QHBoxLayout()
        self.base_Layout.setObjectName(u"base_Layout")
        self.room_btn = QPushButton(self.centralwidget)
        self.room_btn.setObjectName(u"room_btn")
        self.room_btn.setCursor(QCursor(Qt.PointingHandCursor))
        icon7 = QIcon()
        icon7.addFile(u":/icons/event_seat_white_24dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.room_btn.setIcon(icon7)
        self.room_btn.setCheckable(True)

        self.base_Layout.addWidget(self.room_btn)

        self.book_btn = QPushButton(self.centralwidget)
        self.book_btn.setObjectName(u"book_btn")
        self.book_btn.setCursor(QCursor(Qt.PointingHandCursor))
        icon8 = QIcon()
        icon8.addFile(u":/icons/book_white_24dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.book_btn.setIcon(icon8)
        self.book_btn.setCheckable(True)

        self.base_Layout.addWidget(self.book_btn)

        self.readers_btn = QPushButton(self.centralwidget)
        self.readers_btn.setObjectName(u"readers_btn")
        self.readers_btn.setCursor(QCursor(Qt.PointingHandCursor))
        icon9 = QIcon()
        icon9.addFile(u":/icons/people_white_24dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.readers_btn.setIcon(icon9)
        self.readers_btn.setCheckable(True)

        self.base_Layout.addWidget(self.readers_btn)

        self.is_btn = QPushButton(self.centralwidget)
        self.is_btn.setObjectName(u"is_btn")
        self.is_btn.setCursor(QCursor(Qt.PointingHandCursor))
        icon10 = QIcon()
        icon10.addFile(u":/icons/pan_tool_white_24dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.is_btn.setIcon(icon10)
        self.is_btn.setCheckable(True)

        self.base_Layout.addWidget(self.is_btn)


        self.gridLayout.addLayout(self.base_Layout, 0, 0, 1, 1)

        self.tableWidget = QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setMinimumSize(QSize(0, 0))
        self.tableWidget.setMaximumSize(QSize(16777215, 16777215))
        palette = QPalette()
        brush = QBrush(QColor(60, 59, 58, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(220, 214, 202, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush2 = QBrush(QColor(225, 124, 41, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Highlight, brush2)
        brush3 = QBrush(QColor(156, 87, 28, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Link, brush3)
        brush4 = QBrush(QColor(109, 61, 20, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.LinkVisited, brush4)
        brush5 = QBrush(QColor(60, 59, 58, 128))
        brush5.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush5)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Highlight, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Link, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.LinkVisited, brush4)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush5)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Link, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.LinkVisited, brush4)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush5)
#endif
        self.tableWidget.setPalette(palette)
        self.tableWidget.setStyleSheet(u"QHeaderView::section { \n"
"background-color: #9C571C; \n"
"color: white; \n"
"\n"
"}\n"
"\n"
"QTableWidget::item:selected {\n"
"    background-color: #B98960;\n"
"}\n"
"\n"
"QTableWidget::item {\n"
"    color: #6D3D14;\n"
"	 border: none;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    border: none;\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	font-size: 10pt;\n"
"}\n"
"\n"
"QTableView::item {\n"
"    border-right: 1px solid #6D3D14;\n"
"}\n"
"\n"
"\n"
"\n"
"QScrollBar:horizontal {\n"
"    background: #DCD6CA; /* \u0417\u0430\u0434\u0430\u0435\u0442 \u0446\u0432\u0435\u0442 \u0444\u043e\u043d\u0430 \u0433\u043e\u0440\u0438\u0437\u043e\u043d\u0442\u0430\u043b\u044c\u043d\u043e\u0433\u043e \u0441\u043a\u0440\u043e\u043b\u043b\u0431\u0430\u0440\u0430 */\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"    background: #6D3D14; /* \u0417\u0430\u0434\u0430\u0435\u0442 \u0446\u0432\u0435\u0442 \u043f\u043e\u043b\u0437\u0443\u043d\u043a\u0430 \u0433\u043e\u0440\u0438\u0437\u043e\u043d\u0442\u0430\u043b\u044c"
                        "\u043d\u043e\u0433\u043e \u0441\u043a\u0440\u043e\u043b\u043b\u0431\u0430\u0440\u0430 */\n"
"	border-radius: 3px;\n"
"}\n"
"QScrollBar:vertical {\n"
"    background: #DCD6CA; /* \u0417\u0430\u0434\u0430\u0435\u0442 \u0446\u0432\u0435\u0442 \u0444\u043e\u043d\u0430 \u0432\u0435\u0440\u0442\u0438\u043a\u0430\u043b\u044c\u043d\u043e\u0433\u043e \u0441\u043a\u0440\u043e\u043b\u043b\u0431\u0430\u0440\u0430 */\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background: #6D3D14; /* \u0417\u0430\u0434\u0430\u0435\u0442 \u0446\u0432\u0435\u0442 \u043f\u043e\u043b\u0437\u0443\u043d\u043a\u0430 \u0432\u0435\u0440\u0442\u0438\u043a\u0430\u043b\u044c\u043d\u043e\u0433\u043e \u0441\u043a\u0440\u043e\u043b\u043b\u0431\u0430\u0440\u0430 */\n"
"	border-radius: 3px;\n"
"}\n"
"\n"
"QTableWidget::selection {\n"
"    background-color: #B98960;\n"
"}")
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(0)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setHighlightSections(True)

        self.gridLayout.addWidget(self.tableWidget, 1, 0, 12, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Library", None))
        self.editing_btn.setText("")
        self.safe_btn.setText("")
        self.report_btn.setText("")
        self.logout_btn.setText("")
        self.new_btn.setText("")
        self.del_btn.setText("")
        self.room_btn.setText(QCoreApplication.translate("MainWindow", u"\u0427\u0438\u0442\u0430\u043b\u044c\u043d\u044b\u0435 \u0437\u0430\u043b\u044b", None))
        self.book_btn.setText(QCoreApplication.translate("MainWindow", u"\u041b\u0438\u0442\u0435\u0440\u0430\u0442\u0443\u0440\u0430", None))
        self.readers_btn.setText(QCoreApplication.translate("MainWindow", u"\u0427\u0438\u0442\u0430\u0442\u0435\u043b\u0438", None))
        self.is_btn.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0434\u0430\u043d\u043d\u0430\u044f \u043b\u0438\u0442\u0435\u0440\u0430\u0442\u0443\u0440\u0430", None))
    # retranslateUi


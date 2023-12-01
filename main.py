import psycopg2
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QTableView
# from PySide6.QtSql import QSqlDatabase, QSqlQuery, QSqlTableModel
#
# # db = QSqlDatabase.addDatabase('QPSQL')
# # db.setHostName('5432')  # Имя хоста базы данных (localhost, если локальная база данных)
# # db.setDatabaseName('TRZBD')  # Имя базы данных
# # db.setUserName('admin')  # Имя пользователя базы данных
# # db.setPassword('admin!')  # Пароль пользователя базы данных
# connection = psycopg2.connect(host="localhost", port=5432, database="TRZBD", user="admin", password="admin!")
# cursor = connection.cursor()
# print(cursor.execute("SELECT * FROM \"room\""))
# cursor.close()
# connection.close()
# if not connection:
#     print('Не удалось подключиться к базе данных!')
#     sys.exit(1)
# print('Удалось')

# import sys
# from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel
#
# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Главное окно")
#         self.setGeometry(100, 100, 300, 300)
#
#         self.label = QLabel("Добро пожаловать!", self)
#         self.label.setGeometry(50, 50, 200, 50)
#
#         self.button = QPushButton("Вход", self)
#         self.button.setGeometry(100, 150, 100, 30)
#         self.button.clicked.connect(self.open_admin_window)
#
#     def open_admin_window(self):
#         self.admin_window = AdminWindow()
#         self.admin_window.show()
#         self.close()
#
# class AdminWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Окно администратора")
#         self.setGeometry(100, 100, 300, 200)
#
#         self.label = QLabel("Добро пожаловать, Администратор!", self)
#         self.label.setGeometry(50, 50, 200, 50)
#
# if __name__ == "__main__":
#     app = QApplication([])
#     main_window = MainWindow()
#     main_window.show()
#     sys.exit(app.exec())



# from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton
# from PySide6.QtCore import Qt
#
# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#
#         # Создаем виджет и устанавливаем его в главное окно
#         self.central_widget = QWidget()
#         self.setCentralWidget(self.central_widget)
#
#         # Создаем вертикальный контейнерный макет
#         self.layout = QVBoxLayout(self.central_widget)
#
#         # Создаем кнопки
#         self.button1 = QPushButton("Button 1")
#         self.button2 = QPushButton("Button 2")
#         self.button3 = QPushButton("Button 3")
#         self.button4 = QPushButton("Button 4")
#
#         # Добавляем кнопки в макет
#         self.layout.addWidget(self.button1)
#         self.layout.addWidget(self.button2)
#         self.layout.addWidget(self.button3)
#         self.layout.addWidget(self.button4)
#
#         # Подключаем метод "button_clicked" к сигналу "clicked" каждой кнопки
#         self.button1.clicked.connect(lambda: self.button_clicked(self.button1))
#         self.button2.clicked.connect(lambda: self.button_clicked(self.button2))
#         self.button3.clicked.connect(lambda: self.button_clicked(self.button3))
#         self.button4.clicked.connect(lambda: self.button_clicked(self.button4))
#
#     def button_clicked(self, clicked_button):
#         # Перебираем все кнопки и устанавливаем/снимаем свойство "checked" в зависимости от нажатия
#         for button in [self.button1, self.button2, self.button3, self.button4]:
#             if button == clicked_button:
#                 button.setChecked(True)
#             else:
#                 button.setChecked(False)
#
# if __name__ == "__main__":
#     app = QApplication([])
#     window = MainWindow()
#     window.show()
#     app.exec()


# from PySide6.QtWidgets import QApplication, QTableWidget, QTableWidgetItem
# import sys
# import psycopg2
#
#
# class DatabaseApp(QApplication):
#     def __init__(self):
#         super().__init__(sys.argv)
#         self.init_ui()
#
#     def init_ui(self):
#         # Создайте окно приложения
#         window = QTableWidget()
#
#         # Подключение к базе данных
#         connection = psycopg2.connect(
#             user="admin",
#             password="admin!",
#             host="localhost",
#             port="5432",
#             database="TRZBD"
#         )
#
#         # Создание курсора для выполнения SQL-запросов
#         cursor = connection.cursor()
#
#         # Выполните SQL-запрос для получения данных из таблицы
#         cursor.execute("SELECT * FROM room")
#         data = cursor.fetchall()
#
#         # Закройте курсор и соединение
#         cursor.close()
#         connection.close()
#
#         # Отобразите данные в таблице
#         window.setRowCount(len(data))
#         window.setColumnCount(len(data[0]))
#
#         for i, row in enumerate(data):
#             for j, value in enumerate(row):
#                 item = QTableWidgetItem(str(value))
#                 window.setItem(i, j, item)
#
#         # Отобразите окно
#         window.show()
#
#         sys.exit(self.exec())
#
# if __name__ == '__main__':
#     app = DatabaseApp()


# import name
#
#
# table = name.BUTTONS_TABLE['lib_btn']
# print(table)


from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        button_open_new_window = QPushButton('Open New Window', self)
        button_open_new_window.clicked.connect(self.open_new_window)
        layout.addWidget(button_open_new_window)

        self.setLayout(layout)
        self.setWindowTitle('Main Window')

    def open_new_window(self):
        self.new_window = NewWindow(self)
        self.new_window.show()

class NewWindow(QWidget):
    def __init__(self, main_window):
        super().__init__()

        self.main_window = main_window
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        button_back = QPushButton('Back to Main Window', self)
        button_back.clicked.connect(self.back_to_main_window)
        layout.addWidget(button_back)

        self.setLayout(layout)
        self.setWindowTitle('New Window')

    def back_to_main_window(self):
        self.close()
        self.main_window.show()

if __name__ == '__main__':
    app = QApplication([])
    main_window = MainWindow()
    main_window.show()
    app.exec()

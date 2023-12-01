import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLineEdit, QTableWidgetItem, QHeaderView
import login_ui
import librarian_ui
import admin_ui
import psycopg2
import name

con_bul = True
try:
    connection = psycopg2.connect(
        user="admin",
        password="admin!",
        host="localhost",
        port="5432",
        database="TRZBD"
    )
    if not connection:
        con_bul = False
except psycopg2.OperationalError:
    con_bul = False


class Log_in(QMainWindow):
    def __init__(self):
        super(Log_in, self).__init__()
        self.ui = login_ui.Ui_Login()
        self.ui.setupUi(self)

        # Создаем атрибут класса для нового окна
        self.new_window = None

        # Проверка подключения к БД
        if not con_bul:
            self.ui.label_error.setText('Сбой подключения к базе данных')

        # видимость пароля
        self.ui.pushButton.clicked.connect(self.visibility_password)
        # при загрузке скрыть пароль
        self.ui.lineEdit_password.setEchoMode(QLineEdit.Password)

        # вход в базу
        self.ui.login_btn.clicked.connect(self.open_new_window)

    def visibility_password(self) -> None:
        if self.ui.pushButton.isChecked():
            self.ui.lineEdit_password.setEchoMode(QLineEdit.Normal)
        else:
            self.ui.lineEdit_password.setEchoMode(QLineEdit.Password)

    def open_new_window(self) -> None:
        # login = self.ui.lineEdit_login.text()
        # password = self.ui.lineEdit_password.text()
        # if login and password:
        #     if con_bul:
        #         cursor = connection.cursor()
        #         query = f"SELECT type_user FROM Users_table WHERE login = '{login}' AND password = '{password}'"
        #         cursor.execute(query)
        #         user = cursor.fetchone()
        #         # Проверяем, есть ли пользователь с указанным логином и паролем
        #         if user:
        #             if user[0] == 'admin':
        #                 self.new_window = Admin_window()
        #                 self.new_window.show()
        #                 self.hide()
        #             else:
        #                 self.new_window = librarian_window()
        #                 self.new_window.show()
        #                 self.hide()
        #             self.ui.lineEdit_login.setText('')
        #             self.ui.lineEdit_password.setText('')
        #             self.ui.label_error.setText('')
        #         else:
        #             self.ui.label_error.setText('Неверный логин или пароль')
        #         cursor.close()
        self.new_window = Admin_window()
        self.new_window.show()
        self.hide()


class Admin_window(QMainWindow):
    def __init__(self):
        super(Admin_window, self).__init__()
        self.ui = admin_ui.Ui_MainWindow()
        self.ui.setupUi(self)

        # Установка первой таблицы
        self.ui.lib_btn.setChecked(True)
        self.table_from_database('lib_btn')

        # кнопки отвечающие за вывод таблиц из бд
        for btn in name.LIST_BUTTON:
            getattr(self.ui, btn).clicked.connect(self.button_clicked)
        # self.ui.tableWidget.horizontalHeader().setStretchLastSection(True)

        # Выход в логин
        self.ui.logout_btn.clicked.connect(self.logout)

        # Сохранить данные
        self.ui.safe_btn.clicked.connect(self.get_checked_button)

    def button_clicked(self) -> None:
        sender_button = self.sender()
        for button in name.LIST_BUTTON:
            btn = getattr(self.ui, button)
            if btn == sender_button:
                btn.setChecked(True)
                self.table_from_database(button)
            else:
                btn.setChecked(False)

    def table_from_database(self, sender_btn) -> None:
        # Создание курсора для выполнения SQL-запросов
        cursor = connection.cursor()
        # Извлечение названия таблицы
        table = name.BUTTONS_TABLE[str(sender_btn)]
        # Выполните SQL-запрос для получения данных из таблицы
        cursor.execute(f"SELECT * FROM {table}")
        data = cursor.fetchall()
        # Получение заголовков столбцов
        column_names = [desc[0] for desc in cursor.description]
        # Установка заголовков в QTableWidget
        self.ui.tableWidget.setColumnCount(len(column_names))
        self.ui.tableWidget.setHorizontalHeaderLabels(column_names)
        # Отобразите данные в таблице
        self.ui.tableWidget.setRowCount(len(data))
        self.ui.tableWidget.setColumnCount(len(data[0]))
        for i, row in enumerate(data):
            for j, value in enumerate(row):
                item = QTableWidgetItem(str(value))
                self.ui.tableWidget.setItem(i, j, item)
        # Устанавливаем ширину таблицы равной ширине родительского виджета (QMainWindow)
        # Устанавливаем таблицу в центр основного виджета
        # self.setCentralWidget(self.ui.tableWidget)
        # Устанавливаем горизонтальные заголовки
        # self.ui.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        # self.ui.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.tableWidget.resizeColumnsToContents()
        # Закрытие курсора
        cursor.close()

    def logout(self):
        self.close()
        window.show()
        # self.new_window = librarian_window()
        # self.new_window.show()
        # self.hide()

    def get_checked_button(self) -> None:
        for button in name.LIST_BUTTON:
            if getattr(self.ui, button).isChecked():
                self.save_changes(button)

    def save_changes(self, button) -> None:
        # Создание курсора для выполнения SQL-запросов
        cursor = connection.cursor()
        for row in range(self.ui.tableWidget.rowCount()):
            tuple_item = ()
            for col in range(self.ui.tableWidget.columnCount()):
                # ПОСТРОЧНА ЗАПИСИ ВЫТАСКИВАЕМ
                tuple_item = tuple_item + (self.ui.tableWidget.item(row, col).text(),)
            tuple_item = tuple_item[1:] + (tuple_item[0],)
            cursor.execute(name.UPDATES_TABLE[button], tuple_item)
        connection.commit()
        cursor.close()


class librarian_window(QMainWindow):
    def __init__(self):
        super(librarian_window, self).__init__()
        self.ui = librarian_ui.Ui_MainWindow()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Log_in()
    window.show()

    sys.exit(app.exec())

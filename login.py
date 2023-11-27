import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLineEdit, QTableWidgetItem
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

        # вход в базу
        self.ui.login_btn.clicked.connect(self.open_new_window)

    def visibility_password(self) -> None:
        if self.ui.pushButton.isChecked():
            self.ui.lineEdit_password.setEchoMode(QLineEdit.Normal)
        else:
            self.ui.lineEdit_password.setEchoMode(QLineEdit.Password)

    def open_new_window(self) -> None:
        login = self.ui.lineEdit_login.text()
        password = self.ui.lineEdit_password.text()

        if con_bul:
            cursor = connection.cursor()
            query = f"SELECT type_user FROM Users_table WHERE login = '{login}' AND password = '{password}'"
            cursor.execute(query)
            user = cursor.fetchone()

            # Проверяем, есть ли пользователь с указанным логином и паролем
            if user:
                self.ui.label_error.setText('Успешный вход')
                if user[0] == 'admin':
                    self.new_window = Admin_window()
                    self.new_window.show()
                    self.hide()
                else:
                    self.new_window = librarian_window()
                    self.new_window.show()
                    self.hide()
            else:
                self.ui.label_error.setText('Неверный логин или пароль')
            cursor.close()


class Admin_window(QMainWindow):
    def __init__(self):
        super(Admin_window, self).__init__()
        self.ui = admin_ui.Ui_MainWindow()
        self.ui.setupUi(self)

        # кнопки отвечающие за вывод таблиц из бд
        for btn in name.BUTTONS_TABLE:
            getattr(self.ui, btn).clicked.connect(self.button_clicked)
        #
        # # Подключение к базе данных
        # connection = psycopg2.connect(
        #     user="admin",
        #     password="admin!",
        #     host="localhost",
        #     port="5432",
        #     database="TRZBD"
        # )
        #
        # # Создание курсора для выполнения SQL-запросов
        # cursor = connection.cursor()
        #
        # # Выполните SQL-запрос для получения данных из таблицы
        # cursor.execute("SELECT * FROM library")
        # data = cursor.fetchall()
        #
        # # Отобразите данные в таблице
        # self.ui.tableWidget.setRowCount(len(data))
        # self.ui.tableWidget.setColumnCount(len(data[0]))
        #
        # for i, row in enumerate(data):
        #     for j, value in enumerate(row):
        #         item = QTableWidgetItem(str(value))
        #         self.ui.tableWidget.setItem(i, j, item)
        #
        # # Закройте курсор и соединение
        # cursor.close()
        # connection.close()

    def button_clicked(self) -> None:
        sender_button = self.sender()
        for button in [self.ui.lib_btn, self.ui.room_btn, self.ui.book_btn, self.ui.readers_btn, self.ui.is_btn]:
            if button != sender_button:
                button.setChecked(False)
            else:
                sender_button.setChecked(True)
        self.table_from_database(sender_button)

    def table_from_database(self, sender_btn) -> None:
        # # Создание курсора для выполнения SQL-запросов
        # cursor = connection.cursor()
        #
        # # Выполните SQL-запрос для получения данных из таблицы
        # cursor.execute(f"SELECT * FROM {name.BUTTONS_TABLE[str(sender_btn)]}")
        # data = cursor.fetchall()
        #
        # # Отобразите данные в таблице
        # self.ui.tableWidget.setRowCount(len(data))
        # self.ui.tableWidget.setColumnCount(len(data[0]))
        #
        # for i, row in enumerate(data):
        #     for j, value in enumerate(row):
        #         item = QTableWidgetItem(str(value))
        #         self.ui.tableWidget.setItem(i, j, item)
        #
        # # Закройте курсор и соединение
        # cursor.close()
        pass


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
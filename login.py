import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLineEdit, QTableWidgetItem, QHeaderView, QFormLayout, QDialog
import login_ui
import librarian_ui
import admin_ui
import psycopg2
import name


new_row = 0
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
        for btn in name.LIST_BUTTON_TABLE:
            getattr(self.ui, btn).clicked.connect(self.button_clicked)
        # self.ui.tableWidget.horizontalHeader().setStretchLastSection(True)

        # Выход в логин
        self.ui.logout_btn.clicked.connect(self.logout)

        # Сохранить данные
        self.ui.safe_btn.clicked.connect(self.get_checked_button)
        # создать новой записи
        self.ui.new_btn.clicked.connect(self.get_checked_button)
        # Удаление записи
        self.ui.del_btn.clicked.connect(self.get_checked_button)

    def button_clicked(self) -> None:
        sender_button = self.sender()
        for button in name.LIST_BUTTON_TABLE:
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
        self.ui.tableWidget.sortItems(0)

    def logout(self):
        self.close()
        window.show()
        # self.new_window = librarian_window()
        # self.new_window.show()
        # self.hide()

    def get_checked_button(self) -> None:
        for button in name.LIST_BUTTON_TABLE:
            if getattr(self.ui, button).isChecked():
                for btn in name.LIST_BUTTON_MANAGEMENT:
                    if getattr(self.ui, btn) == self.sender():
                        getattr(self, name.BUTTON_MANAGEMENT[btn])(button)
                # self.save_changes(button)

    def save_changes(self, button) -> None:
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

    def new_row_interface(self, button) -> None:
        # Получаем количество строк в таблице
        current_row_count = self.ui.tableWidget.rowCount()
        # Вставляем новую строку в таблицу
        self.ui.tableWidget.insertRow(current_row_count)
        # Заполняем новую строку пустыми ячейками
        for column in range(self.ui.tableWidget.columnCount()):
            if column == 0:
                item = self.ui.tableWidget.item(current_row_count - 1, 0).text()
                item = QTableWidgetItem(str(int(item) + 1))
            else:
                item = QTableWidgetItem("")
            self.ui.tableWidget.setItem(current_row_count, column, item)
        # new_row += 1
        self.new_row_db(button)

    def new_row_db(self, button) -> None:
        cursor = connection.cursor()
        row = self.ui.tableWidget.rowCount() - 1
        tuple_item = ()
        for col in range(self.ui.tableWidget.columnCount()):
            # ПОСТРОЧНА ЗАПИСИ ВЫТАСКИВАЕМ
            tuple_item = tuple_item + (self.ui.tableWidget.item(row, col).text(),)
        cursor.execute(name.INSERT_TABLE[button], tuple_item)
        connection.commit()
        cursor.close()

    def delete_row(self, button):
        selected_row = self.ui.tableWidget.currentRow()
        if selected_row >= 0:
            self.ui.tableWidget.removeRow(selected_row)
            cursor = connection.cursor()
            cursor.execute(name.DELETE_TABLE[button], str(selected_row+1))
            connection.commit()
            cursor.close()

    def editing(self):
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

import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QLabel
import sqlite3
from ui_file import Ui_MainWindow
from ui_file_1 import Ui_MainWindow_1


class MyWidget(QMainWindow):
    def __init__(self):
        super(MyWidget, self).__init__()
        self.ui = Ui_MainWindow_1()
        self.ui_1 = Ui_MainWindow()
        self.ui.setupUi(self)
        self.conn = sqlite3.connect('coffee.sqlite')
        self.ui.pushButton.clicked.connect(self.run)
        self.ui.pushButton_2.clicked.connect(self.change)

    def change(self):
        self.ui_1.setupUi(self)
        self.ui_1.radioButton.clicked.connect(self.adding)
        self.ui_1.radioButton_2.clicked.connect(self.adding)
        self.ui_1.text = QLabel()
        self.whatwedo = str()
        self.ui_1.statusbar.addWidget(self.ui_1.text)
        self.ui_1.label.hide()
        self.ui_1.pushButton_4.hide()
        self.ui_1.plainTextEdit_4.hide()
        self.ui_1.comboBox.addItems(['молотый', 'зерновой'])
        self.ui_1.comboBox_2.addItems(['итальянская', 'сильная', 'средняя', 'слабая'])
        self.ui_1.pushButton_3.clicked.connect(self.add)

    def adding(self):
        if self.ui_1.radioButton.isChecked():
            self.whatwedo = 'add'
            self.ui_1.label_2.show()
            self.ui_1.label_3.show()
            self.ui_1.label_4.show()
            self.ui_1.label_5.show()
            self.ui_1.label_6.show()
            self.ui_1.label_7.show()
            self.ui_1.plainTextEdit_3.show()
            self.ui_1.comboBox_2.show()
            self.ui_1.plainTextEdit.show()
            self.ui_1.plainTextEdit_5.show()
            self.ui_1.plainTextEdit_6.show()
            self.ui_1.label.hide()
            self.ui_1.plainTextEdit_4.hide()
            self.ui_1.pushButton_4.hide()
            self.ui_1.comboBox.show()
        elif self.ui_1.radioButton_2.isChecked():
            self.whatwedo = 'change'
            self.ui_1.label.show()
            self.ui_1.plainTextEdit_4.show()
            self.ui_1.label_2.hide()
            self.ui_1.label_3.hide()
            self.ui_1.label_4.hide()
            self.ui_1.label_5.hide()
            self.ui_1.label_6.hide()
            self.ui_1.label_7.hide()
            self.ui_1.plainTextEdit_3.hide()
            self.ui_1.comboBox_2.hide()
            self.ui_1.plainTextEdit.hide()
            self.ui_1.plainTextEdit_5.hide()
            self.ui_1.plainTextEdit_6.hide()
            self.ui_1.comboBox.hide()
            self.ui_1.pushButton_4.show()
            self.ui_1.pushButton_4.clicked.connect(self.searching)
        else:
            self.whatwedo = 'aa'

    def searching(self):
        cur = self.conn.cursor()
        request = 'SELECT title from name WHERE id=' + self.ui_1.plainTextEdit_4.toPlainText()
        res = cur.execute(request).fetchall()
        if len(res) != 0:
            self.ui_1.text.setText('')
            self.ui_1.plainTextEdit_4.show()
            self.ui_1.label_2.show()
            self.ui_1.label_3.show()
            self.ui_1.label_4.show()
            self.ui_1.label_5.show()
            self.ui_1.label_6.show()
            self.ui_1.label_7.show()
            self.ui_1.plainTextEdit_3.show()
            self.ui_1.comboBox_2.show()
            self.ui_1.plainTextEdit.show()
            self.ui_1.plainTextEdit_5.show()
            self.ui_1.plainTextEdit_6.show()
            self.ui_1.comboBox.show()
            self.ui_1.plainTextEdit_3.setPlainText(str(res[0][0]))
            request = 'SELECT roasting from roasting WHERE id=' + self.ui_1.plainTextEdit_4.toPlainText()
            res = cur.execute(request).fetchall()
            self.ui_1.comboBox_2.setCurrentText(str(res[0][0]))
            request = 'SELECT type from type WHERE id=' + self.ui_1.plainTextEdit_4.toPlainText()
            res = cur.execute(request).fetchall()
            self.ui_1.comboBox.setCurrentText(str(res[0][0]))
            request = 'SELECT about from taste WHERE id=' + self.ui_1.plainTextEdit_4.toPlainText()
            res = cur.execute(request).fetchall()
            self.ui_1.plainTextEdit.setPlainText(str(res[0][0]))
            request = 'SELECT volume from volume WHERE id=' + self.ui_1.plainTextEdit_4.toPlainText()
            res = cur.execute(request).fetchall()
            self.ui_1.plainTextEdit_5.setPlainText(str(res[0][0]))
            request = 'SELECT price from price WHERE id=' + self.ui_1.plainTextEdit_4.toPlainText()
            res = cur.execute(request).fetchall()
            self.ui_1.plainTextEdit_6.setPlainText(str(res[0][0]))
        else:
            self.ui_1.text.setText("Такого id нет")

    def add(self):
        name = self.ui_1.plainTextEdit_3.toPlainText()
        roasting = self.ui_1.comboBox_2.currentText()
        taste = self.ui_1.plainTextEdit.toPlainText()
        volume = self.ui_1.plainTextEdit_5.toPlainText()
        price = self.ui_1.plainTextEdit_6.toPlainText()
        type = self.ui_1.comboBox.currentText()
        if self.whatwedo == 'add':
            if len(name) == 0 or len(roasting) == 0 or len(taste) == 0 or len(volume) == 0 or \
                    len(price) == 0 or len(type) == 0:
                self.ui_1.text.setText('Заполнены не все данные')
            elif not volume.isdigit() or not price.isdigit():
                self.ui_1.text.setText('Объем и цена - численные значения')
            else:
                cur = self.conn.cursor()
                request = "INSERT INTO name(title) VALUES('" + name + "')"
                cur.execute(request)
                request = "INSERT INTO roasting(roasting) VALUES('" + roasting + "')"
                cur.execute(request)
                request = "INSERT INTO taste(about) VALUES('" + taste + "')"
                cur.execute(request)
                request = "INSERT INTO volume(volume) VALUES('" + volume + "')"
                cur.execute(request)
                request = "INSERT INTO price(price) VALUES('" + price + "')"
                cur.execute(request)
                request = "INSERT INTO type(type) VALUES('" + type + "')"
                cur.execute(request)
                self.conn.commit()
                self.ui.setupUi(self)
                self.conn = sqlite3.connect('coffee.sqlite')
                self.ui.pushButton.clicked.connect(self.run)
                self.ui.pushButton_2.clicked.connect(self.change)
        elif self.whatwedo == 'change':
            cur = self.conn.cursor()
            request = "UPDATE name SET title ='" + name + "' WHERE id=" + self.ui_1.plainTextEdit_4.toPlainText()
            cur.execute(request)
            request = "UPDATE roasting SET roasting ='" + \
                      roasting + "' WHERE id=" + self.ui_1.plainTextEdit_4.toPlainText()
            cur.execute(request)
            request = "UPDATE taste SET about ='" + taste + "' WHERE id=" + self.ui_1.plainTextEdit_4.toPlainText()
            cur.execute(request)
            request = "UPDATE volume SET volume ='" + volume + "' WHERE id=" + self.ui_1.plainTextEdit_4.toPlainText()
            cur.execute(request)
            request = "UPDATE price SET price ='" + price + "' WHERE id=" + self.ui_1.plainTextEdit_4.toPlainText()
            cur.execute(request)
            request = "UPDATE type SET type ='" + type + "' WHERE id=" + self.ui_1.plainTextEdit_4.toPlainText()
            cur.execute(request)
            self.conn.commit()
            self.ui.setupUi(self)
            self.conn = sqlite3.connect('coffee.sqlite')
            self.ui.pushButton.clicked.connect(self.run)
            self.ui.pushButton_2.clicked.connect(self.change)
        else:
            self.ui_1.text.setText('Ничего не выбрано')

    def run(self):
        self.ui.tableWidget.setColumnCount(7)
        self.ui.tableWidget.setHorizontalHeaderLabels(
            ['ID', 'название сорта', 'степень обжарки',
             'молотый/в зернах', 'описание вкуса', 'цена', 'объем упаковки'])
        self.ui.tableWidget.setRowCount(0)
        request = "SELECT name.id,\n"
        request += "name.title, \n"
        request += "roasting.roasting, \n"
        request += "type.type, \n"
        request += "taste.about, \n"
        request += "price.price, \n"
        request += "volume.volume \n"
        request += "from name \n"
        request += "LEFT JOIN roasting ON name.id = roasting.id \n"
        request += "LEFT JOIN type ON name.id = type.id \n"
        request += "LEFT JOIN taste ON name.id = taste.id \n"
        request += "LEFT JOIN price ON name.id = price.id \n"
        request += "LEFT JOIN volume ON name.id = volume.id \n"
        request += "ORDER BY name.id;"
        cur = self.conn.cursor()
        res = cur.execute(request).fetchall()
        for i in range(len(res)):
            self.ui.tableWidget.setRowCount(
                self.ui.tableWidget.rowCount() + 1)
            for j in range(7):
                self.ui.tableWidget.setItem(
                    i, j, QTableWidgetItem(str(res[i][j])))
        self.ui.tableWidget.resizeColumnsToContents()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = MyWidget()
    form.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())

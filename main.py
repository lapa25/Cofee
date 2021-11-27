import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QLabel
import sqlite3
from PyQt5 import uic


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.conn = sqlite3.connect('coffee.sqlite')
        self.pushButton.clicked.connect(self.run)
        self.pushButton_2.clicked.connect(self.change)

    def change(self):
        uic.loadUi('addEditCoffeeForm.ui', self)
        self.radioButton.clicked.connect(self.adding)
        self.radioButton_2.clicked.connect(self.adding)
        self.text = QLabel()
        self.whatwedo = str()
        self.statusbar.addWidget(self.text)
        self.label.hide()
        self.pushButton_4.hide()
        self.plainTextEdit_4.hide()
        self.comboBox.addItems(['молотый', 'зерновой'])
        self.comboBox_2.addItems(['итальянская', 'сильная', 'средняя', 'слабая'])
        self.pushButton_3.clicked.connect(self.add)

    def adding(self):
        if self.radioButton.isChecked():
            self.whatwedo = 'add'
            self.label_2.show()
            self.label_3.show()
            self.label_4.show()
            self.label_5.show()
            self.label_6.show()
            self.label_7.show()
            self.plainTextEdit_3.show()
            self.comboBox_2.show()
            self.plainTextEdit.show()
            self.plainTextEdit_5.show()
            self.plainTextEdit_6.show()
            self.label.hide()
            self.plainTextEdit_4.hide()
            self.pushButton_4.hide()
            self.comboBox.show()
        elif self.radioButton_2.isChecked():
            self.whatwedo = 'change'
            self.label.show()
            self.plainTextEdit_4.show()
            self.label_2.hide()
            self.label_3.hide()
            self.label_4.hide()
            self.label_5.hide()
            self.label_6.hide()
            self.label_7.hide()
            self.plainTextEdit_3.hide()
            self.comboBox_2.hide()
            self.plainTextEdit.hide()
            self.plainTextEdit_5.hide()
            self.plainTextEdit_6.hide()
            self.comboBox.hide()
            self.pushButton_4.show()
            self.pushButton_4.clicked.connect(self.searching)
        else:
            self.whatwedo = 'aa'

    def searching(self):
        cur = self.conn.cursor()
        request = 'SELECT title from name WHERE id=' + self.plainTextEdit_4.toPlainText()
        res = cur.execute(request).fetchall()
        if len(res) != 0:
            self.text.setText('')
            self.plainTextEdit_4.show()
            self.label_2.show()
            self.label_3.show()
            self.label_4.show()
            self.label_5.show()
            self.label_6.show()
            self.label_7.show()
            self.plainTextEdit_3.show()
            self.comboBox_2.show()
            self.plainTextEdit.show()
            self.plainTextEdit_5.show()
            self.plainTextEdit_6.show()
            self.comboBox.show()
            self.plainTextEdit_3.setPlainText(str(res[0][0]))
            request = 'SELECT roasting from roasting WHERE id=' + self.plainTextEdit_4.toPlainText()
            res = cur.execute(request).fetchall()
            self.comboBox_2.setCurrentText(str(res[0][0]))
            request = 'SELECT type from type WHERE id=' + self.plainTextEdit_4.toPlainText()
            res = cur.execute(request).fetchall()
            self.comboBox.setCurrentText(str(res[0][0]))
            request = 'SELECT about from taste WHERE id=' + self.plainTextEdit_4.toPlainText()
            res = cur.execute(request).fetchall()
            self.plainTextEdit.setPlainText(str(res[0][0]))
            request = 'SELECT volume from volume WHERE id=' + self.plainTextEdit_4.toPlainText()
            res = cur.execute(request).fetchall()
            self.plainTextEdit_5.setPlainText(str(res[0][0]))
            request = 'SELECT price from price WHERE id=' + self.plainTextEdit_4.toPlainText()
            res = cur.execute(request).fetchall()
            self.plainTextEdit_6.setPlainText(str(res[0][0]))
        else:
            self.text.setText("Такого id нет")

    def add(self):
        name = self.plainTextEdit_3.toPlainText()
        roasting = self.comboBox_2.currentText()
        taste = self.plainTextEdit.toPlainText()
        volume = self.plainTextEdit_5.toPlainText()
        price = self.plainTextEdit_6.toPlainText()
        type = self.comboBox.currentText()
        if self.whatwedo == 'add':
            if len(name) == 0 or len(roasting) == 0 or len(taste) == 0 or len(volume) == 0 or \
                    len(price) == 0 or len(type) == 0:
                self.text.setText('Заполнены не все данные')
            elif not volume.isdigit() or not price.isdigit():
                self.text.setText('Объем и цена - численные значения')
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
                uic.loadUi('main.ui', self)
                self.conn = sqlite3.connect('coffee.sqlite')
                self.pushButton.clicked.connect(self.run)
                self.pushButton_2.clicked.connect(self.change)
        elif self.whatwedo == 'change':
            cur = self.conn.cursor()
            request = "UPDATE name SET title ='" + name + "' WHERE id=" + self.plainTextEdit_4.toPlainText()
            cur.execute(request)
            request = "UPDATE roasting SET roasting ='" + roasting + "' WHERE id=" + self.plainTextEdit_4.toPlainText()
            cur.execute(request)
            request = "UPDATE taste SET about ='" + taste + "' WHERE id=" + self.plainTextEdit_4.toPlainText()
            cur.execute(request)
            request = "UPDATE volume SET volume ='" + volume + "' WHERE id=" + self.plainTextEdit_4.toPlainText()
            cur.execute(request)
            request = "UPDATE price SET price ='" + price + "' WHERE id=" + self.plainTextEdit_4.toPlainText()
            cur.execute(request)
            request = "UPDATE type SET type ='" + type + "' WHERE id=" + self.plainTextEdit_4.toPlainText()
            cur.execute(request)
            self.conn.commit()
            uic.loadUi('main.ui', self)
            self.conn = sqlite3.connect('coffee.sqlite')
            self.pushButton.clicked.connect(self.run)
            self.pushButton_2.clicked.connect(self.change)
        else:
            self.text.setText('Ничего не выбрано')

    def run(self):
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setHorizontalHeaderLabels(
            ['ID', 'название сорта', 'степень обжарки',
             'молотый/в зернах', 'описание вкуса', 'цена', 'объем упаковки'])
        self.tableWidget.setRowCount(0)
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
            self.tableWidget.setRowCount(
                self.tableWidget.rowCount() + 1)
            for j in range(7):
                self.tableWidget.setItem(
                    i, j, QTableWidgetItem(str(res[i][j])))
        self.tableWidget.resizeColumnsToContents()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = MyWidget()
    form.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())

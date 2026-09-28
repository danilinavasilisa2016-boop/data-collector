import csv
import os
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QMessageBox
from ui_table_window import Ui_TableWindow
from data_reader import get_data

CSV_FILE = "data.csv"


class TableWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_TableWindow()
        self.ui.setupUi(self)

        self.ui.btnRead.clicked.connect(self.add_row)
        self.ui.btnSave.clicked.connect(self.save_data)
        self.ui.btnClear.clicked.connect(self.clear_table)

    def add_row(self):
        data = get_data()
        if not data:
            return
        row = self.ui.tableWidget.rowCount()
        self.ui.tableWidget.insertRow(row)
        for col, value in enumerate(data):
            self.ui.tableWidget.setItem(row, col, QTableWidgetItem(str(value)))

    def save_data(self):
        file_exists = os.path.isfile(CSV_FILE)
        with open(CSV_FILE, "a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            if not file_exists:
                writer.writerow(["Температура", "Влажность", "Освещение"])
            for r in range(self.ui.tableWidget.rowCount()):
                row_data = []
                for c in range(self.ui.tableWidget.columnCount()):
                    item = self.ui.tableWidget.item(r, c)
                    row_data.append(item.text() if item else "")
                writer.writerow(row_data)
        QMessageBox.information(self, "Сохранение", f"Данные сохранены в {CSV_FILE}")

    def clear_table(self):
        self.ui.tableWidget.setRowCount(0)
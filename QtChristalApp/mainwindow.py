# This Python file uses the following encoding: utf-8
import os
from pathlib import Path
import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QLabel, QDialog, QVBoxLayout, QHBoxLayout, QGridLayout, QProgressBar, QSpacerItem, QSizePolicy,QComboBox
from PySide6.QtCore import QFile, QSize, Qt
from PySide6.QtUiTools import QUiLoader
from PySide6.QtGui import QIcon, QPixmap, QPalette, QColor, QFont, QFontDatabase

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.load_ui()

    def load_ui(self):
        loader = QUiLoader()
        path = os.fspath(Path(__file__).resolve().parent / "form.ui")
        ui_file = QFile(path)
        ui_file.open(QFile.ReadOnly)
        loader.load(ui_file, self)
        ui_file.close()


if __name__ == "__main__":
    app = QApplication([])
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec_())

# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QFileDialog
from PySide6.QtGui import QPixmap
#from imageSettings import

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.bouton_ouvrirImgIn.clicked.connect(self.ouvrirImage)

    def ouvrirImage(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(self, "Sélectionner une image", "", "Images (*.png *.jpg *.jpeg *.gif *.bmp)", options=options)
        if fileName:
            self.ui.labeltext_chemin.setText(fileName)
            pixmap = QPixmap(fileName)
            self.ui.label_ImgIn.setPixmap(pixmap)
            self.ui.label_ImgIn.setScaledContents(True)





if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())

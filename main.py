import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui


class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.button = QtWidgets.QPushButton("Click me!")
        self.buttonSecond = QtWidgets.QPushButton("Hello")

        self.text = QtWidgets.QLabel("Hello World",
                                     alignment=QtCore.Qt.AlignCenter)
        self.textSecond = QtWidgets.QLabel(
            "1", alignment=QtCore.Qt.AlignCenter)

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.buttonSecond)

        self.buttonSecond.clicked.connect(self.randomMagicNumber)

    @QtCore.Slot()
    def randomMagicNumber(self):
        self.text.setText(str(random.randint(0, 100)))


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())

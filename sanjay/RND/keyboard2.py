from PyQt5.QtWidgets import QDialog, QApplication, QLineEdit, QPushButton
from PyQt5.QtCore import Qt, QRect, pyqtSignal, pyqtSlot
import sys


class FirstWindow(QDialog):
    def __init__(self, parent=None):
        super(FirstWindow, self).__init__(parent)

        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setFixedSize(400, 400)

        self.second_window = SecondWindow()

        self.button_go_second_window = QPushButton(self)
        self.button_go_second_window.setGeometry(QRect(40, 150, 220, 50))
        self.button_go_second_window.setStyleSheet(
            "QPushButton { background-color: rgba(63, 142, 191, 255); color : rgba(242, 242, 242, 255) }"
        )

        self.button_go_second_window.clicked.connect(self.go_second_window)
        self.second_window.sendDataSignal.connect(self.receive_data_slot)

    @pyqtSlot()
    def go_second_window(self):
        self.second_window.show()

    @pyqtSlot(str)
    def receive_data_slot(self, text):
        self.button_go_second_window.setText(text)


class SecondWindow(QDialog):
    sendDataSignal = pyqtSignal(str)

    def __init__(self, parent=None):

        super(SecondWindow, self).__init__(parent)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setFixedSize(400, 400)

        self.field = QLineEdit(self)
        self.field.move(40, 100)
        self.button_send_data_back = QPushButton(self)
        self.button_send_data_back.setText("Send")
        self.button_send_data_back.setGeometry(QRect(40, 150, 220, 50))
        self.button_send_data_back.setStyleSheet(
            "QPushButton { background-color: rgba(63, 142, 191, 255); color : rgba(242, 242, 242, 255) }"
        )
        self.button_send_data_back.clicked.connect(self.send_data_back)

    @pyqtSlot()
    def send_data_back(self):
        self.sendDataSignal.emit(self.field.text())
        self.field.clear()
        self.close()


if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = FirstWindow()
    window.show()
    sys.exit(App.exec())
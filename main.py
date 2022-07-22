import sys

from PyQt5.QtWidgets import QApplication

from screens.todo import ToDo

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ToDo()
    window.show()
    app.exec()

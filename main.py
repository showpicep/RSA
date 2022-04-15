import sys
from PyQt5.QtWidgets import QApplication
from modules.interface import UIWindow


def application():
    app = QApplication(sys.argv)
    main_window = UIWindow()
    main_window.show()
    app.exec_()


if __name__ == '__main__':
    application()

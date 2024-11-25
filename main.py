from main_ui import MainWindow
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QSize
from PySide6.QtGui import QIcon


if __name__ == "__main__":
    
    app = QApplication([])
    app_icon = QIcon()
    app_icon.addFile(r"icons\spotify_icon.ico", QSize(30,30))
    app.setWindowIcon(app_icon)

    window = MainWindow()
    window.show()
    app.exec()

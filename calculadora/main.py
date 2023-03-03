
import sys
from main_window import MainWindow
from display import Display
from PySide6.QtWidgets import QApplication, QLabel
from variables import WINDOW_ICON_PATH
from PySide6.QtGui import QIcon
from styles import setupTheme
from buttons import ButtonsGrid
from info import Info


if __name__ == '__main__':
    # Cria a aplicaçao
    app = QApplication(sys.argv)
    setupTheme()
    window = MainWindow()

    # Define o icone
    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    # Info
    info = Info('0')
    window.addWidgetToVLayout(info)

    # Display
    display = Display()
    window.addWidgetToVLayout(display)

    # Grid
    buttonsGrid = ButtonsGrid(display, info, window)
    window.vLayout.addLayout(buttonsGrid)


    # Executa Tudo
    window.adjustFixedSize()
    window.show()
    app.exec()

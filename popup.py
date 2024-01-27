from PyQt6.QtWidgets import QMessageBox

def ok_popup(window_title:str, text:str):
    popup = QMessageBox()
    popup.setWindowTitle(window_title)
    popup.setText(text)
    popup.exec()
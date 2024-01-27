from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QTabWidget, QLabel
from view import panel_interface

class LogPanel(QWidget, panel_interface.panel):
    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QVBoxLayout(self)
        layout.addWidget(QLabel(f"This is the log panel"))
        self.setLayout(layout)
        
    def get_name(self):
        return "Logs"
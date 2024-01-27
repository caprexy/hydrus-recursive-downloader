import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QTabWidget, QLabel
from view import current_subscription_panel_view, input_panel_view, log_panel_view

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout(self)

        self.tab_widget = QTabWidget(self)

        panels = [
            input_panel_view.InputPanel(),
            current_subscription_panel_view.SubscriptionsPanel(),
            log_panel_view.LogPanel()
        ]
        
        names = [panel.get_name() for panel in panels]

        for panel, name in zip(panels, names):
            self.tab_widget.addTab(panel, name)

        layout.addWidget(self.tab_widget)

        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

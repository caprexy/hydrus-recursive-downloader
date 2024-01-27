from PyQt6.QtWidgets import QLineEdit, QWidget, QGridLayout, QPushButton, QLabel, QComboBox, QMessageBox
from view import panel_interface
from controller import input_panel_controller

class InputPanel(QWidget, panel_interface.panel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.input_panel_controller = input_panel_controller.InputPanelController()
        
        self.layout = QGridLayout(self)
        self.layout.addWidget(QLabel(f"This is the input panel"))
        self.setLayout(self.layout)
        
        self.wanted_id_row(0)
        self.check_subscriptions(1)
        
    def wanted_id_row(self, row: int):
        self.services_dropdown = QComboBox()
        self.layout.addWidget(self.services_dropdown, row, 0)
        
        services = [
            "patreon",
            ""
        ]
        self.services_dropdown.addItems(services)
        
        self.subscription_id_input = QLineEdit("Replace with numerical ID")
        self.layout.addWidget(self.subscription_id_input, row, 1)
        
        self.add_subscription_button = QPushButton("Add subscription",)
        self.add_subscription_button.clicked.connect(
            lambda: self.input_panel_controller.add_subscription(
                self.subscription_id_input.text(),
                self.services_dropdown.currentText()
            ))
        self.layout.addWidget(self.add_subscription_button, row, 2)
        
        self.delete_subscription_button = QPushButton("Delete subscription",)
        self.delete_subscription_button.clicked.connect(self.confirm_delete)
        self.layout.addWidget(self.delete_subscription_button, row, 3)
        
    def check_subscriptions(self, row:int):
        self.check_subscriptions_button = QPushButton("Check subscriptions",)
        self.check_subscriptions_button.clicked.connect(self.confirm_delete)
        self.layout.addWidget(self.check_subscriptions_button, row, 0)
        
    
    def confirm_delete(self):
        confirmation_dialog = QMessageBox()
        confirmation_dialog.setIcon(QMessageBox.Icon.Question)
        confirmation_dialog.setWindowTitle("Confirmation")
        confirmation_dialog.setText("Are you sure?")
        confirmation_dialog.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        result = confirmation_dialog.exec()
        
        if result == QMessageBox.StandardButton.Yes:
            self.input_panel_controller.delete_subscription(self.subscription_id_input.text(), self.services_dropdown.currentText())
        
        
    def get_name(self):
        return "Inputs"
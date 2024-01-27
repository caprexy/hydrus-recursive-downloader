from PyQt6.QtGui import QShowEvent
from PyQt6.QtWidgets import QTableWidget, QWidget, QVBoxLayout, QTableWidgetItem, QLabel, QComboBox
from view import panel_interface
from controller import database_controller
from model import subscription_model

class SubscriptionsPanel(QWidget, panel_interface.panel):
    subscription_list = None
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.layout = QVBoxLayout(self)
        self.setLayout(self.layout)
        
        self.database = database_controller.DatabaseController()
        
        self.subscribed_subscriptions_table = QTableWidget()
        column_names = [
            "Service",
            "Subscription ID"
        ]
        self.subscribed_subscriptions_table.setColumnCount(len(column_names))
        self.subscribed_subscriptions_table.setHorizontalHeaderLabels(column_names)
        self.subscribed_subscriptions_table.verticalHeader().setVisible(False)
        self.subscribed_subscriptions_table.setSortingEnabled(True)
        
        self.layout.addWidget(self.subscribed_subscriptions_table)
        
        
    def get_name(self):
        return "Subscriptions"
    
    def showEvent(self, a0: QShowEvent | None) -> None:
        subscription_rows = self.database.get_all_subscriptions()
        self.subscribed_subscriptions_table.setRowCount(len(subscription_rows))
        
        self.subscription_list = []
        row_index = 0
        for subscription_data in subscription_rows:
            subscription = subscription_model.convert_database_row_to_subscription(subscription_data)
            self.subscription_list.append(subscription)
            self.subscribed_subscriptions_table.setItem(row_index, 0, QTableWidgetItem(subscription.service))
            self.subscribed_subscriptions_table.setItem(row_index, 1, QTableWidgetItem(subscription.service_id))
            self.subscribed_subscriptions_table.setItem(row_index, 2, QTableWidgetItem("ssss"))
            
            row_index += 1
        return super().showEvent(a0)
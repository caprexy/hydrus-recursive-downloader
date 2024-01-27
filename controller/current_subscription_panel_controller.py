from PyQt6.QtWidgets import QTableWidgetItem, QTableWidget,QComboBox
from model import subscription_model
import constants


class CurrentSubscriptionPanelController:
    subscribed_subscriptions_table_pause = False
    
    def __init__(self, parent) -> None:
        self.parent = parent
        
    def set_subscribed_subscriptions_table(self, subscribed_subscriptions_table):
        self.subscribed_subscriptions_table = subscribed_subscriptions_table
        self.subscribed_subscriptions_table.itemChanged.connect(self.on_table_item_changed)
        self.subscribed_subscriptions_table_pause = True
    
    def start_listening_to_subscribed_subscriptions_table(self, subscription_list):
        self.subscribed_subscriptions_table_pause = False
        self.subscription_list = subscription_list
    def stop_listening_to_subscribed_subscriptions_table(self):
        self.subscribed_subscriptions_table_pause = True
        
    def build_subscription_row(self, subscribed_subscriptions_table: QTableWidget, row_index:int, subscription: subscription_model.Subscription):
        service_entry = QComboBox()
        service_entry.addItems(constants.SERVICES)
        service_entry.setCurrentIndex(constants.SERVICES.index(subscription.service))
        subscribed_subscriptions_table.setCellWidget(row_index, 0, service_entry)
        
        service_id_entry =  QTableWidgetItem(str(subscription.service_id))
        subscribed_subscriptions_table.setItem(row_index, 1, service_id_entry) 
        
        service_entry.currentIndexChanged.connect(lambda: (
            subscription_model.update_subscription_service(
                self.subscription_list[row_index],
                service_entry.currentText() ),
            service_entry.setCurrentIndex(constants.SERVICES.index(subscription.service)) 
            ))

    def on_table_item_changed(self, item:QTableWidgetItem):
        if self.subscribed_subscriptions_table_pause:
            return
        
        if item.column() == 1: 
            if item.text().isdigit():
                if not subscription_model.update_subscription_service_id(
                        self.subscription_list[item.row()],
                        item.text() ):
                    item.setText(str(self.subscription_list[item.row()].service_id))
            else:
                item.setText(str(self.subscription_list[item.row()].service_id))
        

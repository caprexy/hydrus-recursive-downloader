from controller import database_controller

class InputPanelController:
    def __init__(self, parent=None) -> None:
        self.database = database_controller.DatabaseController()
        
    def add_subscription(self, subscription_id:int, subscription_service:str):
        self.database.add_subscription(subscription_service, subscription_id)
    
    def delete_subscription(self, subscription_id:int, subscription_service:str):
        self.database.delete_subscription(subscription_service, subscription_id)
        
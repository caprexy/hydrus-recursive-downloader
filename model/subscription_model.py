import pickle
from controller import database_controller

database = database_controller.DatabaseController()

class Subscription():
    def __init__(self, service_id: int, service: str, associated_urls:list) -> None:
        self.service_id = service_id
        self.service = service
        self.associated_urls = associated_urls
        self.database = database
        
def update_subscription_service_id( subscription: Subscription, new_service_id):
    if database.update_subscription_service_id(
            subscription.service_id, subscription.service, new_service_id):
        subscription.service_id = new_service_id
        return True
    return False

def update_subscription_service(subscription: Subscription, new_service):
    if database.update_subscription_service(
            subscription.service_id, subscription.service, new_service):
        subscription.service = new_service
        return True
    return False

def convert_database_row_to_subscription(row:list):
    subscription = Subscription(
        row[1],
        row[2],
        pickle.loads(row[3])
    )
    
    return subscription


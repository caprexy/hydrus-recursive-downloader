import pickle

class Subscription():
    def __init__(self, service_id: int, service: str, associated_urls:list) -> None:
        self.service_id = service_id
        self.service = service
        self.associated_urls = associated_urls


def convert_database_row_to_subscription(row:list):
    subscription = Subscription(
        row[1],
        row[2],
        pickle.loads(row[3])
    )
    
    return subscription
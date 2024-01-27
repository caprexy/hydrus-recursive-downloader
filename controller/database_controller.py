import sqlite3
from controller import database_constants
import pickle

import popup as popup

class DatabaseController():
    _instance = None
    
    def __new__(cls) -> None:
        if cls._instance is not None:
            return cls._instance
        cls._instance = super(DatabaseController, cls).__new__(cls)
    
        cls.connection = sqlite3.connect(database_constants.DATABASE_NAME)
        
        cls.cursor = cls.connection.cursor()
        
        cls.cursor.execute(database_constants.INITALLIZE_TABLE_COMMAND)
        
        return cls._instance
        
    def add_subscription(self, service: str, service_id:int):
        associated_urls = []
        serialized_list = pickle.dumps(associated_urls)
        
        subscription_exists = self.cursor.execute(
            "SELECT COUNT(*) FROM subscriptions WHERE service_id = ? AND service = ?",
            (service_id, service))
        
        if subscription_exists.fetchone()[0] >= 1:
            popup.ok_popup("Error", "Subscription already exists")
            return
        
        try:
            self.cursor.execute(
                "INSERT INTO subscriptions (service_id, service, associated_urls) VALUES (?, ?, ?)", 
                (service_id, service, serialized_list))
            self.connection.commit()
        except Exception as e:
            popup.ok_popup("Error", f"Failed to add to subscriptions: {e}")
            self.connection.rollback()
        
    def delete_subscription(self, service:str, service_id:int):
        try:
            self.cursor.execute("DELETE FROM subscriptions WHERE service_id = ? AND service = ?", (service_id, service))
            self.connection.commit()
        except Exception as e:
            popup.ok_popup("Error", f"Failed to delete: {e}")
        
    def update_subscription_service_id(self, old_service_id, old_service, new_service_id):
        
        try:
            self.cursor.execute("UPDATE subscriptions SET service_id = ? WHERE service_id = ? AND service = ?",
                                (int(new_service_id), old_service_id, old_service))
            self.connection.commit()
            return True
        except Exception as e:
            popup.ok_popup("Error", f"Failed to update service_id: {e}")
            return False
    def update_subscription_service(self, old_service_id, old_service, new_service):
        try:
            self.cursor.execute("UPDATE subscriptions SET service = ? WHERE service_id = ? AND service = ?",
                                (new_service, old_service_id, old_service))
            self.connection.commit()
            return True
        except Exception as e:
            popup.ok_popup("Error", f"Failed to update service: {e}")
            return False

        
    def get_all_subscriptions(self):
        self.cursor.execute(f"SELECT * FROM {database_constants.USER_TABLE_NAME}")
        return self.cursor.fetchall()

    def __del__(self):
        self.connection.close()
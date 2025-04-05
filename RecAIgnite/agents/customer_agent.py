import sqlite3
from utils.memory import get_user_preferences

class CustomerAgent:
    def __init__(self, user_id):
        self.user_id = user_id

    def get_preferences(self):
        return get_user_preferences(self.user_id)

    def update_preferences(self, new_data):
        print(f"[CustomerAgent] Updating preferences for User {self.user_id}: {new_data}")

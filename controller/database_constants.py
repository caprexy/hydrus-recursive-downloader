DATABASE_NAME = "USERS_DATABASE"
USER_TABLE_NAME = "subscriptions"
INITALLIZE_TABLE_COMMAND = f"""
    CREATE TABLE IF NOT EXISTS {USER_TABLE_NAME} (
        unique_id INTEGER PRIMARY KEY AUTOINCREMENT,
        service_id INTEGER,
        service TEXT,
        associated_urls BLOB
    )

"""
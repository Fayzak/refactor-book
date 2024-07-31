# Глобальные объекты
database_connection = "Database Connection"
config = {"debug": True, "version": "1.0"}

def fetch_data():
    if config["debug"]:
        print("Fetching data in debug mode")
    # Использование глобального объекта database_connection
    print(f"Using {database_connection} to fetch data")
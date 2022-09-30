from app_settings import AppSettings
from app_main_window import MainWindow
from EventBinder import EventBinder
from db_main import AppDB

if __name__ == "__main__":
    # app_db = AppDB()
    app_gui = MainWindow()
    event_binder = EventBinder()

    app_gui.create_window(title=AppSettings.app_name, icon=None, window_size=AppSettings.window_size)
    app_gui.window_loop()



from app_settings import AppSettings
from app_main_window import MainWindow


if __name__ == "__main__":
    app_gui = MainWindow()
    app_gui.set_layout(layout=app_gui.get_window_layout())
    app_gui.create_window(title="test", icon=None, window_size=AppSettings.window_size)
    app_gui.read_window(AppSettings.default_read_timeout)

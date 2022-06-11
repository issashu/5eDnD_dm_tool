from app_settings import AppSettings
from app_main_window import MainWindow
from EventBinder import EventBinder


if __name__ == "__main__":
    app_gui = MainWindow()
    event_binder = EventBinder()
    app_gui.set_layout(layout=app_gui.get_window_layout())
    app_gui.create_window(title="World Map", icon=None, window_size=AppSettings.window_size)
    event_binder.bind_event(["<Button-1>", 'Window Click'], app_gui.get_window())
    app_gui.read_window()

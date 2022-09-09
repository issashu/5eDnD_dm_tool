from app_settings import AppSettings
from app_main_window import MainWindow
from EventBinder import EventBinder
from db_main import AppDB


if __name__ == "__main__":
    app_db = AppDB()
    app_gui = MainWindow()
    event_binder = EventBinder()
    app_gui.set_layout(layout=app_gui.get_window_layout())
    app_gui.create_window(title="World Map", icon=None, window_size=AppSettings.window_size)
    app_gui.set_active_window(app_gui)
    window = app_gui.get_window()
    # TODO Need to memorize somewhere return value of the draw image to have object ID. Used to modify or delete by ID
    main_map = window['main_canvas'].draw_image(filename=AppSettings.main_map, location=(0, AppSettings.window_width))
    #TODO Cleanup main from unnecessary logic
    app_gui.main_loop()


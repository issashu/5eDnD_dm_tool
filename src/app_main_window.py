from BaseWindow_class import BaseWindow
from app_settings import AppSettings


class MainWindow(BaseWindow):
    __main_window_layout = AppSettings.layout
    __map_image = None

    def get_window_layout(self):
        return self.__main_window_layout

    def set_map(self, map_file):
        self.__map_image = map_file

    def get_map(self):
        return self.__map_image

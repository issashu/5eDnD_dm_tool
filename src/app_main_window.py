from BaseWindowClass import BaseWindow
from WindowManagerClass import WindowManager
from app_settings import AppSettings


class MainWindow(BaseWindow, WindowManager):
    __main_window_layout = AppSettings.layout_main
    __map_image = None
    __version = AppSettings.app_version

    def get_window_layout(self) -> list:
        """
        Method used to retrieve the window layout list.

        Returns: The window layout as a list

        """
        return self.__main_window_layout

    def set_map(self, map_file):
        """
        Method used to set the map to be displayed on the window itself

        Args:
            map_file: a PNG map file. Keep resolution to maximum 1080p to avoid display issues.
        """
        self.__map_image = map_file

    def get_map(self):
        """
        Retrieves the map image stored in the window.

        Returns: a PNG file representing the stored map PNG image

        """
        return self.__map_image

    def get_app_version(self):
        return self.__version

    def main_loop(self):
        while self.check_is_active():
            self.read_window(300)
            print(self.event, self.values, self.check_is_active())
            self.common_events_loop()
            if self.event == 'main_canvas':
                window = self.get_window()
                # TODO Need to memorize somewhere return value of the draw image to have object ID. Used to modify or delete by ID
                # window['main_canvas'].draw_image(filename=AppSettings.pin_icon, location=self.values['main_canvas'])
                window['main_canvas'].draw_point(point=self.values['main_canvas'], size=5, color='black')

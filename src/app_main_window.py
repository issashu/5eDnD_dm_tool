from BaseWindowClass import BaseWindow
from app_settings import AppSettings
import PySimpleGUI as simple_gui


class MainWindow(BaseWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.set_layout(AppSettings.main_window_layout)
        self.__map_image = AppSettings.main_map
        self.__version = AppSettings.app_version

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

    def process_window_events(self):

        if self.event == simple_gui.WIN_CLOSED or self.event == 'Exit':
            self.close_window()
            return None

        if self.event == 'Version':
            simple_gui.popup_ok(self.get_app_version(), title="Version info")
            return None

    def window_loop(self):
        active_window = self.get_window()

        active_window['main_canvas'].draw_image(filename=AppSettings.main_map, location=(0, AppSettings.window_width))

        while self.check_is_active():
            self.read_window(300)
            print(self.event, self.values, self.check_is_active())

            self.process_window_events()

            if self.event == 'main_canvas':
                window = self.get_window()
                # TODO Need to memorize somewhere return value of the draw image to have object ID. Used to modify or delete by ID
                # window['main_canvas'].draw_image(filename=AppSettings.pin_icon, location=self.values['main_canvas'])
                window['main_canvas'].draw_point(point=self.values['main_canvas'], size=3, color='white')


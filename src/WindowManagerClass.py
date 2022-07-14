import PySimpleGUI as simple_gui


class WindowManager(object):
    """
    Singleton style window manager
    """
    __instance = None
    __current_window = None

    def __new__(cls):
        """
        Single style instantiation method. If there is no instance of the class, creates a new one.
        Otherwise, just returns the existing one.
        """
        if cls.__instance is None:
            cls.__instance = super(WindowManager, cls).__new__(cls)

        return cls.__instance

    def set_active_window(self, app_window):
        """
        Sets the window that the manager operates on
        Args:
            app_window: This the instance of the window class that will be operated on. Do not pass the PySimpleGUI window directly.
        Returns:

        """
        self.__current_window = app_window

    def get_active_window(self):
        return self.__current_window

    def common_events_loop(self):
        #TODO Clean up the list of common events. This is placeholder for now
        if self.__current_window.event == 'Version':
            simple_gui.popup_ok(self.__current_window.get_app_version(), title="Version info")
            return None

        if self.__current_window.event == simple_gui.WIN_CLOSED or self.__current_window.event == 'Exit':
            self.__current_window.close_window()
            return None



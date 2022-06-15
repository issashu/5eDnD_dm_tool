import PySimpleGUI as simple_gui


class BaseWindow(object):
    """
    Base window class, containing common window members and methods.
    Inherit this for all other app windows.
    """

    def __init__(self):
        """
        Single style instantiation method. If there is no instance of the class, creates a new one.
        Otherwise, just returns the existing one. Creates a barebone window. Use specific methods to add elements.
        """
        self.event = None
        self.values = None
        self.__window_layout = None
        self.__window = None
        self.__is_active = True

    def __getattribute__(self, name: str) -> any:
        return super(BaseWindow, self).__getattribute__(name)

    def __setattr__(self, key, value):
        self.__dict__[key] = value

    def set_layout(self, layout) -> None:
        """
        Setter method for the window layout.
        :param layout: Provide a predefined layout to use as the window one.
        """
        self.__window_layout = layout

    def create_window(self, title, icon, window_size, right_click_menu=simple_gui.MENU_RIGHT_CLICK_EDITME_VER_SETTINGS_EXIT) -> simple_gui.Window:
        """
        Creates a window based on predefined layout, title, icon and size.
        """
        self.__window = simple_gui.Window(title=title, icon=icon, size=window_size, layout=self.__window_layout,
                                          grab_anywhere=True, finalize=True, right_click_menu=right_click_menu)

    def get_window(self):
        """
        Returns the created window.

        Returns: PySimpleGUi.Window

        """
        return self.__window

    def check_is_active(self):
        """
        Returns: True if window is active or False, if it has been closed.
        """
        return self.__is_active

    def read_window(self, timeout=None):
        """
        Method used to refresh the window and read any values and events of it.
        """
        self.event, self.values = self.__window.Read(timeout)

    def close_window(self) -> None:
        """
        Method used to close the app window.
        """
        self.__is_active = False
        self.__window.close()


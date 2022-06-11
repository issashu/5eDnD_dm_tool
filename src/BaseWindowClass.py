import PySimpleGUI as simple_gui


class BaseWindow(object):
    """
    Base window class, containing common window members and methods.
    Inherit this for all other app windows.
    """
    __instance = None
    __window_layout = None
    __window = None

    def __new__(cls):
        """
        Single style instantiation method. If there is no instance of the class, creates a new one.
        Otherwise, just returns the existing one. Creates a barebone window. Use specific methods to add elements.
        """
        if cls.__instance is None:
            cls.__instance = super(BaseWindow, cls).__new__(cls)
            cls.events = None
            cls.values = None

        return cls.__instance

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

    def create_window(self, title, icon, window_size) -> simple_gui.Window:
        """
        Creates a window based on predefined layout, title, icon and size.
        """
        self.__window = simple_gui.Window(title=title, icon=icon, size=window_size, layout=self.__window_layout,
                                          grab_anywhere=True, finalize=True)

        return self.__window

    def read_window(self, timeout=None):
        """
        Method used to refresh the window and read any values and events of it.
        """
        self.events, self.values = self.__window.Read(timeout)

    def close_window(self) -> None:
        """
        Method used to close the app window.
        """
        self.__window.close()

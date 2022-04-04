import PySimpleGUI as simple_gui


class BaseWindow(object):
    __instance = None
    __window = None

    def __new__(cls) -> None:
        if cls.__instance is None:
            cls.__instance = super(BaseWindow, cls).__new__(cls)
            cls.window_layout = None

        return cls.__instance

    def __getattribute__(self, name: str) -> Any:
        return super(BaseWindow, self).__getattribute__(name)

    def __setattr__(self, key, value):
        self.__dict__[key] = value

    def create_layout(self, layout) -> list:
        
        self.window_layout = layout

        return self.window_layout

    def create_window(self, title, icon, window_size, window_layout) -> object:
        self.__window = simple_gui.Window(title=title, icon=icon, size=window_size, layout=window_layout,
                                          grab_anywhere=True)

        return self.__window



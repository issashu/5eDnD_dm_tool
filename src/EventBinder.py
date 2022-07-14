import PySimpleGUI as simple_gui


class EventBinder(object):
    """
    One Binder to rule them all and events to bind/unbind them
    """
    __instance = None

    def __new__(cls):
        """
        Single style instantiation method. If there is no instance of the class, creates a new one.
        Otherwise, just returns the existing one.
        """
        if cls.__instance is None:
            cls.__instance = super(EventBinder, cls).__new__(cls)

        return cls.__instance

    def bind_event(self, event, window):
        # type: (list, simple_gui.Window)-> None
        """
        Binds an event to a window. The event passed must be a list containing the event key name and a
        return event description.
        Args:
            event:
            window:

        Returns: None

        """
        window.bind(event[0], event[1])

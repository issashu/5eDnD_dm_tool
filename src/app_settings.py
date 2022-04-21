import PySimpleGUI as Sg


class AppSettings:
    layout = [[Sg.Text('Test window text')],
              [Sg.InputText()]]
    default_read_timeout = 300

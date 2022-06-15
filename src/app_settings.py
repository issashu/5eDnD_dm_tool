import PySimpleGUI as Sg


# noinspection PyMissingOrEmptyDocstring
class AppSettings:
    app_version = '0.1a'
    settings_file_path = '.'
    settings_file_name = 'SETTINGS.INI'
    settings = Sg.UserSettings(path=settings_file_path, filename=settings_file_name, use_config_file=True)
    window_size = (int(settings['Window Settings']['window_height']), int(settings['Window Settings']['window_width']))
    default_read_timeout = int(settings['Window Settings']['default_timeout'])
    main_map = "/Users/issashu/Library/Mobile Documents/com~apple~CloudDocs/Coding/5eDnD_app/5eDnD_dm_tool/" \
               "app_assets/Rothosia Map beautifying general.png"
    column = [[Sg.Image(source=main_map, key='map')]]
    layout = [[Sg.Column(column, size=window_size, scrollable=True)]]



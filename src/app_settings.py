import PySimpleGUI as Sg
from PIL import Image


# noinspection PyMissingOrEmptyDocstring
class AppSettings:
    app_name = 'Roleplay Map DB'
    app_version = '0.1a'
    settings_file_path = '.'
    settings_file_name = 'SETTINGS.INI'
    settings = Sg.UserSettings(path=settings_file_path, filename=settings_file_name, use_config_file=True)
    window_height = int(settings['Window Settings']['window_height'])
    window_width = int(settings['Window Settings']['window_width'])
    window_size = (window_width, window_height)
    default_read_timeout = int(settings['Window Settings']['default_timeout'])
    # FIXME Check how to set paths for assets. This below sucks big time!
    main_map = "/Users/issashu/Library/Mobile Documents/com~apple~CloudDocs/Coding/5eDnD_app/5eDnD_dm_tool/" \
               "app_assets/Images/Rothosia Map beautifying general.png"
    pin_icon = "/Users/issashu/Library/Mobile Documents/com~apple~CloudDocs/Coding/5eDnD_app/5eDnD_dm_tool/" \
               "app_assets/Images/Pin.png"

    # TODO Add error handling and separate map loading logic into own object
    map = Image.open(main_map)
    canvas_width, canvas_height = map.size

    col = [[Sg.Graph(canvas_size=map.size, graph_bottom_left=(0, 0), graph_top_right=window_size,
                     enable_events=True, drag_submits=False, expand_x=True, expand_y=True, key='main_canvas')]]

    main_window_layout = [[Sg.Column(col, scrollable=True, expand_x=True, expand_y=True, key='main_column')]]

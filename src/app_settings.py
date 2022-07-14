import PySimpleGUI as Sg


# noinspection PyMissingOrEmptyDocstring
class AppSettings:
    app_version = '0.1a'
    settings_file_path = '.'
    settings_file_name = 'SETTINGS.INI'
    settings = Sg.UserSettings(path=settings_file_path, filename=settings_file_name, use_config_file=True)
    window_height = int(settings['Window Settings']['window_height'])
    window_width = int(settings['Window Settings']['window_width'])
    window_size = (window_height, window_width)
    default_read_timeout = int(settings['Window Settings']['default_timeout'])
    # FIXME Check how to set paths for assets. This below sucks big time!
    main_map = "/Users/issashu/Library/Mobile Documents/com~apple~CloudDocs/Coding/5eDnD_app/5eDnD_dm_tool/" \
               "app_assets/Images/Rothosia Map beautifying general.png"
    pin_icon = "/Users/issashu/Library/Mobile Documents/com~apple~CloudDocs/Coding/5eDnD_app/5eDnD_dm_tool/" \
               "app_assets/Images/Pin.png"
    column = [[Sg.Image(source=main_map, key='map')]]
    layout_main = [[Sg.Graph(canvas_size=window_size, graph_bottom_left=(0, 0), graph_top_right=window_size,
                             enable_events=True, drag_submits=False, key='main_canvas')]]



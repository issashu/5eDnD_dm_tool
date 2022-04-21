import PySimpleGUI as Sg


class AppSettings:
    main_map = "/Users/issashu/Library/Mobile Documents/com~apple~CloudDocs/Coding/5eDnD_app/5eDnD_dm_tool/" \
               "app_assets/BG_map_small.png"
    window_size = (500,  400)
    layout = [[Sg.Text('Test window text')],
              [Sg.Image(source=main_map)]]
    default_read_timeout = 300

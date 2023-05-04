import dearpygui.dearpygui as dpg
import json

PrimaryWindow = 'PrimaryWindow'
ConfiguratorWindow = 'ConfiguratorWindow'
nightscout_url = 'nightscout_url'
api_token = 'api_token'
refresh_rate = 'refresh_rate'
with_direction = 'with_direction'


def get_config():
    with open(file='config.json', mode='r') as config_file: return json.load(fp=config_file)


dpg.create_context()
dpg.create_viewport(
    title='NWI-Configurator',
    small_icon='',
    large_icon='',
    min_width=400, max_width=400, width=400,
    min_height=200, max_height=200, height=200,
    resizable=False, vsync=True, decorated=True, always_on_top=True
)


class Tools:
    def __init__(self):
        pass

    @staticmethod
    def Font(path, size: int):
        with dpg.font_registry():
            fr = dpg.add_font(path, size)
        return fr

    @staticmethod
    def centerWindows():
        primary_width = dpg.get_item_width(PrimaryWindow)
        primary_height = dpg.get_item_height(PrimaryWindow)

        main_width = dpg.get_item_width(ConfiguratorWindow)
        main_height = dpg.get_item_height(ConfiguratorWindow)
        dpg.set_item_pos(item=ConfiguratorWindow, pos=[int((primary_width / 2 - main_width / 2)),
                                                       int((primary_height / 2 - main_height / 2))])

    @staticmethod
    def applyConfig():
        config = get_config()
        config[nightscout_url] = dpg.get_value(item=nightscout_url)
        config[api_token] = dpg.get_value(item=api_token)
        config[refresh_rate] = dpg.get_value(item=refresh_rate)
        config[with_direction] = dpg.get_value(item=with_direction)
        with open(file='config.json', mode='w') as config_file:
            json.dump(obj=config, fp=config_file, sort_keys=True, indent=4)
        dpg.stop_dearpygui()


class Main(Tools):
    def __init__(self):
        super().__init__()

    with dpg.window(tag=ConfiguratorWindow, no_resize=True, no_collapse=True, no_title_bar=True, no_move=True,
                    autosize=True, no_scrollbar=True, on_close=lambda: dpg.stop_dearpygui(), no_close=False,
                    no_background=True):
        dpg.add_input_text(label='NightScout URL', default_value=get_config()['nightscout_url'], tag=nightscout_url)
        dpg.add_input_text(label='NightScout API-Token', default_value=get_config()['api_token'], tag=api_token)
        dpg.add_input_float(label='Refresh Rate', default_value=get_config()['refresh_rate'], tag=refresh_rate, min_value=0.1, max_value=60, step=0.1, indent=1)
        dpg.add_checkbox(label='Show Direction?', default_value=get_config()['with_direction'], tag=with_direction)
        dpg.add_button(label='Apply', callback=lambda: Tools().applyConfig())


def run_dpg():
    with dpg.window(tag=PrimaryWindow): ...
    dpg.set_viewport_resize_callback(lambda: Tools().centerWindows())
    # dpg.bind_theme(set_default_theme())
    dpg.bind_font(font=Tools().Font(r"assets/DejaVuSans.ttf", 13))
    dpg.set_primary_window(window=PrimaryWindow, value=True)
    dpg.setup_dearpygui()
    dpg.show_viewport(minimized=False)
    dpg.start_dearpygui()
    dpg.destroy_context()


if __name__ == '__main__': run_dpg()

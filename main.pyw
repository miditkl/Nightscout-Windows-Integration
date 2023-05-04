import os, time, json, threading, ctypes, sys
try:
    import requests
    from PIL import Image, ImageFont, ImageDraw
    from PyQt5 import QtCore, QtGui, QtWidgets
except ImportError:
    stream = os.popen('pip install -r "assets/requirements.txt"')
    print(stream.read())
    import requests
    from PIL import Image, ImageFont, ImageDraw
    from PyQt5 import QtCore, QtGui, QtWidgets

if sys.platform.startswith('win'):
    if not sys.argv[0].endswith('.exe'):
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(u'CompanyName.ProductName.SubProduct.VersionInformation')


def get_config():
    with open(file='config.json', mode='r') as config_file: return json.load(fp=config_file)


if get_config()['nightscout_url'] == '' or get_config()['api_token'] == '': os.startfile('NWI-configurator.pyw')

directions = {
    'DoubleUp': {'icon': '↑↑'},
    'SingleUp': {'icon': '↑'},
    'FortyFiveUp': {'icon': u'↗'},
    'Flat': {'icon': '→'},
    'FortyFiveDown': {'icon': u'↘'},
    'SingleDown': {'icon': '↓'},
    'DoubleDown': {'icon': '↓↓'}
}


class App(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.resize(1, 1)
        self.setWindowOpacity(0)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setWindowIcon(QtGui.QIcon('assets/icon.ico'))


app = QtWidgets.QApplication(sys.argv)

tray = QtWidgets.QSystemTrayIcon(QtGui.QIcon('assets/icon.ico'))
tray.setVisible(True)
tray_menu = QtWidgets.QMenu()
OpenNWIConfig = QtWidgets.QAction('Open NWI-Configurator')
OpenNWIConfig.triggered.connect(lambda: os.startfile('NWI-configurator.pyw'))
tray_menu.addAction(OpenNWIConfig)
tray.setContextMenu(tray_menu)
widget = App()


def get_current_bsi():  # bsi -> blood sugar information
    config = get_config()
    api_url = f'{config["nightscout_url"]}/api/v1/entries/current.json?token={config["api_token"]}'
    print(requests.get(url=api_url).json()[0])
    return requests.get(url=api_url).json()[0]


def get_sgv_direction():   # sgv -> blood sugar
    current_bsi = get_current_bsi()
    sgv = current_bsi['sgv']
    for key, value in directions.items():
        if current_bsi['direction'] == key:
            return {"sgv": sgv, "direction": value}
        else:
            continue


def refresh_icon():
    try: config = get_config()
    except: return
    sgv_dir = get_sgv_direction()
    txt = f'{sgv_dir["sgv"]}{sgv_dir["direction"]["icon"]}'
    if config["with_direction"]: icotxt = txt
    else: icotxt = f'{sgv_dir["sgv"]}'
    ico = Image.new(mode="RGBA", size=(256, 256), color=(0, 0, 0, 0))
    if len(icotxt) == 2: text_size = 225
    elif len(icotxt) == 3: text_size = 125
    elif len(icotxt) == 4: text_size = 95
    else: text_size = 70
    ImageDraw.Draw(ico).text(text=icotxt, xy=(ico.width / 2, ico.height / 2), anchor='mm', fill=(255, 255, 255),
                             font=ImageFont.truetype(font='assets/DejaVuSans.ttf', size=text_size))
    ico.save(fp='assets/icon.ico', format='ico', sizes=[(256, 256)])
    widget.setWindowTitle(txt)
    widget.setWindowIcon(QtGui.QIcon('assets/icon.ico'))
    print(sgv_dir['sgv'], sgv_dir['direction']['icon'])


class ri_loop(QtCore.QThread):
    def run(self):
        while True:
            refresh_icon()
            time.sleep(get_config()["refresh_rate"] * 60)


try:
    rit = ri_loop()
    rit.finished.connect(app.exit)
    rit.start()
    widget.show()
    sys.exit(app.exec_())
except Exception as e:
    pass

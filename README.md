![Logo](http://abload.de/img/logo6xjy3.png)

# A small app that shows you your glucose value in the taskbar by using NightScout.

## Demo
![Demo](http://abload.de/img/demorrjaq.png)

## Installation

[![Download](https://img.shields.io/badge/Nightscout--Windows--Integration-download-darkgreen?style=for-the-badge&logo=GitHub)]()
[![DownloadPy](https://img.shields.io/badge/Python--3.10-download-blue?style=for-the-badge&logo=GitHub)](https://www.python.org/ftp/python/3.10.2/python-3.10.2-amd64.exe)

- Install Python 3.10 (Make sure that Python is in your path)
- Unpack the downloaded zip file
### Configure config.json with the NWI-Configurator (recommended):
- Run `main.pyw` once with administrative permissions (All necessary libraries are installed automatically, the second time the admin rights are no longer required.)
- The NWI-Configurator will ask you for the necessary information.
- It will look like this by default:  
![NWIC](https://abload.de/img/nwicbqkrh.png)
- Paste your Nightscout URL into the "Nightscout URL" field. Make sure that the URL starts with "http://" or "https://".
- Paste your Nightscout API-Token with the appropiate permissions into the "Nightscout API-Token" field.
- Change the interval in minutes, at which value is queried on nightscout at "Refresh Rate" (Default is 2 minutes).
- Click the checkbox "Show direction?", as you want to see the direction of the glucose value (as shown in the demo).

<details><summary><h3>Configure config.json manually (click to expand):</h3></summary>

#### How it looks like by default

```json
{
  "nightscout_url": "",
  "api_token": "",
  "with_direction": true,
  "refresh_rate": 2
}
```

| Key              | Value   | Description                                                                                                                                     |
|:-----------------|:--------|:------------------------------------------------------------------------------------------------------------------------------------------------|
| `nightscout_url` | `str`   | **Required**. Your Nightscout URL. (Must start with https:// or http://)                                                                        |
| `api_token`      | `str`   | **Required**. Your API key with the appropriate permissions.                                                                                    |
| `with_direction` | `bool`  | **Required**. If false, it won't show in the icon the direction your glucose reading is<br>moving (as shown in the demo), if true, then it will |
| `refresh_rate`   | `float` | **Required**. Interval in minutes at which your value is queried on nightscout.                                                                 |
</details>

### Last step
- Run `main.pyw` again but now without administrative permissions.
- It is finished and now ready to use. You can now see your glucose value in the taskbar.

## Features
- If you want to run NWI by startup, run the file named `_Add to startup.bat`
- If you want no more that NWI runs by startup, run the file named `_Remove from startup.bat` 
- If you want to start the NWI-Configurator, go to the tray icon, right-click it and select `Open NWI-Configurator`.

## Authors

- [@realSnosh](https://www.github.com/realSnosh)


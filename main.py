from datetime import datetime
from termcolor import colored
import json
import io
import importlib
import os
from pathlib import Path


def log(data, color):
    pre_text = colored("[{0}]:".format(datetime.now().strftime('%H:%M:%S')), 'white')
    text = colored(data, color)
    print(pre_text, text)


def LoadConfig():
    config_path = 'config.json'
    # check if exists - if not create one
    if os.path.isfile(config_path) and os.access(config_path, os.R_OK):
        log("Config exists and is readable!", 'green')
    else:
        log("Either config is missing or is not readable", 'red')
        log("creating file...", 'grey')
        with io.open(config_path, 'w') as db_file:
            db_file.write(json.dumps({"modules": [""]}))
        log("Edit 'config.json' and execute 'main.py' again.", 'yellow')
        input("Press Enter to exit...")
        exit()
    # read file if everything is ok
    with open(config_path) as config_file:
        data = json.load(config_file)
    return data


def CheckModules(data):
    for path in Path('Modules').rglob('*.py'):

        module_name = os.path.splitext(path.name)[0]  # most complicated way lol
        if module_name not in data['modules']:
            break

        log('Found {0} module!'.format(module_name), 'green')

        new_module = importlib.import_module("Modules." + module_name)
        new_module.Start()
        log('{0} finished!'.format(module_name), 'green')


CheckModules(LoadConfig())

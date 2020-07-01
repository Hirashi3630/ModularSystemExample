import json
import io
import importlib
import os
from pathlib import Path

# config
CONFIG_PATH = 'config.json'
# check if exists - if not create one
if os.path.isfile(CONFIG_PATH) and os.access(CONFIG_PATH, os.R_OK):
    print("Config exists and is readable!")
else:
    print("Either config is missing or is not readable, creating file...")
    with io.open(CONFIG_PATH, 'w') as db_file:
        db_file.write(json.dumps({"modules": [""]}))
    print("Edit 'config.json' and execute 'main.py' again.")
    input("Press Enter to exit...")
    exit()
# read file if everything is ok
with open(CONFIG_PATH) as config_file:
    data = json.load(config_file)

# check /Modules folder
for path in Path('Modules').rglob('*.py'):

    module_name = os.path.splitext(path.name)[0]  # most complicated way lol
    if module_name not in data['modules']:
        break

    print('Found {0} module!'.format(module_name))

    new_module = importlib.import_module("Modules." + module_name)
    new_module.Start()
    print('{0} finished!'.format(module_name))

import importlib
import os
from pathlib import Path


for path in Path('Modules').rglob('*.py'):
    module_name = os.path.splitext(path.name)[0]  # most complicated way lol
    print('Found {0} module!'.format(module_name))

    new_module = importlib.import_module("Modules." + module_name)
    new_module.Start()
    print('{0} finished!'.format(module_name))

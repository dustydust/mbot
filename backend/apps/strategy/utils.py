import os
import importlib
from django.conf import settings


def get_local_strategies(_type: str = 'dict'):
    strategies = []
    # entry_filename = os.sep + 'entry'  # for entry.py files
    entry_filename = os.sep + settings.STRATEGY_ENTRY_FILE
    strategy_base_path = '.' + os.sep + 'strategies'

    for path_entry in os.listdir(strategy_base_path):
        _checkdir = os.path.join(strategy_base_path, path_entry)
        if os.path.isdir(_checkdir) and os.path.isfile(_checkdir + entry_filename):
            if _type == 'dict':
                strategies.append({'name': path_entry, 'path': _checkdir + os.sep})
            elif _type == 'tuple':
                strategies.append((_checkdir + os.sep, path_entry))

    return strategies


def get_strategy_module_path(file_path: str) -> str:
    file_path = file_path[2:]  # Remove first "."
    file_path = file_path.replace("\\", ".").replace("/", ".")  # For Windows/Unix/Mac
    return file_path + settings.STRATEGY_ENTRY_MODULE


def get_strategy_entity(module_path: str):
    module_path = get_strategy_module_path(module_path)
    strategy_module = importlib.import_module(module_path)
    StrategyMap = getattr(strategy_module, settings.STRATEGY_MAP_CLASSNAME)
    strategy_object = StrategyMap()
    return strategy_object
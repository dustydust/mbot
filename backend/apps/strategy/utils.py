import os
from django.conf import settings

def get_local_strategies(type='dict'):
    strategies = []
    # entry_filename = os.sep + 'entry.py'
    entry_filename = os.sep + settings.STRATEGY_ENTRY_FILE
    strategy_base_path = '.' + os.sep + 'strategies'

    for path_entry in os.listdir(strategy_base_path):
        _checkdir = os.path.join(strategy_base_path, path_entry)
        if os.path.isdir(_checkdir) and os.path.isfile(_checkdir + entry_filename):
            if type == 'dict':
                strategies.append({'name' : path_entry, 'path': _checkdir + os.sep})
            elif type == 'tuple':
                strategies.append((_checkdir + os.sep, path_entry))

    return strategies

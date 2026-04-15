import os
import sys

def get_base_path():
    if getattr(sys, 'frozen', False):
        bundle_dir = os.path.dirname(sys.executable)
        return os.path.abspath(os.path.join(bundle_dir, '../../..'))
    else:
        return os.path.dirname(os.path.abspath(__file__))

def get_resource(filename):
    return os.path.join(get_base_path(), filename)
from fabric.api import *
import os

cwd = os.getcwd()
instance_path = os.path.join(cwd, 'instance')

def d():
    """Run in debug mode"""
    local('python manage.py run -i {} -D true'.format(instance_path))

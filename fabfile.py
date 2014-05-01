from fabric.api import *
import os

cwd = os.getcwd()
instance_path = os.path.join(cwd, 'instance')

env.hosts = ['198.23.165.64']
env.user = 'no'

def d():
    """Run in debug mode"""
    local('python manage.py run -i {} -D true'.format(instance_path))

def pack():
    local('python setup.py sdist --formats=gztar')

def deploy():
    name = local('python setup.py --fullname', capture=True)

    put('dist/{}.tar.gz'.format(name), '/tmp/{}.tar.gz'.format(name))

    with cd('/tmp'):
        run('tar xvzf {}.tar.gz'.format(name))

        with cd('{}'.format(name)):
            run('/home/no/.virtualenvs/rossview.reunion/bin/python setup.py install')

        run('rm -rf {} {}.tar.gz'.format(name, name))

    # make or update timestamp of instance config
    run('touch /var/www/rhs04reunion.com/instance/config.py')

def restart_remote():
    # stop app server
    # start app server
    print "IMPLEMENT ME"

def ship():
    pack()
    deploy()
    restart_remote()


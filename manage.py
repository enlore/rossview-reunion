from app import create_app
from flask.ext.script import Manager, Server

m = Manager(create_app)

m.add_option('-D', '--debug', dest='debug', required=False)
m.add_option('-i', '--instance', dest='instance_path', required=False)
m.add_command('run', Server(port=3000, host="127.0.0.1"))

if __name__ == '__main__':
    m.run()

from os import getenv
from intercom_app import create_app


env_name = getenv('APPLICATION_CONFIG')
application = create_app(env_name)

if __name__ == '__main__':
    application.run()

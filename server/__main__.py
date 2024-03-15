from server.constants import ServerConstants
from server.common import get_config
from server.routes import app

if __name__ == '__main__':
    config = get_config()
    app.run(host=config[ServerConstants.HOST], port=config[ServerConstants.PORT])

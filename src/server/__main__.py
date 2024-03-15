from src.server.constants import ServerConstants
from src.server.common import get_config
from src.server.routes import app
from src.database_handler import DatabaseHandler

if __name__ == '__main__':
    config = get_config()
    DatabaseHandler().create_database()
    app.run(host=config[ServerConstants.HOST], port=config[ServerConstants.PORT])

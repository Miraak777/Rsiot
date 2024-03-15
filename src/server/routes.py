from src.server.common import get_app
from src.server.constants import ServerConstants
from flask import Response, json
from http import HTTPStatus
from src.database_handler import DatabaseHandler

app = get_app()


@app.route('/goods_list', methods=[ServerConstants.GET])
def goods_list() -> Response:
    data = DatabaseHandler().get_goods_list()
    response = app.response_class(response=json.dumps(data), status=HTTPStatus.OK)
    return response

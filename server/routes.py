from server.common import get_app
from server.constants import ServerConstants
from flask import Response, json, request
from http import HTTPStatus

app = get_app()


@app.route('/word_list', methods=[ServerConstants.GET])
def word_list() -> Response:
    response = app.response_class(response=json.dumps(data), status=HTTPStatus.OK)
    return response

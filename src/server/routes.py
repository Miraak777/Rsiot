from src.server.common import get_app
from src.server.constants import ServerConstants
from flask import Response, json, request
from http import HTTPStatus
from src.database_handler import DatabaseHandler

app = get_app()


@app.route('/goods_list', methods=[ServerConstants.GET])
def goods_list() -> Response:
    data = DatabaseHandler().get_goods_list()
    response = app.response_class(response=json.dumps(data), status=HTTPStatus.OK)
    return response


@app.route('/add_good', methods=[ServerConstants.POST])
def add_good() -> Response:
    naming = request.form.get(ServerConstants.NAMING)
    price = request.form.get(ServerConstants.PRICE)
    category = request.form.get(ServerConstants.CATEGORY)
    DatabaseHandler().add_good(naming, price, category)
    response = app.response_class(status=HTTPStatus.OK)
    return response


@app.route('/del_good', methods=[ServerConstants.POST])
def del_good() -> Response:
    id = request.form.get(ServerConstants.ID)
    DatabaseHandler().del_good(id)
    response = app.response_class(status=HTTPStatus.OK)
    return response

@app.route('/update_good', methods=[ServerConstants.POST])
def update_good() -> Response:
    id = request.form.get(ServerConstants.ID)
    naming = request.form.get(ServerConstants.NAMING)
    price = request.form.get(ServerConstants.PRICE)
    category = request.form.get(ServerConstants.CATEGORY)
    DatabaseHandler().update_good(id, naming, price, category)
    response = app.response_class(status=HTTPStatus.OK)
    return response

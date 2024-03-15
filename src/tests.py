from unittest import TestCase, main
from src.server.routes import app
from flask import json


class RsiotLabTestCase(TestCase):

    def setUp(self):
        self.context = app.app_context()
        self.context.push()
        self.client = app.test_client()

    def tearDown(self):
        self.context.pop()

    def test_goods_list(self):
        response = self.client.get("/goods_list")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(type(json.loads(response.get_data().decode())), list)

    def test_add_good(self):
        response = self.client.post("/add_good", data={"naming": "car", "price": "9.99", "category": "auto"})
        self.assertEqual(response.status_code, 200)

    def test_update_good(self):
        response = self.client.post("/update_good", data={"id": 2, "naming": "Big car", "price": "9.99", "category": "auto"})
        self.assertEqual(response.status_code, 200)

    def test_del_good(self):
        response = self.client.post("/del_good", data={"id": 2})
        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    main()

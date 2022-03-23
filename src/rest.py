import logging
import time

from flask import Flask
from flask import request
from flask import jsonify
from flask import make_response
from flask import abort

from . import controller


app = Flask(__name__)

## ficam as rotas


@app.route('/hello')
def hello_wordl():
    return jsonify('hello world'), 200


@app.route('/list', methods=['POST'])
def create_list():
    req = request.get_json()

    title = req['title']
    items = req['items']

    list = controller.create_list(title, items)

    return jsonify(list), 201


@app.route('/lists', methods=['GET'])
def get_lists():
    lists = controller.get_lists()

    return jsonify(lists), 200


@app.route('/list/<list_id>', methods=['DELETE'])
def delete_list(list_id):
    delete_ret = controller.delete_list(list_id)

    if delete_ret.get('message'):
        return jsonify(delete_ret), 404

    return jsonify(), 204


@app.route("/list/<list_id>", methods=["PUT"])
def update_list(list_id):
    req = request.get_json()

    title = req['title']
    items = req['items']

    updated_list = controller.update_list(list_id, title, items)

    if updated_list.get('message'):
        return jsonify(updated_list), 404

    return jsonify(updated_list), 200

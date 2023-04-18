import argparse
import logging
import time
import warnings
import webbrowser

import flask
import waitress
import yaml
from flask import jsonify
from flask_cors import CORS

warnings.filterwarnings("ignore")

parser = argparse.ArgumentParser()
parser.add_argument("--config", type=str, default="config.yaml")
args = parser.parse_args()

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

config = yaml.load(open(args.config, "r"), Loader=yaml.FullLoader)

host = "localhost"
port = 9000

app = flask.Flask(__name__)
CORS(app)


@app.route('/', methods=['GET'])
def root():
    return jsonify('根目录')


@app.route('/running', methods=['GET'])
def running():
    return jsonify({"running": True})


@app.route('/status/<path:model_id>', methods=['GET'])
def status(model_id):
    return jsonify({"status": True})


@app.route('/models', methods=['POST', 'GET'])
def models():
    return jsonify("models")


if __name__ == '__main__':
    # temp folders

    print(f"[ port {port} ] what")
    webbrowser.open_new("http://{host}:{port}".format(host=host, port=port))
    waitress.serve(app, host=host, port=port)

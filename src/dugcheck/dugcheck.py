# encoding=utf-8
import logging
import os

from flask import Flask, jsonify
from flask_cors import CORS
from gevent.pywsgi import WSGIServer

logging.basicConfig()


class Dugcheck(object):
    def __init__(self):
        os.environ["FLASK_ENV"] = "development"
        self.app = Flask(__name__)
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)
        CORS(self.app)

    def question(self, question_id):
        """Wrapper.
        """
        # register a route for question_id and let the frontend hit
        # APIs on this route.
        self.logger.info(f"registering solution to question: {question_id}")

        def foo(fn):
            def handler():
                inp = {}
                out = fn(inp)
                return jsonify(out)

            self.app.add_url_rule(f"/{question_id}", f"evaluator_{question_id}", handler)
            return handler

        return foo

    def run(self, host="0.0.0.0", port="3002", debug=True):
        self.logger.info(f"server running at: http://{host}:{port}")
        http_server = WSGIServer((host, port), self.app)
        http_server.serve_forever()

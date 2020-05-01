# encoding=utf-8
import json
import logging
import os
import traceback

from flask import Flask, jsonify, request
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

    def question(self, question_id):  # noqa: C901
        """Wrapper.
        """
        # register a route for question_id and let the frontend hit
        # APIs on this route.
        def foo(fn):
            def handler():
                inp, out, status_code = {}, {}, 200

                data = request.stream.read()
                try:
                    inp = json.loads(data)
                except json.JSONDecodeError:
                    pass

                try:
                    out = fn(inp)
                except Exception as e:
                    out = {"error": str(e), "traceback": traceback.format_exc()}
                    status_code = 500

                return jsonify(out), status_code

            self.app.add_url_rule(
                f"/{question_id}", f"evaluator_{question_id}", handler, methods=["POST"]
            )
            self.logger.info(f"registering solution to question: {question_id}")
            return handler

        return foo

    def run(self, host="0.0.0.0", port=3002):
        http_server = WSGIServer((host, port), self.app)
        self.logger.info(f"server running at: http://{host}:{port}")
        http_server.serve_forever()

import json
import http.server
import socketserver
from http import HTTPStatus

from google.oauth2 import id_token
from google.auth.transport import requests


GOOGLE_CLIENT_ID = ""


class Handler(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        if self.path != "/signin-with-google":
            self.send_response(HTTPStatus.NOT_FOUND)
            self.end_headers()
            return

        token = ''
        try:
            content_length = int(self.headers['Content-Length'])
            body = self.rfile.read(content_length)
            d = json.loads(body)
            token = d['credential']
        except Exception as err:
            print("Got exception: ", err)
            self.send_response(HTTPStatus.BAD_REQUEST)
            self.end_headers()
            return

        try:
            # Specify the CLIENT_ID of the app that accesses the backend:
            idinfo = id_token.verify_oauth2_token(
                token, requests.Request(), GOOGLE_CLIENT_ID)
            print(json.dumps(idinfo, indent=4))
        except ValueError as err:
            print("Got exception: ", err)
            self.send_response(HTTPStatus.BAD_REQUEST)
            self.end_headers()
            return

        self.send_response(HTTPStatus.OK)
        self.end_headers()


httpd = socketserver.TCPServer(('', 8000), Handler)
httpd.serve_forever()

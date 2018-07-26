import pprint
from wsgiref import simple_server
import json
import falcon

import config


class EchoResource(object):
    def on_get(self, req, res):
        pprint.pprint(req)

    def on_post(self, req, res):
        payload = json.loads(req.params['payload'])
        pprint.pprint(payload)


app = falcon.API()

echo = EchoResource()

app.add_route('/', echo)

if __name__ == '__main__':
    httpd = simple_server.make_server('127.0.0.1', config.PORT, app)
    print('Ready to receive requests')
    httpd.serve_forever()

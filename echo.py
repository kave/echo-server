import pprint
from wsgiref import simple_server
import json
import falcon

import config


class EchoResource(object):
    def on_get(self, req, res):
        pprint.pprint(f'${req} Params: ${req.params}')

    def on_post(self, req, res):
        pprint.pprint(f'${req} Params: ${req.params}')
        if req.media:
            pprint.pprint(req.media)


app = falcon.API()

echo = EchoResource()

app.add_route('/', echo)

if __name__ == '__main__':
    httpd = simple_server.make_server(config.HOST, config.PORT, app)
    print(f'Ready to receive requests on {config.PORT}')
    httpd.serve_forever()

import logging

import tornado.ioloop
import tornado.web
import tornado.options
from tornado import autoreload

from ..timelog import read_record

# if DEBUG = True
logger = logging.getLogger('main')
logger.setLevel(logging.DEBUG)

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")
        logger.info(self.get_argument('image', None))
        image = self.get_argument('image', None)
        if image:
            read_record(image)

application = tornado.web.Application([
    (r"/", MainHandler),
], debug=True)

if __name__ == "__main__":
    application.listen(8888)
    ioloop = tornado.ioloop.IOLoop.instance()
    autoreload.start(ioloop)
    ioloop.start()

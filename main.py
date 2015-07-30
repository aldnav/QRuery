import logging

import tornado.ioloop
import tornado.web
import tornado.options
from tornado import autoreload

from timelog.base import read_record

# if DEBUG = True
logger = logging.getLogger('main')
logger.setLevel(logging.DEBUG)

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        image = self.get_argument('image', None)
        # TODO: Accept image
        image_url = self.get_argument('image_url', None)
        if image_url:
            try:
                response = read_record(image_url)
            except Exception, e:
                self.write(str(e))
            else:
                self.write(response)
                logger.info(response)

application = tornado.web.Application([
    (r"/", MainHandler),
], debug=True)

if __name__ == "__main__":
    application.listen(8888)
    ioloop = tornado.ioloop.IOLoop.instance()
    autoreload.start(ioloop)
    ioloop.start()

from __future__ import division, print_function

from gevent.monkey import patch_all; patch_all()

import argparse
import logging

from coup_challenge_app.flask_util import create_flask
from coup_challenge_app.endpoints import v0

logger = logging.getLogger(__name__)


class CoupApp(object):
    def __init__(self):
        super(CoupApp, self).__init__()
        self.args_parser = argparse.ArgumentParser()
        self.args_parser.add_argument(
            '--host',
            default='',
            dest="flask_host",
            required=False,
            help="Bind Flask server to specific interface"
        )
        self.args_parser.add_argument(
            '--port',
            default=8080,
            type=int,
            dest="flask_port",
            required=False,
            help="Port Flask server to specific port"
        )

        self.flask = None

    @property
    def args(self):
        """
        Returns parsed command line arguments.
        """
        return self.args_parser.parse_args()

    def run(self, flask_host=None, flask_port=None):
        """
        Run the coup challenge app.

        Args:
            flask_host (str):
                Address to bind to. Taken from args if not specified
            flask_port (int):
                Port to listen on. Taken from args if not specified

        Returns:
            None
        """
        from gevent.pywsgi import WSGIServer

        self.flask = create_flask(__package__, )
        self.flask.register_blueprint(v0.blueprint)

        if flask_host is None:
            flask_host = self.args.flask_host
        if flask_port is None:
            flask_port = self.args.flask_port

        def flask_run():
            logger.info(
                'Listening for Flask requests on %s:%u...',
                flask_host, flask_port
            )
            wsgi = WSGIServer(
                (flask_host, flask_port),
                self.flask,
                log=logger,
                error_log=logger
            )
            wsgi.serve_forever()

        def flask_shutdown():
            pass

        try:
            flask_run()
        except KeyboardInterrupt:
            logger.info("Caught SIGINT, exiting")
        finally:
            flask_shutdown()


def main():
    app = CoupApp()
    app.run()


if __name__ == '__main__':
    main()

import argparse
import logging
import logging.handlers
import os
import threading

from concord232 import api
from concord232 import concord

LOG_FORMAT = '%(asctime)-15s %(module)s %(levelname)s %(message)s'


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--config', default='config.ini',
                        metavar='FILE',
                        help='Path to config file')
    parser.add_argument('--debug', default=False, action='store_true',
                        help='Enable debug')
    parser.add_argument('--log', default=None,
                        metavar='FILE',
                        help='Path to log file')
    parser.add_argument('--serial', default=None,
                        metavar='PORT',
                        help='Serial port to open for stream')
    parser.add_argument('--listen', default='0.0.0.0',
                        metavar='ADDR',
                        help='Listen address (defaults to 0.0.0.0 (all interfaces))')
    parser.add_argument('--port', default=5007, type=int,
                        help='Listen port (defaults to 5007)')
    args = parser.parse_args()

    LOG = logging.getLogger()
    LOG.setLevel(logging.DEBUG)
    formatter = logging.Formatter(LOG_FORMAT)
    istty = os.isatty(0)

    if args.debug and not istty:
        debug_handler = logging.handlers.RotatingFileHandler(
            'debug.log',
            maxBytes=1024*1024*10,
            backupCount=3)
        debug_handler.setFormatter(formatter)
        debug_handler.setLevel(logging.DEBUG)
        LOG.addHandler(debug_handler)

    if istty:
        verbose_handler = logging.StreamHandler()
        verbose_handler.setFormatter(formatter)
        verbose_handler.setLevel(args.debug and logging.DEBUG or logging.INFO)
        LOG.addHandler(verbose_handler)

    if args.log:
        log_handler = logging.handlers.RotatingFileHandler(
            args.log,
            maxBytes=1024*1024*10,
            backupCount=3)
        log_handler.setFormatter(formatter)
        log_handler.setLevel(logging.DEBUG)
        LOG.addHandler(log_handler)

    LOG.info('Ready')
    logging.getLogger('connectionpool').setLevel(logging.WARNING)

    if args.serial:
        ctrl = concord.AlarmPanelInterface(args.serial, 0.25, LOG)
    else:
        LOG.error('Serial and baudrate are required')
        return

    api.CONTROLLER = ctrl

    t = threading.Thread(target=ctrl.message_loop)
    t.daemon = True
    t.start()
    
    api.app.run(debug=True, host=args.listen, port=args.port, threaded=True)

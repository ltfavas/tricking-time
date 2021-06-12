from .base import *

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'console': {
            '()': 'colorlog.ColoredFormatter',
            # exact format is not important, this is the minimum information
            'format': '[%(asctime)s] %(log_color)s %(name)-12s (%(levelname)s) %(message)s',
            'datefmt': '%d/%b/%Y %H:%M:%S',
            'log_colors': {
                'DEBUG':    'cyan',
                'INFO':     'green',
                'WARNING':  'yellow',
                'ERROR':    'red',
                'CRITICAL': 'bold_red',
            },
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'console',
        },
    },
    'loggers': {
        # root logger
        '': {
            'level': 'DEBUG',
            'handlers': ['console'],
        },
    },
}

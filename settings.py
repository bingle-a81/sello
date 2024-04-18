import logging
se_log=logging.getLogger(__name__)
def get_logger():

    se_log.info("This is a test")

log_dict={
    'version': 1,
     'disable_existing_loggers': False,
        'formatters': {
                'simple': {
                    'format': '{asctime} - {levelname} - {name} - {message}',
                    'style': '{'}
    },
    'handlers': {'file': 
                 {'class': 'logging.handlers.RotatingFileHandler', 
                  'level': 'DEBUG',
                   'formatter':'simple', 
                   'filename': 'debug.log',
                   'maxBytes': 1024*1024, 
                   'backupCount': 5}
                   },
    'loggers': {'': {'handlers': ['file'], 'level': 'DEBUG', 'propagate': True}},
}

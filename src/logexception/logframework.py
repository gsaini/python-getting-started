'''
Create a logging framework to collect all the logs into a single file .Please follow all the tasks below.

 - Make the logger customisable, with settings being retrieved from a configuration file
 - Create the logging framework; every time the logger is invoked, it should log into a single file
 - The logging format has to be generic with the module_name, function_name, line_no : message
'''
import os
import logging.config

import yaml

def setup_logging(
    path='config/logger.yaml',
):
    if os.path.exists(path):
        with open(path, 'rt') as f:
            config = yaml.safe_load(f.read())
        logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=logging.INFO)

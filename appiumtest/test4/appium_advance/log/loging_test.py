#! /usr/bin/env/python
# -*- coding:utf-8 -*-
import logging
# logging.basicConfig(level=logging.DEBUG)
logging.basicConfig(level=logging.INFO,filename='runlog.log',format='%(asctime)s %(filename)s[line:%(lineno)d]%(levelname)s%(message)s')

logging.debug("debug info")
logging.info('hello world')
logging.warning('warning')
logging.error('error')
logging.critical('critical info')

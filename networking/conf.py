import sys, os
sys.path.append(os.path.abspath('../common/'))

from conf import *

version = '4.11.99'
release = '4.11.99'

project = "RTEMS Networking User Manual"

latex_documents = [
	('index', 'networking.tex', u'RTEMS Networking User Manual', u'RTEMS Documentation Project', 'manual'),
]

import sys, os
sys.path.append(os.path.abspath('../common/'))

from conf import *

version = '4.11.99'
release = '4.11.99'

project = "RTEMS POSIX API Guide"

latex_documents = [
	('index', 'posix-users.tex', u'RTEMS POSIX API Guide', u'RTEMS Documentation Project', 'manual'),
]
